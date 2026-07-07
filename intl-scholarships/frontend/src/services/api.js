const BASE = import.meta.env.VITE_API_URL || "http://localhost:5000/api/v1";

async function get(path) {
  const res = await fetch(`${BASE}${path}`);
  if (!res.ok) throw new Error(`API error: ${res.statusText}`);
  return res.json();
}

export function fetchScholarships({ degree = "", visa = "", field = "", search = "" } = {}) {
  const params = new URLSearchParams();
  if (degree) params.set("degree", degree);
  if (visa)   params.set("visa",   visa);
  if (field)  params.set("field",  field);
  if (search) params.set("search", search);
  const query = params.toString() ? `?${params.toString()}` : "";
  return get(`/scholarships${query}`);
}

export const fetchStats     = () => get("/scholarships/stats");
export const fetchFields    = () => get("/scholarships/fields");
export const fetchVisaTypes = () => get("/scholarships/visa-types");
