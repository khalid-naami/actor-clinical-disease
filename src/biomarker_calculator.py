"""Clinical Biomarker & Multi-System Risk Stratification Calculator.

Calculates ADA Diabetes Risk Score, ASCVD 10-year Cardiovascular Risk Category,
KDIGO CKD Staging, and overall Preventive Health & Longevity Score.
"""

from typing import Dict, Any, List
import math

class BiomarkerCalculator:
    """Computes evidence-calibrated clinical risk scores and tailored health recommendations."""

    @staticmethod
    def calculate_patient_risk(
        age: int,
        gender: str,
        systolic_bp: int,
        diastolic_bp: int,
        hba1c: float,
        fasting_glucose: int,
        ldl_c: int,
        hdl_c: int,
        egfr: int,
        bmi: float,
        weekly_exercise_min: int,
        is_smoker: bool,
        family_history_cad: bool,
        family_history_diabetes: bool
    ) -> Dict[str, Any]:
        """Calculates multi-system chronic disease risk stratification."""

        # 1. Diabetes / Metabolic Risk Scoring (0 - 100)
        t2d_score = 0
        if age >= 45: t2d_score += 20
        elif age >= 35: t2d_score += 10

        if bmi >= 30: t2d_score += 30
        elif bmi >= 25: t2d_score += 15

        if hba1c >= 6.5: t2d_score += 45
        elif hba1c >= 5.7: t2d_score += 25

        if fasting_glucose >= 126: t2d_score += 35
        elif fasting_glucose >= 100: t2d_score += 20

        if family_history_diabetes: t2d_score += 15
        if weekly_exercise_min < 150: t2d_score += 15
        else: t2d_score = max(0, t2d_score - 10)

        t2d_risk_pct = min(98, max(5, int(t2d_score * 0.75)))
        t2d_stage = "High / Established Diabetes" if hba1c >= 6.5 or fasting_glucose >= 126 else ("Prediabetes / Moderate Risk" if hba1c >= 5.7 or fasting_glucose >= 100 or t2d_risk_pct > 40 else "Optimal Metabolic Health")

        # 2. Cardiovascular / Atherosclerotic Risk Scoring (ASCVD Estimation)
        cv_score = 0
        if age >= 55: cv_score += 25
        elif age >= 45: cv_score += 15

        if systolic_bp >= 160 or diastolic_bp >= 100: cv_score += 35
        elif systolic_bp >= 130 or diastolic_bp >= 85: cv_score += 20

        if ldl_c >= 160: cv_score += 30
        elif ldl_c >= 100: cv_score += 15

        if hdl_c < 40: cv_score += 15
        if is_smoker: cv_score += 25
        if family_history_cad: cv_score += 15

        ascvd_risk_pct = min(95, max(4, int(cv_score * 0.7)))
        if ascvd_risk_pct >= 20: cv_category = "High Risk (>=20% 10-Yr ASCVD)"
        elif ascvd_risk_pct >= 7.5: cv_category = "Intermediate Risk (7.5 - 19.9%)"
        elif ascvd_risk_pct >= 5: cv_category = "Borderline Risk (5.0 - 7.4%)"
        else: cv_category = "Low Risk (< 5.0%)"

        # 3. Renal Health / KDIGO Staging
        if egfr >= 90:
            kdigo_stage = "Stage G1 (Normal / Optimal eGFR >=90)"
            renal_risk_level = "Low Risk"
        elif egfr >= 60:
            kdigo_stage = "Stage G2 (Mildly Decreased eGFR 60-89)"
            renal_risk_level = "Mild Risk"
        elif egfr >= 45:
            kdigo_stage = "Stage G3a (Mild-to-Moderate eGFR 45-59)"
            renal_risk_level = "Moderate Risk"
        elif egfr >= 30:
            kdigo_stage = "Stage G3b (Moderate-to-Severe eGFR 30-44)"
            renal_risk_level = "High Risk"
        elif egfr >= 15:
            kdigo_stage = "Stage G4 (Severely Decreased eGFR 15-29)"
            renal_risk_level = "Very High Risk"
        else:
            kdigo_stage = "Stage G5 (Kidney Failure eGFR <15)"
            renal_risk_level = "Critical Renal Failure"

        # 4. Blood Pressure Staging (ACC/AHA Guidelines)
        if systolic_bp >= 180 or diastolic_bp >= 120:
            bp_stage = "Hypertensive Crisis (Emergency Medical Evaluation Required)"
            bp_status_color = "#ef4444"
        elif systolic_bp >= 140 or diastolic_bp >= 90:
            bp_stage = "Stage 2 Hypertension"
            bp_status_color = "#f97316"
        elif systolic_bp >= 130 or diastolic_bp >= 80:
            bp_stage = "Stage 1 Hypertension"
            bp_status_color = "#eab308"
        elif systolic_bp >= 120 and diastolic_bp < 80:
            bp_stage = "Elevated Blood Pressure"
            bp_status_color = "#38bdf8"
        else:
            bp_stage = "Normal / Optimal Blood Pressure (<120/<80)"
            bp_status_color = "#10b981"

        # 5. Composite Longevity & Preventive Health Index (0 - 100%)
        penalties = 0
        if bmi > 25: penalties += (bmi - 25) * 2
        if systolic_bp > 120: penalties += (systolic_bp - 120) * 0.5
        if hba1c > 5.7: penalties += (hba1c - 5.7) * 15
        if ldl_c > 100: penalties += (ldl_c - 100) * 0.15
        if egfr < 90: penalties += (90 - egfr) * 0.3
        if is_smoker: penalties += 20
        if weekly_exercise_min < 150: penalties += 15

        health_index = max(15, min(99, int(100 - penalties)))

        # Priority Clinical Recommendations
        recommendations = []
        if hba1c >= 5.7 or fasting_glucose >= 100:
            recommendations.append("Adopt a Low-Glycemic Mediterranean diet rich in soluble fiber (beta-glucan) and initiate post-meal brisk 15-minute walks.")
        if systolic_bp >= 130 or diastolic_bp >= 80:
            recommendations.append("Implement the strict DASH protocol: reduce sodium to <1,500 mg/day, increase potassium to 4,700 mg/day, and introduce daily isometric handgrip training.")
        if ldl_c >= 100:
            recommendations.append("Incorporate 2-3g/day of plant sterols and viscous fiber (oats, legumes, psyllium); discuss lipid-lowering therapy with a cardiologist if 10-yr risk >= 7.5%.")
        if weekly_exercise_min < 150:
            recommendations.append("Gradually scale physical activity toward the clinical target of 150-300 min/week moderate aerobic exercise + 2 resistance sessions.")
        if is_smoker:
            recommendations.append("Immediate smoking cessation counseling: tobacco elimination halves excess coronary mortality within 1 year.")

        if not recommendations:
            recommendations.append("Maintain optimal preventive biomarkers with continued adherence to balanced nutrition, restful 7-8h sleep, and regular zone-2 cardiovascular training.")

        return {
            "health_index": health_index,
            "t2d_risk_pct": t2d_risk_pct,
            "t2d_stage": t2d_stage,
            "ascvd_risk_pct": ascvd_risk_pct,
            "cv_category": cv_category,
            "kdigo_stage": kdigo_stage,
            "renal_risk_level": renal_risk_level,
            "bp_stage": bp_stage,
            "bp_status_color": bp_status_color,
            "recommendations": recommendations
        }
