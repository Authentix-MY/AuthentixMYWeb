-- =====================================================================
-- Authentix — database setup (Supabase → SQL Editor → paste ALL → Run; safe to re-run)
-- Tables: enquiries, drops, reviews, events, heartbeat, admins
-- Public visitors can ONLY: submit an enquiry, log anonymous events,
-- read published drops and visible reviews, and call ping().
-- Everything else requires an admin login.
-- =====================================================================
create extension if not exists pgcrypto;

-- ---------- admins ----------
create table if not exists public.admins (email text primary key);
alter table public.admins enable row level security;
-- >>> CHANGE THIS to the email you will log in with <<<
insert into public.admins (email) values ('you@example.com') on conflict do nothing;

create or replace function public.is_admin() returns boolean
language plpgsql stable security definer set search_path = public as $$
begin
  return exists (select 1 from public.admins where lower(email) = lower(coalesce(auth.jwt() ->> 'email', '')));
end $$;
drop policy if exists "admins read self" on public.admins;
create policy "admins read self" on public.admins for select to authenticated using (public.is_admin());

-- ---------- enquiries ----------
create table if not exists public.enquiries (
  id          uuid primary key default gen_random_uuid(),
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now(),
  name        text not null check (char_length(name) between 1 and 120),
  whatsapp    text not null check (char_length(whatsapp) between 4 and 40),
  event       text not null check (char_length(event) between 1 and 200),
  city        text check (char_length(city) <= 80),
  service     text check (char_length(service) <= 40),
  category    text check (char_length(category) <= 60),
  quantity    text check (char_length(quantity) <= 10),
  notes       text check (char_length(notes) <= 2000),
  lang        text default 'en' check (lang in ('en','zh')),
  consent     boolean not null default false,
  session_id  text check (char_length(session_id) <= 64),
  utm_source  text check (char_length(utm_source) <= 60),
  status      text not null default 'new' check (status in ('new','quoted','paid','secured','closed'))
);
create index if not exists enquiries_created_idx on public.enquiries (created_at desc);
alter table public.enquiries enable row level security;
drop policy if exists "public can submit" on public.enquiries;
create policy "public can submit" on public.enquiries for insert to anon, authenticated
  with check (consent = true and status = 'new');
drop policy if exists "admin full access" on public.enquiries;
create policy "admin full access" on public.enquiries for all to authenticated
  using (public.is_admin()) with check (public.is_admin());

-- ---------- drops ----------
create table if not exists public.drops (
  id             text primary key default ('drop-' || substr(gen_random_uuid()::text, 1, 8)),
  created_at     timestamptz not null default now(),
  updated_at     timestamptz not null default now(),
  artist         text not null,
  tour_en        text, tour_zh text,
  city           text not null default 'SG' check (city in ('SG','KL','OTHER')),
  venue_en       text, venue_zh text,
  date_label_en  text, date_label_zh text,
  event_date     date,
  status         text not null default 'soon' check (status in ('preorder','soon','available','soldout')),
  note_en        text, note_zh text,
  image_url      text,
  published      boolean not null default true
);
alter table public.drops enable row level security;
drop policy if exists "public reads published" on public.drops;
create policy "public reads published" on public.drops for select to anon, authenticated using (published = true);
drop policy if exists "admin full access" on public.drops;
create policy "admin full access" on public.drops for all to authenticated using (public.is_admin()) with check (public.is_admin());

-- ---------- reviews ----------
create table if not exists public.reviews (
  id             text primary key default ('rev-' || substr(gen_random_uuid()::text, 1, 8)),
  created_at     timestamptz not null default now(),
  handle         text not null,
  text           text not null,
  text_zh        text,
  tags           text[] not null default '{}',
  event          text,
  source         text default 'Carousell',
  screenshot_url text,
  visible        boolean not null default true,
  sort_order     int not null default 0
);
alter table public.reviews enable row level security;
drop policy if exists "public reads visible" on public.reviews;
create policy "public reads visible" on public.reviews for select to anon, authenticated using (visible = true);
drop policy if exists "admin full access" on public.reviews;
create policy "admin full access" on public.reviews for all to authenticated using (public.is_admin()) with check (public.is_admin());

