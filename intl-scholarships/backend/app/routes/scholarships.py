from flask import Blueprint, request, jsonify
from app.services.scholarship_service import ScholarshipService

scholarships_bp = Blueprint("scholarships", __name__)
_service = ScholarshipService()


@scholarships_bp.route("", methods=["GET"])
def get_all():
    """GET /api/v1/scholarships — get all or filtered scholarships."""
    degree = request.args.get("degree")
    visa   = request.args.get("visa")
    field  = request.args.get("field")
    search = request.args.get("search")

    if any([degree, visa, field, search]):
        results = _service.filter(degree=degree, visa=visa,
                                  field=field, search=search)
    else:
        results = _service.get_all()

    return jsonify({
        "count":   len(results),
        "results": results
    }), 200


@scholarships_bp.route("/<int:scholarship_id>", methods=["GET"])
def get_one(scholarship_id):
    """GET /api/v1/scholarships/<id> — get single scholarship."""
    result = _service.get_by_id(scholarship_id)
    if not result:
        return jsonify({"error": f"Scholarship {scholarship_id} not found"}), 404
    return jsonify(result), 200


@scholarships_bp.route("/stats", methods=["GET"])
def get_stats():
    """GET /api/v1/scholarships/stats — get summary statistics."""
    return jsonify(_service.get_stats()), 200


@scholarships_bp.route("/fields", methods=["GET"])
def get_fields():
    """GET /api/v1/scholarships/fields — get all available fields of study."""
    return jsonify(_service.get_fields()), 200


@scholarships_bp.route("/visa-types", methods=["GET"])
def get_visa_types():
    """GET /api/v1/scholarships/visa-types — get all visa types."""
    return jsonify(_service.get_visa_types()), 200
