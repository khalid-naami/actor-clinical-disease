"""Apify Actor Entrypoint: Clinical Disease Epidemiology & Biomarker Risk Engine."""

import asyncio
import math
import os
import sys
from typing import Any, Dict, List

# Ensure root directory is in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apify import Actor
from src.diseases_database import CHRONIC_DISEASES_DB
from src.biomarker_calculator import BiomarkerCalculator
from src.nutrition_engine import NutritionEngine
from src.exercise_prescription import ExercisePrescriptionEngine
from src.medical_journal_client import MedicalJournalClient


DISEASE_NAME_ALIASES: Dict[str, str] = {
    "Type 2 Diabetes Mellitus": "Type 2 Diabetes Mellitus",
    "Cardiovascular & Heart Disease": "Cardiovascular & Heart Disease",
    "Hypertension (High Blood Pressure)": "Hypertension (High Blood Pressure)",
    "Oncology & Cancer Prevention": "Oncology & Common Solid Tumors",
    "Oncology & Common Solid Tumors": "Oncology & Common Solid Tumors",
    "Chronic Kidney Disease (CKD)": "Chronic Kidney Disease",
    "Chronic Kidney Disease": "Chronic Kidney Disease",
    "Chronic Obstructive Pulmonary Disease (COPD)": "COPD & Chronic Respiratory Diseases",
    "COPD & Chronic Respiratory Diseases": "COPD & Chronic Respiratory Diseases",
    "Alzheimer's Disease & Cognitive Decline": "Alzheimer's & Neurodegenerative Disorders",
    "Alzheimer's & Neurodegenerative Disorders": "Alzheimer's & Neurodegenerative Disorders",
}


