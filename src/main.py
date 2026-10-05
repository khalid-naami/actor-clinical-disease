"""Apify Actor Entrypoint: Chronic Disease Clinical Intelligence & Medical Breakthroughs."""

import asyncio
import os
from apify import Actor
from src.diseases_database import CHRONIC_DISEASES_DB
from src.nutrition_engine import DIET_PROTOCOLS
from src.exercise_prescription import EXERCISE_PROTOCOLS
from src.medical_journal_client import MedicalJournalClient
from src.biomarker_calculator import BiomarkerCalculator

async def main() -> None:
    async with Actor:
        actor_input = await Actor.get_input() or {}
        target_disease = actor_input.get("targetDisease", "All 7 Chronic Diseases")
        include_nutrition = bool(actor_input.get("includeNutritionProtocols", True))
        include_exercise = bool(actor_input.get("includeExercisePrescriptions", True))
        include_breakthroughs = bool(actor_input.get("includeCuratedBreakthroughs", True))
        fetch_live_trials = bool(actor_input.get("fetchLiveEuropePmcTrials", True))
        api_key = actor_input.get("apiKey") or os.getenv("APIFY_TOKEN") or os.getenv("API_KEY", "")

        # Patient risk calculation parameters
        sim_age = int(actor_input.get("patientSimulationAge", 52))
        sim_hba1c = float(actor_input.get("patientSimulationHba1c", 6.2))
        sim_systolic = int(actor_input.get("patientSimulationSystolicBp", 135))
        sim_ldl = int(actor_input.get("patientSimulationLdlC", 125))
        sim_bmi = float(actor_input.get("patientSimulationBmi", 27.8))

        Actor.log.info(f"Initiating Clinical Disease Intelligence for: {target_disease}")
        if api_key:
            Actor.log.info("API Key / Token authentication provided.")

        # Determine target list of diseases
        if target_disease == "All 7 Chronic Diseases" or target_disease not in CHRONIC_DISEASES_DB:
            selected_diseases = list(CHRONIC_DISEASES_DB.keys())
        else:
            selected_diseases = [target_disease]

        journal_client = MedicalJournalClient()
        dataset_records = []

        # 1. Process each disease profile
        for d_name in selected_diseases:
            d_info = CHRONIC_DISEASES_DB[d_name]
            record = {
                "record_type": "disease_clinical_profile",
                "disease_name": d_name,
                "icd10": d_info.get("icd10"),
                "category": d_info.get("category"),
                "global_prevalence": d_info.get("prevalence_global"),
                "annual_mortality": d_info.get("annual_mortality"),
                "guidelines": d_info.get("guidelines"),
                "summary": d_info.get("summary"),
                "pathophysiology": d_info.get("pathophysiology"),
                "primary_biomarkers": d_info.get("primary_biomarkers"),
                "pharmacological_pillars": d_info.get("pharmacological_pillars"),
                "key_complications": d_info.get("key_complications"),
                "risk_factors": d_info.get("risk_factors")
            }

            # Medical Nutrition
            if include_nutrition and d_name in DIET_PROTOCOLS:
                record["medical_nutrition_protocol"] = DIET_PROTOCOLS[d_name]

            # FITT Exercise
            if include_exercise and d_name in EXERCISE_PROTOCOLS:
                record["fitt_exercise_prescription"] = EXERCISE_PROTOCOLS[d_name]

            # Curated Breakthroughs
            if include_breakthroughs:
                record["landmark_breakthrough_publications"] = journal_client.get_curated_breakthroughs(d_name)

            # Live Europe PMC Trials
            if fetch_live_trials:
                Actor.log.info(f"Harvesting live Europe PMC clinical trials for: {d_name}...")
                trials = journal_client.fetch_live_recent_trials(d_name, max_results=3)
                record["recent_live_clinical_trials"] = trials

            dataset_records.append(record)

        # 2. Patient Stratification Assessment Record
        patient_risk_eval = BiomarkerCalculator.calculate_patient_risk(
            age=sim_age,
            gender="Male",
            systolic_bp=sim_systolic,
            diastolic_bp=85,
            hba1c=sim_hba1c,
            fasting_glucose=112,
            ldl_c=sim_ldl,
            hdl_c=45,
            egfr=88,
            bmi=sim_bmi,
            weekly_exercise_min=90,
            is_smoker=False,
            family_history_cad=True,
            family_history_diabetes=True
        )

        dataset_records.append({
            "record_type": "patient_risk_stratification_simulation",
            "patient_parameters": {
                "age": sim_age,
                "hba1c": sim_hba1c,
                "systolic_bp": sim_systolic,
                "ldl_c": sim_ldl,
                "bmi": sim_bmi
            },
            "risk_stratification_results": patient_risk_eval
        })

        if dataset_records:
            await Actor.push_data(dataset_records)
            Actor.log.info(f"Successfully pushed {len(dataset_records)} clinical intelligence records to Apify dataset.")

        # Save executive summary in Key-Value store for Apify MCP & instant API tools
        summary_payload = {
            "targetDisease": target_disease,
            "diseasesAnalyzedCount": len(selected_diseases),
            "diseases": selected_diseases,
            "patientRiskAssessment": {
                "diabetesRisk": patient_risk_eval.get("diabetes_risk_category", "Moderate"),
                "cvRisk": patient_risk_eval.get("cardiovascular_risk_category", "Moderate"),
                "generalAdvice": patient_risk_eval.get("lifestyle_prescription", "Adhere to FITT protocol.")
            },
            "diseasesOverview": [
                {
                    "name": d["disease_name"],
                    "icd10": d["icd10"],
                    "prevalence": d["global_prevalence"],
                    "diet": d.get("medical_nutrition_protocol", {}).get("diet_name", "Clinical Protocol")
                }
                for d in dataset_records if d.get("record_type") == "disease_clinical_profile"
            ]
        }
        await Actor.set_value("OUTPUT", summary_payload)
        Actor.log.info("Stored clinical summary OUTPUT in Key-Value store.")

if __name__ == "__main__":
    asyncio.run(main())
