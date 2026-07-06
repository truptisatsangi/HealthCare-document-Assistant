from enum import Enum

class Category(str, Enum):
    GENERAL = "general"
    SUMMARY = "summary"
    CURRENT_MEDICATION = "current_medication"
    DISEASE_QUERY = "disease_query"
    RECOMMENDATION = "recommendation"

class reportType(str, Enum):
    BLOOD_TEST = "blood_test"
    GENERAL_REPORT = "general_report"
    DIABETES_REPORT = "diabetes_report"
    MRI = "mri"
    CT_SCAN = "ct_scan"
    X_RAY = "x_ray"