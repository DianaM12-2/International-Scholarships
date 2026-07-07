export default function StatsBar({ stats }) {
  const items = [
    { label: "Total Scholarships", value: stats.total,         icon: "🎓" },
    { label: "OPT Friendly",       value: stats.opt_friendly,  icon: "✅" },
    { label: "F-1 Eligible",       value: stats.f1_friendly,   icon: "🌎" },
    { label: "Renewable",          value: stats.renewable,     icon: "↻"  },
  ];

  return (
    <div className="stats-bar">
      {items.map(({ label, value, icon }) => (
        <div key={label} className="stat-item">
          <span className="stat-icon">{icon}</span>
          <span className="stat-value">{value}</span>
          <span className="stat-label">{label}</span>
        </div>
      ))}
    </div>
  );
}
