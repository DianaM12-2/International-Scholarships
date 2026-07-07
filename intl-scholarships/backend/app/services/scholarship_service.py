from app.models.scholarship import Scholarship
from typing import List, Optional


# ──────────────────────────────────────────────
# Scholarship Database (seed data)
# ──────────────────────────────────────────────

SCHOLARSHIPS = [
    Scholarship(
        id=1, name="Google Generation Scholarship",
        provider="Google", amount="$10,000/year",
        deadline="December 1, 2026",
        degree_levels=["undergraduate", "graduate"],
        eligible_visas=["F-1 Student", "F-1 OPT", "Any"],
        fields_of_study=["Computer Science", "Computer Engineering", "STEM"],
        description="Google's scholarship for students studying computer science or related fields. Open to international students. Recipients also attend a retreat at Google HQ.",
        url="https://buildyourfuture.withgoogle.com/scholarships/google-scholarship",
        renewable=True, gpa_requirement=3.0,
        tags=["google", "cs", "tech", "stem", "international", "OPT", "F-1"]
    ),
    Scholarship(
        id=2, name="Microsoft Scholarship Program",
        provider="Microsoft", amount="$5,000/year",
        deadline="February 1, 2027",
        degree_levels=["undergraduate"],
        eligible_visas=["F-1 Student", "Any"],
        fields_of_study=["Computer Science", "Engineering", "STEM"],
        description="Microsoft's scholarship supporting students pursuing degrees in STEM fields. Includes mentorship opportunities and a chance to intern at Microsoft.",
        url="https://careers.microsoft.com/students/us/en/usscholarship",
        renewable=False, gpa_requirement=3.0,
        tags=["microsoft", "tech", "stem", "undergraduate", "international"]
    ),
    Scholarship(
        id=3, name="Hispanic Scholarship Fund",
        provider="Hispanic Scholarship Fund", amount="$500–$5,000",
        deadline="February 15, 2027",
        degree_levels=["undergraduate", "graduate"],
        eligible_visas=["F-1 Student", "F-1 OPT", "Any"],
        fields_of_study=["Any"],
        description="The largest non-profit organization supporting Latino higher education. Provides scholarships, mentoring, and career development to Latino students across all fields.",
        url="https://www.hsf.net/scholarship",
        renewable=True, gpa_requirement=2.5,
        tags=["hispanic", "latino", "diversity", "any field", "international", "OPT"]
    ),
    Scholarship(
        id=4, name="Society of Women Engineers Scholarship",
        provider="Society of Women Engineers (SWE)", amount="$1,000–$17,000",
        deadline="May 1, 2027",
        degree_levels=["undergraduate", "graduate"],
        eligible_visas=["F-1 Student", "F-1 OPT", "Any"],
        fields_of_study=["Engineering", "Computer Science", "STEM"],
        description="Multiple scholarship programs for women pursuing engineering and computer science degrees. Open to international students studying in the US.",
        url="https://swe.org/scholarships",
        renewable=True, gpa_requirement=3.0,
        tags=["women in tech", "engineering", "SWE", "diversity", "international"]
    ),
    Scholarship(
        id=5, name="Fulbright Foreign Student Program",
        provider="U.S. Department of State", amount="Full funding",
        deadline="Varies by country",
        degree_levels=["graduate", "phd"],
        eligible_visas=["J-1"],
        fields_of_study=["Any"],
        description="The Fulbright Program is the U.S. government's flagship international educational exchange program. Provides full funding for graduate study, research, or teaching.",
        url="https://foreign.fulbrightonline.org",
        renewable=False, gpa_requirement=3.0,
        tags=["fulbright", "government", "graduate", "research", "international", "full funding"]
    ),
    Scholarship(
        id=6, name="AAUW International Fellowships",
        provider="American Association of University Women", amount="$20,000–$35,000",
        deadline="November 1, 2026",
        degree_levels=["graduate", "phd"],
        eligible_visas=["F-1 Student", "J-1", "Any"],
        fields_of_study=["Any"],
        description="Fellowships for women who are not US citizens or permanent residents for full-time graduate or postdoctoral study in the United States.",
        url="https://www.aauw.org/resources/programs/fellowships-grants/current-opportunities/international/",
        renewable=False, gpa_requirement=3.0,
        tags=["women", "graduate", "research", "international", "AAUW"]
    ),
    Scholarship(
        id=7, name="QuestBridge National College Match",
        provider="QuestBridge", amount="Full 4-year scholarship",
        deadline="September 26, 2026",
        degree_levels=["undergraduate"],
        eligible_visas=["F-1 Student", "Any"],
        fields_of_study=["Any"],
        description="Links high-achieving students from low-income backgrounds with leading US colleges for full four-year scholarships. Open to international students with financial need.",
        url="https://www.questbridge.org",
        renewable=True, gpa_requirement=3.5,
        tags=["full scholarship", "undergraduate", "low income", "international", "first gen"]
    ),
    Scholarship(
        id=8, name="OPTnation STEM Scholarship",
        provider="OPTnation", amount="$1,000",
        deadline="Rolling — Quarterly",
        degree_levels=["undergraduate", "graduate"],
        eligible_visas=["F-1 OPT"],
        fields_of_study=["Computer Science", "Engineering", "STEM", "Mathematics"],
        description="Scholarship specifically designed for international students on F-1 OPT pursuing STEM careers in the United States. No GPA requirement.",
        url="https://www.optnation.com/blog/scholarship-for-opt-students/",
        renewable=False, gpa_requirement=None,
        tags=["OPT", "F-1 OPT", "STEM", "international", "no GPA requirement"]
    ),
    Scholarship(
        id=9, name="National GEM Consortium Fellowship",
        provider="GEM Consortium", amount="Full tuition + stipend",
        deadline="November 15, 2026",
        degree_levels=["graduate", "phd"],
        eligible_visas=["F-1 Student", "F-1 OPT", "Any"],
        fields_of_study=["Engineering", "Computer Science", "STEM"],
        description="Full tuition fellowship for underrepresented students in STEM graduate programs. Includes paid internships with employer sponsors like Google, Microsoft, and IBM.",
        url="https://www.gemfellowship.org",
        renewable=True, gpa_requirement=3.0,
        tags=["GEM", "fellowship", "diversity", "STEM", "graduate", "full funding", "OPT"]
    ),
    Scholarship(
        id=10, name="National Science Foundation Graduate Research Fellowship",
        provider="NSF", amount="$37,000/year + $12,000 tuition",
        deadline="October 2026",
        degree_levels=["graduate", "phd"],
        eligible_visas=["F-1 Student", "Any"],
        fields_of_study=["Computer Science", "Engineering", "Sciences", "STEM"],
        description="NSF's flagship graduate fellowship supporting outstanding students in STEM. Fellows receive 3 years of funding and access to NSF-funded research opportunities.",
        url="https://www.nsfgrfp.org",
        renewable=True, gpa_requirement=3.5,
        tags=["NSF", "research", "graduate", "PhD", "STEM", "government"]
    ),
    Scholarship(
        id=11, name="AFCEA STEM Scholarship",
        provider="AFCEA Educational Foundation", amount="$2,500–$5,000",
        deadline="November 2026",
        degree_levels=["undergraduate", "graduate"],
        eligible_visas=["F-1 Student", "F-1 OPT", "Any"],
        fields_of_study=["Computer Science", "Engineering", "Cybersecurity", "STEM"],
        description="Scholarships for students pursuing STEM degrees with a focus on communications, IT, and cybersecurity. Open to international students at US institutions.",
        url="https://www.afcea.org/site/foundation/scholarships",
        renewable=False, gpa_requirement=3.0,
        tags=["cybersecurity", "IT", "STEM", "international", "engineering"]
    ),
    Scholarship(
        id=12, name="Point Foundation Scholarship",
        provider="Point Foundation", amount="Up to $14,000/year",
        deadline="January 26, 2027",
        degree_levels=["undergraduate", "graduate"],
        eligible_visas=["F-1 Student", "F-1 OPT", "Any"],
        fields_of_study=["Any"],
        description="Scholarships for LGBTQ+ students demonstrating strong leadership and commitment to their communities. Open to international students studying in the US.",
        url="https://pointfoundation.org",
        renewable=True, gpa_requirement=3.0,
        tags=["LGBTQ", "diversity", "leadership", "international", "any field"]
    ),
    Scholarship(
        id=13, name="Palantir Women in Technology Scholarship",
        provider="Palantir", amount="$10,000",
        deadline="April 2027",
        degree_levels=["undergraduate", "graduate"],
        eligible_visas=["F-1 Student", "F-1 OPT", "Any"],
        fields_of_study=["Computer Science", "Engineering", "Mathematics", "STEM"],
        description="Palantir's scholarship for women studying CS or related technical fields. Includes potential internship opportunity at Palantir.",
        url="https://www.palantir.com/careers/students/scholarship/wit-scholarship/",
        renewable=False, gpa_requirement=None,
        tags=["women in tech", "palantir", "CS", "engineering", "international", "OPT"]
    ),
    Scholarship(
        id=14, name="Generation Google Scholarship: Women in Computing",
        provider="Google", amount="$10,000",
        deadline="December 2026",
        degree_levels=["undergraduate", "graduate"],
        eligible_visas=["F-1 Student", "F-1 OPT", "Any"],
        fields_of_study=["Computer Science", "Computer Engineering", "STEM"],
        description="Scholarship to support women in computing. Recipients invited to attend the annual Google Scholars' Retreat.",
        url="https://buildyourfuture.withgoogle.com/scholarships/generation-google-scholarship",
        renewable=True, gpa_requirement=3.0,
        tags=["google", "women in tech", "CS", "international", "OPT"]
    ),
    Scholarship(
        id=15, name="Immigrants Rising Scholarship Fund",
        provider="Immigrants Rising", amount="$2,500–$10,000",
        deadline="March 1, 2027",
        degree_levels=["undergraduate", "graduate"],
        eligible_visas=["F-1 Student", "F-1 OPT", "Any"],
        fields_of_study=["Any"],
        description="Scholarships specifically for immigrant students including undocumented, DACA, international, and mixed-status students pursuing higher education in the US.",
        url="https://immigrantsrising.org/resource/scholarships-for-undocumented-students/",
        renewable=False, gpa_requirement=None,
        tags=["immigrant", "international", "DACA", "any field", "F-1", "OPT", "first gen"]
    ),
]