-- ---------- events (anonymous website analytics) ----------
create table if not exists public.events (
  id          bigint generated always as identity primary key,
  created_at  timestamptz not null default now(),
  name        text not null check (name in ('page_view','lang_switch','drop_view','drop_enquire','click_whatsapp','click_carousell','click_instagram','form_submit','faq_open','review_open')),
  path        text check (char_length(path) <= 200),
  lang        text check (char_length(lang) <= 5),
  session_id  text check (char_length(session_id) <= 64),
  referrer    text check (char_length(referrer) <= 200),
  utm_source  text check (char_length(utm_source) <= 60),
  device      text check (char_length(device) <= 10),
  props       jsonb not null default '{}'::jsonb check (pg_column_size(props) < 2000)
);
create index if not exists events_created_idx on public.events (created_at desc);
alter table public.events enable row level security;
drop policy if exists "public can log" on public.events;
create policy "public can log" on public.events for insert to anon, authenticated with check (true);
drop policy if exists "admin reads" on public.events;
create policy "admin reads" on public.events for select to authenticated using (public.is_admin());

-- ---------- FAQ ----------
create table if not exists public.faqs (
  id          text primary key default ('faq-' || substr(gen_random_uuid()::text, 1, 8)),
  created_at  timestamptz not null default now(),
  q_en        text not null, a_en text not null,
  q_zh        text, a_zh text,
  visible     boolean not null default true,
  sort_order  int not null default 0
);
alter table public.faqs enable row level security;
drop policy if exists "public reads visible" on public.faqs;
create policy "public reads visible" on public.faqs for select to anon, authenticated using (visible = true);
drop policy if exists "admin full access" on public.faqs;
create policy "admin full access" on public.faqs for all to authenticated using (public.is_admin()) with check (public.is_admin());

-- ---------- site settings (contact links + on/off switches) ----------
create table if not exists public.settings (
  key         text primary key,
  value       jsonb not null default '{}'::jsonb,
  updated_at  timestamptz not null default now()
);
alter table public.settings enable row level security;
drop policy if exists "public reads settings" on public.settings;
create policy "public reads settings" on public.settings for select to anon, authenticated using (true);
drop policy if exists "admin full access" on public.settings;
create policy "admin full access" on public.settings for all to authenticated using (public.is_admin()) with check (public.is_admin());

-- ---------- heartbeat + keep-alive ping ----------
create table if not exists public.heartbeat (id int primary key default 1 check (id = 1), last_ping timestamptz, ok boolean default true);
insert into public.heartbeat (id, last_ping) values (1, now()) on conflict do nothing;
alter table public.heartbeat enable row level security;
drop policy if exists "admin reads" on public.heartbeat;
create policy "admin reads" on public.heartbeat for select to authenticated using (public.is_admin());
create or replace function public.ping() returns timestamptz
language plpgsql security definer set search_path = public as $$
declare t timestamptz;
begin
  update public.heartbeat set last_ping = now(), ok = true where id = 1 returning last_ping into t;
  return t;
end $$;
grant execute on function public.ping() to anon, authenticated;

-- ---------- updated_at ----------
create or replace function public.touch() returns trigger language plpgsql as $$ begin new.updated_at = now(); return new; end $$;
drop trigger if exists t_enq on public.enquiries; create trigger t_enq before update on public.enquiries for each row execute function public.touch();
drop trigger if exists t_drops on public.drops;   create trigger t_drops before update on public.drops for each row execute function public.touch();

-- ---------- media storage (drop covers, review screenshots) ----------
-- Skipped automatically if Supabase Storage isn't switched on yet;
-- in that case run storage.sql later (see README).
do $$
begin
  if to_regclass('storage.buckets') is null or to_regclass('storage.objects') is null then
    raise notice 'Storage not available yet - skipped. Run storage.sql once Storage is enabled.';
    return;
  end if;
  insert into storage.buckets (id, name, public) values ('media', 'media', true) on conflict (id) do nothing;
  drop policy if exists "public reads media" on storage.objects;
  create policy "public reads media" on storage.objects for select to anon, authenticated using (bucket_id = 'media');
  drop policy if exists "admin uploads media" on storage.objects;
  create policy "admin uploads media" on storage.objects for insert to authenticated with check (bucket_id = 'media' and public.is_admin());
  drop policy if exists "admin updates media" on storage.objects;
  create policy "admin updates media" on storage.objects for update to authenticated using (bucket_id = 'media' and public.is_admin());
  drop policy if exists "admin deletes media" on storage.objects;
  create policy "admin deletes media" on storage.objects for delete to authenticated using (bucket_id = 'media' and public.is_admin());
end $$;
