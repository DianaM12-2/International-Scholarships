from dataclasses import dataclass, field
from typing import Optional, List
from enum import Enum


class DegreeLevel(Enum):
    UNDERGRADUATE = "undergraduate"
    GRADUATE      = "graduate"
    PHD           = "phd"
    ANY           = "any"


class VisaStatus(Enum):
    F1_OPT   = "F-1 OPT"
    F1_STUDY = "F-1 Student"
    J1       = "J-1"
    ANY      = "Any"


@dataclass
class Scholarship:
    """
    Represents an international student scholarship opportunity.
    Demonstrates Python OOP with dataclasses, enums, and type hints.
    """
    id:              int
    name:            str
    provider:        str
    amount:          str
    deadline:        str
    degree_levels:   List[str]
    eligible_visas:  List[str]
    fields_of_study: List[str]
    description:     str
    url:             str
    country:         str          = "USA"
    renewable:       bool         = False
    gpa_requirement: Optional[float] = None
    tags:            List[str]    = field(default_factory=list)

    def matches_filter(self, degree: str = None, visa: str = None,
                       field: str = None, search: str = None) -> bool:
        """Check if scholarship matches given filter criteria."""
        if degree and degree.lower() not in [d.lower() for d in self.degree_levels]:
            if "any" not in [d.lower() for d in self.degree_levels]:
                return False
        if visa and visa not in self.eligible_visas:
            if "Any" not in self.eligible_visas:
                return False
        if field and field.lower() not in [f.lower() for f in self.fields_of_study]:
            if "Any" not in self.fields_of_study:
                return False
        if search:
            search_lower = search.lower()
            searchable = (self.name + self.provider + self.description +
                         " ".join(self.tags)).lower()
            if search_lower not in searchable:
                return False
        return True

    def to_dict(self) -> dict:
        return {
            "id":              self.id,
            "name":            self.name,
            "provider":        self.provider,
            "amount":          self.amount,
            "deadline":        self.deadline,
            "degree_levels":   self.degree_levels,
            "eligible_visas":  self.eligible_visas,
            "fields_of_study": self.fields_of_study,
            "description":     self.description,
            "url":             self.url,
            "country":         self.country,
            "renewable":       self.renewable,
            "gpa_requirement": self.gpa_requirement,
            "tags":            self.tags,
        }