class ScholarshipService:
    """Service layer for scholarship queries and filtering."""

    def __init__(self):
        self._data = SCHOLARSHIPS

    def get_all(self) -> list:
        return [s.to_dict() for s in self._data]

    def get_by_id(self, scholarship_id: int) -> Optional[dict]:
        match = next((s for s in self._data if s.id == scholarship_id), None)
        return match.to_dict() if match else None

    def filter(self, degree: str = None, visa: str = None,
               field: str = None, search: str = None) -> list:
        results = [s for s in self._data
                   if s.matches_filter(degree=degree, visa=visa,
                                       field=field, search=search)]
        return [s.to_dict() for s in results]

    def get_stats(self) -> dict:
        total = len(self._data)
        opt_friendly = sum(1 for s in self._data if "F-1 OPT" in s.eligible_visas)
        f1_friendly  = sum(1 for s in self._data if "F-1 Student" in s.eligible_visas or "Any" in s.eligible_visas)
        renewable    = sum(1 for s in self._data if s.renewable)
        grad_count   = sum(1 for s in self._data if "graduate" in s.degree_levels)
        undergrad    = sum(1 for s in self._data if "undergraduate" in s.degree_levels)
        return {
            "total":         total,
            "opt_friendly":  opt_friendly,
            "f1_friendly":   f1_friendly,
            "renewable":     renewable,
            "graduate":      grad_count,
            "undergraduate": undergrad,
        }

    def get_fields(self) -> list:
        fields = set()
        for s in self._data:
            fields.update(s.fields_of_study)
        return sorted(list(fields))

    def get_visa_types(self) -> list:
        visas = set()
        for s in self._data:
            visas.update(s.eligible_visas)
        return sorted(list(visas))
