export function FilterPanel({ filters, onChange, onReset }) {
  const degrees = ["undergraduate", "graduate", "phd"];
  const visas   = ["F-1 Student", "F-1 OPT", "J-1", "Any"];
  const fields  = ["Computer Science", "Engineering", "STEM", "Mathematics",
                   "Sciences", "Cybersecurity", "Any"];

  return (
    <div className="filter-panel">
      <div className="filter-header">
        <h3>Filters</h3>
        <button className="btn-text" onClick={onReset}>Reset all</button>
      </div>

      <div className="filter-group">
        <label>Degree Level</label>
        <select value={filters.degree} onChange={e => onChange("degree", e.target.value)}>
          <option value="">All Degrees</option>
          {degrees.map(d => <option key={d} value={d}>{d.charAt(0).toUpperCase() + d.slice(1)}</option>)}
        </select>
      </div>

      <div className="filter-group">
        <label>Visa Status</label>
        <select value={filters.visa} onChange={e => onChange("visa", e.target.value)}>
          <option value="">All Visa Types</option>
          {visas.map(v => <option key={v} value={v}>{v}</option>)}
        </select>
      </div>

      <div className="filter-group">
        <label>Field of Study</label>
        <select value={filters.field} onChange={e => onChange("field", e.target.value)}>
          <option value="">All Fields</option>
          {fields.map(f => <option key={f} value={f}>{f}</option>)}
        </select>
      </div>
    </div>
  );
}

export default FilterPanel;
