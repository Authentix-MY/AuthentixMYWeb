// Runs once a day on Netlify. Touches the database so the free Supabase
// project is never marked inactive (it pauses after ~7 quiet days).
export default async () => {
  const url = process.env.SUPABASE_URL;
  const key = process.env.SUPABASE_ANON_KEY;
  if (!url || !key) return new Response("Missing SUPABASE_URL / SUPABASE_ANON_KEY", { status: 500 });
  const res = await fetch(`${url}/rest/v1/rpc/ping`, {
    method: "POST",
    headers: { apikey: key, "Content-Type": "application/json", ...(key.startsWith("eyJ") ? { Authorization: `Bearer ${key}` } : {}) },
    body: "{}",
  });
  console.log("keep-alive", res.status);
  return new Response(res.ok ? "ok" : "ping failed", { status: res.ok ? 200 : 502 });
};

export const config = { schedule: "@daily" };
