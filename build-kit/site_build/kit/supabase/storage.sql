-- Authentix — media storage only (run if schema.sql said "Storage not available yet")
-- Supabase → Storage: open it once so it is enabled, then SQL Editor → paste ALL → Run.
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
