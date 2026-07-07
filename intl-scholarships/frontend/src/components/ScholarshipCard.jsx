export default function ScholarshipCard({ scholarship: s, onClick }) {
  const isOptFriendly = s.eligible_visas.includes("F-1 OPT") || s.eligible_visas.includes("Any");

  return (
    <div className="card" onClick={onClick}>
      <div className="card-header">
        <div className="card-badges">
          {isOptFriendly && <span className="badge badge-opt">✓ OPT Friendly</span>}
          {s.renewable && <span className="badge badge-renewable">↻ Renewable</span>}
        </div>
        <div className="card-amount">{s.amount}</div>
      </div>

      <h3 className="card-title">{s.name}</h3>
      <p className="card-provider">{s.provider}</p>
      <p className="card-desc">{s.description.slice(0, 120)}...</p>

      <div className="card-meta">
        <div className="meta-item">
          <span className="meta-label">Deadline</span>
          <span className="meta-value">{s.deadline}</span>
        </div>
        <div className="meta-item">
          <span className="meta-label">Degree</span>
          <span className="meta-value">{s.degree_levels.join(", ")}</span>
        </div>
      </div>

      <div className="card-visas">
        {s.eligible_visas.slice(0, 3).map(v => (
          <span key={v} className="visa-tag">{v}</span>
        ))}
      </div>

      <button className="card-cta">View Details →</button>
    </div>
  );
}
