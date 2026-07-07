import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from app import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as c:
        yield c


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "healthy"


def test_get_all_scholarships(client):
    res = client.get("/api/v1/scholarships")
    assert res.status_code == 200
    data = res.get_json()
    assert "count" in data
    assert "results" in data
    assert data["count"] > 0


def test_get_scholarship_by_id(client):
    res = client.get("/api/v1/scholarships/1")
    assert res.status_code == 200
    data = res.get_json()
    assert data["id"] == 1
    assert "name" in data
    assert "provider" in data


def test_get_scholarship_not_found(client):
    res = client.get("/api/v1/scholarships/9999")
    assert res.status_code == 404


def test_filter_by_degree(client):
    res = client.get("/api/v1/scholarships?degree=graduate")
    assert res.status_code == 200
    data = res.get_json()
    assert data["count"] > 0


def test_filter_by_visa_opt(client):
    res = client.get("/api/v1/scholarships?visa=F-1 OPT")
    assert res.status_code == 200
    data = res.get_json()
    assert data["count"] > 0
    for s in data["results"]:
        assert "F-1 OPT" in s["eligible_visas"] or "Any" in s["eligible_visas"]


def test_filter_by_search(client):
    res = client.get("/api/v1/scholarships?search=google")
    assert res.status_code == 200
    data = res.get_json()
    assert data["count"] > 0
    for s in data["results"]:
        assert "google" in (s["name"] + s["provider"] + s["description"]).lower()


def test_filter_by_field(client):
    res = client.get("/api/v1/scholarships?field=Computer Science")
    assert res.status_code == 200
    assert res.get_json()["count"] > 0


def test_get_stats(client):
    res = client.get("/api/v1/scholarships/stats")
    assert res.status_code == 200
    data = res.get_json()
    for key in ["total", "opt_friendly", "f1_friendly", "renewable"]:
        assert key in data
    assert data["total"] > 0
    assert data["opt_friendly"] > 0


def test_get_fields(client):
    res = client.get("/api/v1/scholarships/fields")
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)
    assert len(res.get_json()) > 0


def test_get_visa_types(client):
    res = client.get("/api/v1/scholarships/visa-types")
    assert res.status_code == 200
    visa_types = res.get_json()
    assert "F-1 OPT" in visa_types
