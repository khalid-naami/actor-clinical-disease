"""Clinical FITT Medical Exercise Prescription Engine.

Provides evidence-based Frequency, Intensity, Time, and Type (FITT) protocols,
heart rate zones, physiological mechanisms, and clinical safety contraindications.
"""

from typing import Dict, List, Any

EXERCISE_PROTOCOLS: Dict[str, Dict[str, Any]] = {
    "Type 2 Diabetes Mellitus": {
        "prescription_title": "Metabolic Optimization & GLUT4 Translocation Protocol",
        "target_weekly_volume": "150 - 300 minutes / week",
        "aerobic_fitt": {
            "frequency": "4 - 5 days / week (No more than 48h between sessions)",
            "intensity": "Moderate (50 - 70% VO2max or 60 - 75% Max Heart Rate / RPE 12-14)",
            "time": "30 - 45 minutes per session",
            "type": "Brisk walking, cycling, rowing, elliptical, or swimming"
        },
        "resistance_fitt": {
            "frequency": "2 - 3 non-consecutive days / week",
            "intensity": "Moderate-to-High (65 - 80% 1RM, 8 - 12 repetitions, 2 - 3 sets)",
            "time": "30 - 45 minutes targeting major muscle groups",
            "type": "Multi-joint compound movements (squats, leg press, chest press, rows)"
        },
        "physiological_mechanisms": [
            "Stimulates insulin-independent GLUT4 glucose transporter translocation via contraction-activated AMPK.",
            "Increases mitochondrial biogenesis, density, and oxidative phosphorylation capacity in skeletal myocytes.",
            "Decreases intramyocellular lipid accumulation and reduces hepatic steatosis.",
            "Induces beneficial myokine secretion (Irisin, IL-6), promoting adipose tissue browning."
        ],
        "safety_contraindications": [
            "Check pre-exercise blood glucose: if <100 mg/dL (on insulin/sulfonylureas), ingest 15-20g fast-acting carbs; if >250 mg/dL with ketones, delay exercise.",
            "Patients with active proliferative diabetic retinopathy must avoid heavy valsalva maneuvers or inverted postures.",
            "Inspect feet daily before and after exercise; wear non-friction specialized diabetic footwear."
        ]
    },

    "Cardiovascular & Coronary Artery Disease": {
        "prescription_title": "Cardiac Rehabilitation & Endothelial Shear Stress Protocol",
        "target_weekly_volume": "150 - 200 minutes / week (Monitored Phase II/III)",
        "aerobic_fitt": {
            "frequency": "5 - 7 days / week",
            "intensity": "Zone 2 Low-to-Moderate (50 - 65% HRR or 10-20 bpm below ischemic threshold)",
            "time": "30 - 60 minutes with 10-min warm-up and cool-down",
            "type": "Treadmill walking, stationary cycle ergometer, arm ergometer"
        },
        "resistance_fitt": {
            "frequency": "2 - 3 days / week",
            "intensity": "Low-to-Moderate (40 - 60% 1RM, 12 - 15 reps, 1 - 2 sets)",
            "time": "20 - 30 minutes",
            "type": "Elastic resistance bands, light dumbbells, bodyweight seated exercises"
        },
        "physiological_mechanisms": [
            "Laminar pulsatile shear stress upregulates endothelial nitric oxide synthase (eNOS), reversing endothelial dysfunction.",
            "Increases coronary collateral circulation and coronary flow reserve.",
            "Lowers resting sympathetic tone and elevates parasympathetic heart rate variability (HRV).",
            "Reduces myocardial oxygen demand at any given submaximal workload (rate-pressure product)."
        ],
        "safety_contraindications": [
            "Absolute contraindication during unstable angina, acute decompensated heart failure, or uncontrolled severe arrhythmias.",
            "Avoid sustained isometric straining / valsalva maneuvers that cause acute spikes in left ventricular afterload.",
            "Stop exercise immediately if patient experiences angina, dizziness, diaphoresis, or sudden dyspnea."
        ]
    },

    "Essential Hypertension": {
        "prescription_title": "Vascular Tone Reduction & Post-Exercise Hypotension Protocol",
        "target_weekly_volume": "150 - 250 minutes / week",
        "aerobic_fitt": {
            "frequency": "5 - 7 days / week (Daily preferred for sustained post-exercise hypotension)",
            "intensity": "Moderate (40 - 60% VO2 Reserve / RPE 11-13)",
            "time": "30 - 45 minutes continuous or intermittent (10-min bouts)",
            "type": "Outdoor walking, cycling, aqua aerobics, light jogging"
        },
        "resistance_fitt": {
            "frequency": "2 - 3 days / week + Isometric Handgrip Training",
            "intensity": "Moderate Dynamic (50 - 70% 1RM) + Isometric Handgrip (4x 2-min squeezes at 30% MVC)",
            "time": "30 minutes dynamic or 12 minutes isometric",
            "type": "Circuit training with low rest intervals and calibrated isometric handgrip dynamometer"
        },
        "physiological_mechanisms": [
            "Induces acute Post-Exercise Hypotension (PEH) lasting 12-24 hours with a 5-8 mmHg reduction.",
            "Decreases peripheral vascular resistance through systemic vasodilation and reduced sympathetic outflow.",
            "Improves arterial compliance and blunts excessive baroreceptor resetting.",
            "Downregulates renal tubular sodium reabsorption through atrial natriuretic peptide (ANP) release."
        ],
        "safety_contraindications": [
            "Do not start exercise if resting systolic BP > 180 mmHg or diastolic BP > 110 mmHg.",
            "Monitor for excessive hypertensive response during exercise (SBP > 220 mmHg or DBP > 105 mmHg is an indication to terminate).",
            "Avoid heavy overhead pressing and prolonged isometric breath-holding."
        ]
    },

    "Oncology & Common Solid Tumors": {
        "prescription_title": "Onco-Functional Preservation & Cachexia Attenuation Protocol",
        "target_weekly_volume": "150 minutes moderate aerobic + 2-3 resistance sessions / week",
        "aerobic_fitt": {
            "frequency": "3 - 5 days / week (Adjustable around chemotherapy cycles)",
            "intensity": "Low-to-Moderate (40 - 60% VO2max / RPE 10-12)",
            "time": "20 - 40 minutes (Can be divided into 10-min mini-sessions)",
            "type": "Recumbent cycling, walking on flat surfaces, light elliptical"
        },
        "resistance_fitt": {
            "frequency": "2 - 3 days / week",
            "intensity": "Moderate (50 - 70% 1RM, 8 - 12 reps, focus on preserving lean mass)",
            "time": "20 - 30 minutes",
            "type": "Machine-based guided resistance, resistance bands, functional core stability"
        },
        "physiological_mechanisms": [
            "Mobilizes and activates cytotoxic Natural Killer (NK) cells into the circulation via epinephrine surge.",
            "Improves intratumoral vascular perfusion, enhancing chemotherapy and immunotherapy drug delivery.",
            "Directly mitigates Cancer-Related Fatigue (CRF) through improved cellular bioenergetics.",
            "Counteracts muscle sarcopenia and osteopenia induced by hormone deprivation therapies."
        ],
        "safety_contraindications": [
            "Avoid public gyms or high-contact environments if absolute neutrophil count (ANC) < 1,000/μL (severe neutropenia).",
            "No high-impact loading or contact sports if bone metastases are present (fracture risk).",
            "Delay session if platelets < 50,000/μL or hemoglobin < 8.0 g/dL."
        ]
    },

    "Chronic Kidney Disease": {
        "prescription_title": "Renal Functional Maintenance & Sarcopenia Defense Protocol",
        "target_weekly_volume": "120 - 180 minutes / week",
        "aerobic_fitt": {
            "frequency": "3 - 5 days / week (Non-dialysis days or intra-dialytic initial 2 hours)",
            "intensity": "Low-to-Moderate (40 - 60% HRR / RPE 11-13)",
            "time": "20 - 35 minutes",
            "type": "Walking, stationary cycling, low-impact seated stepping"
        },
        "resistance_fitt": {
            "frequency": "2 - 3 days / week",
            "intensity": "Light-to-Moderate (40 - 60% 1RM, 10 - 15 repetitions)",
            "time": "20 minutes",
            "type": "Ankle weights, resistance bands, seated leg extensions and arm curls"
        },
        "physiological_mechanisms": [
            "Attenuates systemic inflammation and reduces circulating uremic toxins through sweat and improved dialysis efficiency.",
            "Preserves functional capacity, muscle protein synthesis, and prevents uremic sarcopenia.",
            "Improves blood pressure control, indirectly preserving remaining functional nephrons.",
            "Reduces cardiovascular risk, which is the primary cause of mortality in CKD patients."
        ],
        "safety_contraindications": [
            "Protect vascular access (arteriovenous fistula/graft): avoid direct pressure or heavy weights with the access limb.",
            "Avoid exercise during severe electrolyte imbalances (e.g. serum potassium > 5.5 mEq/L).",
            "Discontinue if experiencing lightheadedness, nausea, or significant interdialytic fluid shifts."
        ]
    },

    "COPD & Chronic Respiratory Diseases": {
        "prescription_title": "Pulmonary Rehabilitation & Ventilatory Efficiency Protocol",
        "target_weekly_volume": "120 - 150 minutes / week",
        "aerobic_fitt": {
            "frequency": "4 - 5 days / week",
            "intensity": "Interval Training (60 - 80% peak work rate intervals interspersed with low-intensity rest)",
            "time": "20 - 30 minutes (Intervals of 2-3 min work / 1-2 min active rest)",
            "type": "Treadmill walking with handrail support, stationary cycling, upper-body ergometry"
        },
        "resistance_fitt": {
            "frequency": "2 - 3 days / week",
            "intensity": "Moderate (50 - 70% 1RM, focus on respiratory and peripheral accessory muscles)",
            "time": "20 minutes",
            "type": "Chest fly, lat pulldown, quadriceps leg extensions + Pursed-Lip Breathing"
        },
        "physiological_mechanisms": [
            "Desensitizes patient to dyspnea sensations, reducing panic and hyperventilation cycles.",
            "Enhances peripheral muscle oxidative capacity, reducing lactic acid production and ventilatory demand at submaximal workloads.",
            "Improves diaphragm and accessory inspiratory muscle strength.",
            "Facilitates airway mucus clearance and reduces dynamic pulmonary hyperinflation."
        ],
        "safety_contraindications": [
            "Continuous pulse oximetry monitoring: keep SpO2 >= 88-90% (administer supplemental oxygen if indicated).",
            "Do not perform during acute bacterial/viral exacerbation until patient is clinically stabilized.",
            "Teach and enforce Pursed-Lip Breathing and Diaphragmatic breathing throughout exercise."
        ]
    },

    "Alzheimer's & Neurodegenerative Disorders": {
        "prescription_title": "Dual-Task Neuroplasticity & BDNF Upregulation Protocol",
        "target_weekly_volume": "150 - 200 minutes / week",
        "aerobic_fitt": {
            "frequency": "4 - 5 days / week",
            "intensity": "Moderate (50 - 65% VO2max / RPE 11-13)",
            "time": "30 - 45 minutes",
            "type": "Brisk walking in nature, tandem cycling, dancing, water aerobics"
        },
        "resistance_fitt": {
            "frequency": "2 - 3 days / week + Dual-Task Cognitive Challenges",
            "intensity": "Moderate (50 - 65% 1RM, balance, coordination, gait training)",
            "time": "25 - 35 minutes",
            "type": "Obstacle courses, Tai Chi, standing balance on foam pads, dual-task counting exercises"
        },
        "physiological_mechanisms": [
            "Directly stimulates synthesis and secretion of Brain-Derived Neurotrophic Factor (BDNF) in the hippocampus.",
            "Increases cerebral blood flow and enhances cortical vascularization via VEGF.",
            "Upregulates glymphatic cerebrospinal fluid clearance of amyloid-beta and hyperphosphorylated tau during subsequent sleep.",
            "Stimulates adult neurogenesis in the subgranular zone of the dentate gyrus."
        ],
        "safety_contraindications": [
            "High fall risk: ensure close physical supervision, clear uncluttered workout pathways, and stable footwear.",
            "Avoid overly complex mechanical equipment that may cause disorientation or emotional agitation.",
            "Perform sessions during optimal daylight hours when cognitive clarity is highest (avoid 'sundowning' periods)."
        ]
    }
}

class ExerciseEngine:
    """Manages clinical exercise prescriptions and therapeutic physical protocols."""

    @staticmethod
    def get_protocol(disease_name: str) -> Dict[str, Any]:
        return EXERCISE_PROTOCOLS.get(disease_name, EXERCISE_PROTOCOLS["Type 2 Diabetes Mellitus"])