def sanitize_record(record: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively strips None, NaN, and Infinity values for clean JSON schema validation."""
    cleaned: Dict[str, Any] = {}
    for k, v in record.items():
        if v is None:
            continue
        if isinstance(v, float) and (math.isnan(v) or math.isinf(v)):
            continue
        if isinstance(v, dict):
            cleaned[k] = sanitize_record(v)
        elif isinstance(v, list):
            cleaned_list = []
            for item in v:
                if isinstance(item, dict):
                    cleaned_list.append(sanitize_record(item))
                elif item is not None and not (isinstance(item, float) and (math.isnan(item) or math.isinf(item))):
                    cleaned_list.append(item)
            cleaned[k] = cleaned_list
        else:
            cleaned[k] = v
    return cleaned


def resolve_disease_names(target_disease: str) -> List[str]:
    """Resolves user input disease selection (including input_schema aliases) to DB keys."""
    if not target_disease or target_disease == "All Major Chronic Diseases (Full Report)":
        return list(CHRONIC_DISEASES_DB.keys())
    mapped = DISEASE_NAME_ALIASES.get(target_disease, target_disease)
    if mapped in CHRONIC_DISEASES_DB:
        return [mapped]
    for db_key in CHRONIC_DISEASES_DB:
        if target_disease.lower() in db_key.lower() or db_key.lower() in target_disease.lower():
            return [db_key]
    return list(CHRONIC_DISEASES_DB.keys())


async def main() -> None:
    async with Actor:
        actor_input = await Actor.get_input() or {}
        target_disease = actor_input.get("targetDisease", "All Major Chronic Diseases (Full Report)")
        include_pubmed = bool(actor_input.get("includePubmedLiterature", True))
        include_lifestyle = bool(actor_input.get("includeNutritionAndExercise", True))
        run_risk_sim = bool(actor_input.get("runBiomarkerSimulation", True))
        api_key = actor_input.get("apiKey") or os.getenv("APIFY_TOKEN") or os.getenv("API_KEY", "")

        # Patient simulation inputs
        p_age = int(actor_input.get("patientAge", 54))
        p_bmi = float(actor_input.get("patientBmi", 28.5))
        p_sbp = int(actor_input.get("patientSystolicBp", 138))
        p_hba1c = float(actor_input.get("patientHba1c", 6.1))
        p_ldl = int(actor_input.get("patientLdl", 135))
        p_egfr = int(actor_input.get("patientEgfr", 78))
        p_smoker = bool(actor_input.get("patientSmoking", False))

        diseases_to_analyze = resolve_disease_names(target_disease)

        Actor.log.info(f"Running Clinical Epidemiology Analysis on {len(diseases_to_analyze)} disease domain(s)...")
        if api_key:
            Actor.log.info("API Key / Token authentication provided.")

        journal_client = MedicalJournalClient()
        dataset_records: List[Dict[str, Any]] = []

        # 1. Process each clinical condition
        for disease_name in diseases_to_analyze:
            d_info = CHRONIC_DISEASES_DB[disease_name]
            record: Dict[str, Any] = {
                "record_type": "disease_clinical_profile",
                "disease_name": disease_name,
                "icd_11_code": d_info.get("icd_11"),
                "category": d_info.get("category"),
                "global_prevalence": d_info.get("global_prevalence"),
                "annual_mortality": d_info.get("annual_mortality"),
                "guidelines": d_info.get("guidelines"),
                "summary": d_info.get("summary"),
                "pathophysiology": d_info.get("pathophysiology"),
                "primary_biomarkers": d_info.get("primary_biomarkers"),
                "pharmacological_pillars": d_info.get("pharmacological_pillars"),
                "key_complications": d_info.get("key_complications"),
                "risk_factors": d_info.get("risk_factors"),
            }

            if include_lifestyle:
                record["medical_nutrition_protocol"] = NutritionEngine.get_protocol(disease_name)
                record["fitt_exercise_prescription"] = ExercisePrescriptionEngine.get_prescription(disease_name)

            if include_pubmed:
                Actor.log.info(f"Fetching PubMed clinical trials & reviews for: {disease_name}...")
                try:
                    articles = journal_client.fetch_pubmed_articles(disease_name, max_results=5)
                except Exception as e:
                    Actor.log.warning(f"PubMed lookup warning for {disease_name}: {e}")
                    articles = []
                record["pubmed_clinical_studies"] = articles

            dataset_records.append(sanitize_record(record))

        # 2. Run Patient Biomarker Risk Stratification Simulation
        patient_risk_eval: Dict[str, Any] = {}
        if run_risk_sim:
            Actor.log.info("Calculating Patient Biomarker Risk Stratification (HbA1c, ASCVD, eGFR)...")
            patient_risk_eval = BiomarkerCalculator.calculate_patient_risk(
                age=p_age,
                bmi=p_bmi,
                systolic_bp=p_sbp,
                hba1c=p_hba1c,
                ldl_mg_dl=p_ldl,
                egfr=p_egfr,
                smoker=p_smoker,
                family_history=True,
                weekly_exercise_mins=90
            )
            patient_risk_eval["diabetes_risk_category"] = patient_risk_eval.get("t2d_stage", "Normal")
            patient_risk_eval["cardiovascular_risk_category"] = patient_risk_eval.get("cv_category", "Low")
            patient_risk_eval["lifestyle_prescription"] = patient_risk_eval.get("recommendations", [])

            dataset_records.append(sanitize_record({
                "record_type": "patient_risk_stratification_simulation",
                "patient_parameters": {
                    "age": p_age,
                    "bmi": p_bmi,
                    "systolic_bp_mmhg": p_sbp,
                    "hba1c_pct": p_hba1c,
                    "ldl_cholesterol_mg_dl": p_ldl,
                    "egfr_ml_min": p_egfr,
                    "is_smoker": p_smoker,
                },
                "risk_stratification_results": patient_risk_eval,
            }))

        if dataset_records:
            await Actor.push_data(dataset_records)
            Actor.log.info(f"Pushed {len(dataset_records)} clinical records to Apify Dataset.")

        # 3. Save Executive Summary to Key-Value Store (OUTPUT)
        summary_payload = {
            "targetDisease": target_disease,
            "diseasesAnalyzedCount": len(diseases_to_analyze),
            "diseasesList": diseases_to_analyze,
            "totalRecordsPushed": len(dataset_records),
            "patientRiskAssessment": {
                "diabetesRiskCategory": patient_risk_eval.get("t2d_stage", "N/A"),
                "diabetesRiskPct": patient_risk_eval.get("t2d_risk_pct"),
                "cardiovascularRiskCategory": patient_risk_eval.get("cv_category", "N/A"),
                "ascvd10YrRiskPct": patient_risk_eval.get("ascvd_risk_pct"),
                "kdigoStage": patient_risk_eval.get("kdigo_stage", "N/A"),
                "bloodPressureStage": patient_risk_eval.get("bp_stage", "N/A"),
                "compositeHealthIndex": patient_risk_eval.get("health_index"),
                "lifestylePrescription": patient_risk_eval.get("recommendations", []),
            } if run_risk_sim else None,
        }
        await Actor.set_value("OUTPUT", sanitize_record(summary_payload))
        if not dataset_records:
            await Actor.fail(status_message="No clinical disease records were produced.")
            return
        Actor.log.info("Executive summary saved to Key-Value Store 'OUTPUT'.")


if __name__ == "__main__":
    asyncio.run(main())
