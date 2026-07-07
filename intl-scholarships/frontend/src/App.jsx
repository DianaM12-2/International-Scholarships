import { useState, useEffect } from "react";
import ScholarshipCard from "./components/ScholarshipCard";
import FilterPanel from "./components/FilterPanel";
import StatsBar from "./components/StatsBar";
import SearchBar from "./components/SearchBar";
import { fetchScholarships, fetchStats } from "./services/api";
import "./styles/App.css";

export default function App() {
  const [scholarships, setScholarships] = useState([]);
  const [stats, setStats]               = useState(null);
  const [loading, setLoading]           = useState(true);
  const [error, setError]               = useState(null);
  const [filters, setFilters]           = useState({ degree: "", visa: "", field: "", search: "" });
  const [selected, setSelected]         = useState(null);

  useEffect(() => {
    loadData();
  }, [filters]);

  async function loadData() {
    try {
      setLoading(true);
      const [data, statsData] = await Promise.all([
        fetchScholarships(filters),
        fetchStats(),
      ]);
      setScholarships(data.results);
      setStats(statsData);
    } catch (err) {
      setError("Failed to load scholarships. Make sure the backend is running.");
    } finally {
      setLoading(false);
    }
  }

  function handleFilterChange(key, value) {
    setFilters(prev => ({ ...prev, [key]: value }));
  }

  function handleReset() {
    setFilters({ degree: "", visa: "", field: "", search: "" });
  }

  return (
    <div className="app">
      <header className="hero">
        <div className="hero-content">
          <div className="hero-badge">🌎 International Students</div>
          <h1>Scholarship Finder</h1>
          <p className="hero-subtitle">
            Discover scholarships open to F-1, OPT, J-1, and international students studying in the US.
          </p>
          {stats && <StatsBar stats={stats} />}
        </div>
      </header>

      <main className="main">
        <aside className="sidebar">
          <SearchBar
            value={filters.search}
            onChange={v => handleFilterChange("search", v)}
          />
          <FilterPanel
            filters={filters}
            onChange={handleFilterChange}
            onReset={handleReset}
          />
        </aside>

        <section className="results">
          {loading ? (
            <div className="loading">
              <div className="spinner" />
              <p>Finding scholarships...</p>
            </div>
          ) : error ? (
            <div className="error-msg">{error}</div>
          ) : scholarships.length === 0 ? (
            <div className="empty">
              <p>No scholarships match your filters.</p>
              <button className="btn-reset" onClick={handleReset}>Clear Filters</button>
            </div>
          ) : (
            <>
              <div className="results-header">
                <h2>{scholarships.length} Scholarship{scholarships.length !== 1 ? "s" : ""} Found</h2>
              </div>
              <div className="cards-grid">
                {scholarships.map(s => (
                  <ScholarshipCard
                    key={s.id}
                    scholarship={s}
                    onClick={() => setSelected(s)}
                  />
                ))}
              </div>
            </>
          )}
        </section>
      </main>

      {selected && (
        <div className="modal-overlay" onClick={() => setSelected(null)}>
          <div className="modal" onClick={e => e.stopPropagation()}>
            <button className="modal-close" onClick={() => setSelected(null)}>✕</button>
            <h2>{selected.name}</h2>
            <p className="modal-provider">{selected.provider}</p>
            <div className="modal-amount">{selected.amount}</div>
            <p className="modal-desc">{selected.description}</p>
            <div className="modal-details">
              <div><strong>Deadline:</strong> {selected.deadline}</div>
              <div><strong>Degree:</strong> {selected.degree_levels.join(", ")}</div>
              <div><strong>Eligible Visas:</strong> {selected.eligible_visas.join(", ")}</div>
              <div><strong>Fields:</strong> {selected.fields_of_study.join(", ")}</div>
              {selected.gpa_requirement && <div><strong>Min GPA:</strong> {selected.gpa_requirement}</div>}
              <div><strong>Renewable:</strong> {selected.renewable ? "Yes ✅" : "No"}</div>
            </div>
            <div className="modal-tags">
              {selected.tags.map(tag => <span key={tag} className="tag">#{tag}</span>)}
            </div>
            <a href={selected.url} target="_blank" rel="noopener noreferrer" className="btn-apply">
              Apply Now →
            </a>
          </div>
        </div>
      )}
    </div>
  );
}
