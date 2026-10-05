# Apify Actor: Chronic Disease Clinical Intelligence & Medical Breakthroughs 🩺🧬

A clinical-grade chronic pathology intelligence Actor covering 7 major non-communicable diseases: **Type 2 Diabetes Mellitus**, **Cardiovascular & CAD**, **Essential Hypertension**, **Oncology**, **Chronic Kidney Disease (CKD)**, **COPD**, and **Alzheimer's Disease**.

---

## 🌟 Key Features

1. **Comprehensive Disease Pathophysiology & Biomarkers**: Detailed ICD-10 profiles, international guidelines (ADA, AHA, ESC, KDIGO, GOLD), laboratory target reference ranges (HbA1c, ApoB, eGFR, hs-CRP, etc.), and frontline pharmacotherapy pillars.
2. **Evidence-Based Medical Nutrition**: Precision macronutrient splits, therapeutic micronutrient targets, beneficial anti-inflammatory superfoods, and strictly prohibited pro-inflammatory/atherogenic items.
3. **FITT Clinical Exercise Prescriptions**: Frequency, Intensity, Time, Type protocols, target heart rate training zones, cellular signaling mechanisms (AMPK, GLUT4, eNOS), and safety contraindications.
4. **Curated Landmark Breakthroughs**: Peer-reviewed trial data from *The New England Journal of Medicine*, *The Lancet*, *JAMA*, and *Nature Medicine* (e.g. Tirzepatide SURPASS, Inclisiran ORION, CRISPR PCSK9 base editing, p-tau217 biomarkers).
5. **Live Europe PMC Clinical Trials Harvester**: Real-time queries to Europe PMC / PubMed for recent human randomized controlled trials and clinical study abstracts.
6. **Multi-System Patient Risk Stratification**: Automated cardiovascular (ASCVD), diabetes metabolic risk, and CKD staging algorithms.

---

## 📥 Input Schema

| Field | Type | Default | Description |
|---|---|---|---|
| `targetDisease` | Select | `"All 7 Chronic Diseases"` | Disease filter or select all 7 conditions. |
| `includeNutritionProtocols` | Boolean | `true` | Include therapeutic nutrition plans and macro splits. |
| `includeExercisePrescriptions` | Boolean | `true` | Include FITT exercise protocols and contraindications. |
| `includeCuratedBreakthroughs` | Boolean | `true` | Include landmark NEJM/Lancet trial summaries. |
| `fetchLiveEuropePmcTrials` | Boolean | `true` | Harvester recent open-access trials from Europe PMC. |
| `patientSimulationAge` | Integer | `52` | Patient age for risk simulation. |
| `patientSimulationHba1c` | Float | `6.2` | HbA1c percentage. |
| `patientSimulationSystolicBp` | Integer | `135` | Systolic blood pressure (mmHg). |
| `patientSimulationLdlC` | Integer | `125` | LDL-C (mg/dL). |
| `patientSimulationBmi` | Float | `27.8` | Body Mass Index. |

---

## 📤 Output Dataset Format

```json
{
  "record_type": "disease_clinical_profile",
  "disease_name": "Type 2 Diabetes Mellitus",
  "icd10": "E11",
  "medical_nutrition_protocol": {
    "diet_name": "Low-Glycemic Mediterranean-Ketogenic Hybrid (L-Med)",
    "macros": { "Carbohydrates": 25, "Proteins": 25, "Healthy Fats": 50 },
    "therapeutic_superfoods": [ ... ],
    "strictly_prohibited_foods": [ ... ]
  },
  "fitt_exercise_prescription": {
    "aerobic_fitt": { ... },
    "resistance_fitt": { ... }
  },
  "landmark_breakthrough_publications": [ ... ],
  "recent_live_clinical_trials": [ ... ]
}
```

---

## 🚀 How to Run Locally

```bash
cd actor-clinical-disease
pip install -r requirements.txt
python -m src.main
```
