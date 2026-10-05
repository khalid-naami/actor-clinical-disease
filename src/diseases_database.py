"""Comprehensive Clinical Database for 7 Major Chronic Diseases.

Includes clinical definitions, epidemiology, target biomarkers, drug classes,
guidelines, and risk stratification metrics.
"""

from typing import Dict, List, Any

CHRONIC_DISEASES_DB: Dict[str, Dict[str, Any]] = {
    "Type 2 Diabetes Mellitus": {
        "id": "T2D",
        "icon": "🩸",
        "category": "Metabolic & Endocrine",
        "icd10": "E11",
        "prevalence_global": "537 Million Adults (10.5% global population)",
        "annual_mortality": "6.7 Million deaths annually",
        "guidelines": "ADA Standards of Care 2026 / EASD Consensus",
        "summary": "A chronic progressive metabolic disorder characterized by peripheral insulin resistance, inadequate compensatory insulin secretion, and chronic systemic hyperglycemia leading to micro- and macrovascular damage.",
        "pathophysiology": "Primary defects include hepatic overproduction of glucose, impaired insulin-stimulated glucose uptake in skeletal muscle and adipose tissue, and pancreatic beta-cell apoptosis driven by lipotoxicity, glucotoxicity, and chronic low-grade inflammation.",
        "primary_biomarkers": [
            {"name": "Hemoglobin A1c (HbA1c)", "unit": "%", "optimal": "< 5.7%", "pre_disease": "5.7 - 6.4%", "target_managed": "< 7.0%", "critical": "> 8.5%"},
            {"name": "Fasting Plasma Glucose (FPG)", "unit": "mg/dL", "optimal": "70 - 99", "pre_disease": "100 - 125", "target_managed": "80 - 130", "critical": "> 180"},
            {"name": "Postprandial Glucose (2h)", "unit": "mg/dL", "optimal": "< 140", "pre_disease": "140 - 199", "target_managed": "< 180", "critical": "> 250"},
            {"name": "Fasting Insulin / HOMA-IR", "unit": "Index", "optimal": "< 1.5", "pre_disease": "1.5 - 2.5", "target_managed": "< 2.0", "critical": "> 3.5"},
            {"name": "Urinary Albumin-to-Creatinine Ratio (uACR)", "unit": "mg/g", "optimal": "< 30", "pre_disease": "30 - 300", "target_managed": "< 30", "critical": "> 300"}
        ],
        "pharmacological_pillars": [
            {"class": "Biguanides (Metformin)", "mechanism": "Inhibits hepatic gluconeogenesis via AMPK activation; enhances peripheral insulin sensitivity."},
            {"class": "GLP-1 Receptor Agonists (Semaglutide, Tirzepatide)", "mechanism": "Glucose-dependent insulin release, suppresses glucagon, delays gastric emptying, central satiety signaling."},
            {"class": "SGLT2 Inhibitors (Empagliflozin, Dapagliflozin)", "mechanism": "Blocks renal proximal tubule glucose reabsorption; delivers profound cardiorenal protection and osmotic diuresis."},
            {"class": "DPP-4 Inhibitors (Sitagliptin)", "mechanism": "Extends endogenous incretin half-life by preventing enzymatic degradation."},
            {"class": "Basal/Bolus Insulins (Glargine, Degludec, Lispro)", "mechanism": "Exogenous hormone replacement to facilitate cellular glucose uptake during advanced beta-cell exhaustion."}
        ],
        "key_complications": [
            "Diabetic Retinopathy & Macular Edema",
            "Diabetic Nephropathy & End-Stage Renal Disease (ESRD)",
            "Peripheral Neuropathy & Diabetic Foot Ulceration",
            "Accelerated Atherosclerosis (Coronary Artery Disease & Stroke)"
        ],
        "risk_factors": {
            "modifiable": ["Visceral Adiposity (BMI > 25, Waist > 94cm/80cm)", "Sedentary Lifestyle", "Ultra-Processed Carbohydrate Intake", "Obstructive Sleep Apnea"],
            "non_modifiable": ["First-degree Family History", "South Asian / Hispanic / African Ancestry", "History of Gestational Diabetes", "Age >= 45"]
        }
    },

    "Cardiovascular & Coronary Artery Disease": {
        "id": "CAD",
        "icon": "🫀",
        "category": "Cardiovascular & Hemodynamic",
        "icd10": "I25.1",
        "prevalence_global": "620 Million Individuals (Leading global cause of death)",
        "annual_mortality": "19.8 Million deaths annually",
        "guidelines": "AHA/ACC Secondary Prevention 2026 / ESC Cardiovascular Guidelines",
        "summary": "Pathological narrowing or occlusion of coronary arteries caused by atheromatous plaque accumulation within the tunica intima, compromising myocardial oxygen delivery.",
        "pathophysiology": "Endothelial dysfunction triggered by elevated apoB lipoproteins, shear stress, and oxidative stress allows subendothelial LDL infiltration, foam cell formation, fibrous cap maturation, and potential plaque rupture inducing acute coronary thrombosis.",
        "primary_biomarkers": [
            {"name": "LDL-Cholesterol (LDL-C)", "unit": "mg/dL", "optimal": "< 70", "pre_disease": "70 - 100", "target_managed": "< 55 (Very High Risk)", "critical": "> 160"},
            {"name": "Apolipoprotein B (ApoB)", "unit": "mg/dL", "optimal": "< 65", "pre_disease": "65 - 80", "target_managed": "< 65", "critical": "> 110"},
            {"name": "High-Sensitivity CRP (hs-CRP)", "unit": "mg/L", "optimal": "< 1.0", "pre_disease": "1.0 - 3.0", "target_managed": "< 1.0", "critical": "> 5.0"},
            {"name": "Lipoprotein(a) [Lp(a)]", "unit": "nmol/L", "optimal": "< 30", "pre_disease": "30 - 75", "target_managed": "< 50", "critical": "> 125"},
            {"name": "High-Sensitivity Troponin I (hs-cTnI)", "unit": "ng/L", "optimal": "< 14", "pre_disease": "14 - 30", "target_managed": "< 14", "critical": "> 50 (Myocardial Injury)"}
        ],
        "pharmacological_pillars": [
            {"class": "HMG-CoA Reductase Inhibitors (Atorvastatin, Rosuvastatin)", "mechanism": "Upregulates hepatic LDL receptors; stabilizes coronary plaques; anti-inflammatory pleiotropic effects."},
            {"class": "PCSK9 Inhibitors / siRNA (Evolocumab, Inclisiran)", "mechanism": "Prevents LDL receptor degradation; dramatically lowers circulating apoB and Lp(a)."},
            {"class": "Dual Antiplatelet Therapy (Aspirin + Clopidogrel/Ticagrelor)", "mechanism": "Inhibits COX-1 and P2Y12 platelet activation, preventing arterial stent thrombosis."},
            {"class": "Beta-1 Selective Blockers (Bisoprolol, Metoprolol)", "mechanism": "Decreases myocardial oxygen demand, lowers resting heart rate, reduces post-MI mortality."},
            {"class": "ACE Inhibitors / ARBs (Ramipril, Telmisartan)", "mechanism": "Inhibits angiotensin II-mediated vasoconstriction, preserves left ventricular geometry."}
        ],
        "key_complications": [
            "Acute ST-Elevation Myocardial Infarction (STEMI)",
            "Ischemic Cardiomyopathy & Congestive Heart Failure",
            "Malignant Ventricular Arrhythmias (VT/VFib)",
            "Sudden Cardiac Death (SCD)"
        ],
        "risk_factors": {
            "modifiable": ["Elevated ApoB/LDL-C", "Hypertension", "Tobacco & E-Cigarette Smoking", "Visceral Obesity", "Chronic Systemic Inflammation"],
            "non_modifiable": ["Premature Family CAD (<55 male, <65 female)", "Elevated Genetic Lp(a)", "Male Biological Sex", "Advanced Age"]
        }
    },

    "Essential Hypertension": {
        "id": "HTN",
        "icon": "⚡",
        "category": "Cardiovascular & Vascular Dynamics",
        "icd10": "I10",
        "prevalence_global": "1.28 Billion Adults (1 in 3 adults worldwide)",
        "annual_mortality": "10.8 Million deaths linked to hypertensive sequelae",
        "guidelines": "ACC/AHA 2026 Hypertension Clinical Practice / ESH Guidelines",
        "summary": "Sustained elevation of systemic arterial blood pressure (Systolic >= 130 mmHg and/or Diastolic >= 80 mmHg) causing endothelial shear stress, vascular remodeling, and end-organ microvascular damage.",
        "pathophysiology": "Multifactorial etiology including inappropriate Renin-Angiotensin-Aldosterone System (RAAS) overactivation, increased sympathetic vasomotor tone, renal sodium retention, endothelial nitric oxide deficiency, and arterial wall stiffening.",
        "primary_biomarkers": [
            {"name": "Systolic Blood Pressure (SBP)", "unit": "mmHg", "optimal": "< 120", "pre_disease": "120 - 129", "target_managed": "< 130", "critical": ">= 180 (Hypertensive Crisis)"},
            {"name": "Diastolic Blood Pressure (DBP)", "unit": "mmHg", "optimal": "< 80", "pre_disease": "80 - 84", "target_managed": "< 80", "critical": ">= 120"},
            {"name": "Pulse Wave Velocity (PWV)", "unit": "m/s", "optimal": "< 7.0", "pre_disease": "7.0 - 9.9", "target_managed": "< 8.0", "critical": "> 10.0 (Severe Arterial Stiffening)"},
            {"name": "Serum Creatinine / eGFR", "unit": "mL/min/1.73m²", "optimal": "> 90", "pre_disease": "60 - 89", "target_managed": "> 60", "critical": "< 30 (Hypertensive Nephropathy)"},
            {"name": "Urine Microalbumin", "unit": "mg/24h", "optimal": "< 30", "pre_disease": "30 - 100", "target_managed": "< 30", "critical": "> 300"}
        ],
        "pharmacological_pillars": [
            {"class": "Angiotensin Receptor Blockers (Losartan, Valsartan)", "mechanism": "Blocks AT1 receptors, preventing vasoconstriction and aldosterone release without bradykinin cough."},
            {"class": "Dihydropyridine Calcium Channel Blockers (Amlodipine)", "mechanism": "Inhibits L-type voltage-gated calcium channels in vascular smooth muscle, reducing peripheral vascular resistance."},
            {"class": "Thiazide-like Diuretics (Chlorthalidone, Indapamide)", "mechanism": "Inhibits Na+/Cl- cotransporter in distal convoluted tubule; long-term vasodilation."},
            {"class": "Mineralocorticoid Receptor Antagonists (Spironolactone, Eplerenone)", "mechanism": "Blocks aldosterone-induced sodium retention; primary therapy for resistant hypertension."}
        ],
        "key_complications": [
            "Hemorrhagic & Ischemic Cerebrovascular Stroke",
            "Left Ventricular Hypertrophy (LVH) & Diastolic Heart Failure",
            "Hypertensive Nephrosclerosis & Renal Failure",
            "Hypertensive Retinopathy & Grade IV Papilledema"
        ],
        "risk_factors": {
            "modifiable": ["High Dietary Sodium (>2,300 mg/day)", "Inadequate Dietary Potassium (<3,500 mg/day)", "Chronic Alcohol Consumption", "Physical Inactivity", "Chronic Mental Stress & Sympathetic Dominance"],
            "non_modifiable": ["Black / African Heritage", "Genetic Polymorphisms in Renin-Angiotensin System", "Age-related Arterial Calcification"]
        }
    },

    "Oncology & Common Solid Tumors": {
        "id": "ONC",
        "icon": "🧬",
        "category": "Cellular Proliferation & Immunology",
        "icd10": "C00-C97",
        "prevalence_global": "50.5 Million (5-year prevalent cases globally)",
        "annual_mortality": "10.0 Million deaths annually",
        "guidelines": "NCCN Comprehensive Cancer Guidelines 2026 / ASCO / ESMO",
        "summary": "A complex collection of diseases characterized by unregulated cellular proliferation, evasion of apoptosis, genomic instability, sustained angiogenesis, and tissue invasion/metastasis.",
        "pathophysiology": "Somatic and germline genetic alterations in oncogenes (e.g., KRAS, EGFR, MYC) and tumor suppressor genes (e.g., TP53, PTEN, BRCA1/2) leading to metabolic reprogramming (Warburg effect) and immune checkpoint escape (PD-1/PD-L1, CTLA-4).",
        "primary_biomarkers": [
            {"name": "Circulating Tumor DNA (ctDNA) MRDs", "unit": "Molecules/mL", "optimal": "Undetectable", "pre_disease": "Low VAF (<0.1%)", "target_managed": "Clearance", "critical": "> 1.0% VAF (Relapse)"},
            {"name": "Carcinoembryonic Antigen (CEA)", "unit": "ng/mL", "optimal": "< 3.0", "pre_disease": "3.0 - 5.0", "target_managed": "< 3.0", "critical": "> 20.0 (Metastatic Burden)"},
            {"name": "Prostate-Specific Antigen (PSA)", "unit": "ng/mL", "optimal": "< 2.5", "pre_disease": "2.5 - 4.0", "target_managed": "< 0.2 (Post-Op)", "critical": "> 10.0"},
            {"name": "Cancer Antigen 125 (CA-125)", "unit": "U/mL", "optimal": "< 35", "pre_disease": "35 - 50", "target_managed": "< 35", "critical": "> 150"},
            {"name": "Neutrophil-to-Lymphocyte Ratio (NLR)", "unit": "Ratio", "optimal": "< 2.0", "pre_disease": "2.0 - 3.5", "target_managed": "< 2.5", "critical": "> 5.0 (High Systemic Inflammation)"}
        ],
        "pharmacological_pillars": [
            {"class": "Immune Checkpoint Inhibitors (Pembrolizumab, Nivolumab)", "mechanism": "Blocks PD-1/PD-L1 axis, rejuvenating cytotoxic T-lymphocytes to recognize and lyse tumor cells."},
            {"class": "Targeted Tyrosine Kinase Inhibitors (Osimertinib, Sotorasib)", "mechanism": "Selectively inhibits oncogenic driver mutations (EGFR T790M, KRAS G12C) blocking downstream MAP-kinase cascade."},
            {"class": "Antibody-Drug Conjugates - ADCs (Trastuzumab Deruxtecan)", "mechanism": "Delivers potent topoisomerase payloads directly to HER2+ tumor cells with bystander effect."},
            {"class": "Platinum & Taxane Cytotoxic Chemotherapy", "mechanism": "Crosslinks DNA strands and arrests mitotic spindle dynamics in rapidly dividing cells."}
        ],
        "key_complications": [
            "Cancer Cachexia & Sarcopenic Muscle Wasting",
            "Distant Organ Metastasis (Bone, Liver, Brain, Lungs)",
            "Treatment-Induced Cardiotoxicity & Neuropathy",
            "Tumor Lysis Syndrome & Severe Febrile Neutropenia"
        ],
        "risk_factors": {
            "modifiable": ["Tobacco & Second-hand Smoke Exposure", "Chronic Alcohol Abuse", "Obesity & Visceral Adiposity", "Processed Meats / Carcinogenic Nitrosamines", "Occupational Asbestos/Chemical Exposure"],
            "non_modifiable": ["Germline Mutations (BRCA1/2, Lynch Syndrome MSH2/MLH1)", "Chronic Oncogenic Viruses (HPV, HBV, HCV, EBV)", "Advanced Age"]
        }
    },

    "Chronic Kidney Disease": {
        "id": "CKD",
        "icon": "🧪",
        "category": "Renal & Electrolyte Homeostasis",
        "icd10": "N18",
        "prevalence_global": "850 Million People (10% - 15% of global population)",
        "annual_mortality": "3.1 Million deaths annually (Projected 5th leading cause by 2040)",
        "guidelines": "KDIGO Clinical Practice Guideline 2026 / KDOQI Guidelines",
        "summary": "Persistent structural or functional abnormalities of the kidneys, present for >3 months, manifested by reduced glomerular filtration rate (eGFR < 60 mL/min/1.73m²) or persistent albuminuria.",
        "pathophysiology": "Glomerular hyperfiltration injury, podocyte effacement, tubulointerstitial inflammation, and progressive interstitial fibrosis leading to loss of nephron units, uremic toxin retention, and impaired erythropoietin/vitamin D synthesis.",
        "primary_biomarkers": [
            {"name": "Estimated Glomerular Filtration Rate (eGFR)", "unit": "mL/min/1.73m²", "optimal": "> 90", "pre_disease": "60 - 89 (G2)", "target_managed": "> 45 (Stabilized)", "critical": "< 15 (G5 - Kidney Failure)"},
            {"name": "Serum Creatinine", "unit": "mg/dL", "optimal": "0.7 - 1.2", "pre_disease": "1.3 - 1.8", "target_managed": "< 1.5", "critical": "> 3.5"},
            {"name": "Urine Albumin-to-Creatinine Ratio (uACR)", "unit": "mg/g", "optimal": "< 30 (A1)", "pre_disease": "30 - 300 (A2 Micro)", "target_managed": "< 30", "critical": "> 300 (A3 Macroalbuminuria)"},
            {"name": "Serum Potassium (K+)", "unit": "mEq/L", "optimal": "3.8 - 4.8", "pre_disease": "4.9 - 5.2", "target_managed": "4.0 - 5.0", "critical": "> 5.8 (Hyperkalemia / Arrhythmia)"},
            {"name": "Intact Parathyroid Hormone (iPTH)", "unit": "pg/mL", "optimal": "15 - 65", "pre_disease": "65 - 120", "target_managed": "2x - 9x baseline", "critical": "> 300 (Renal Osteodystrophy)"}
        ],
        "pharmacological_pillars": [
            {"class": "SGLT2 Inhibitors (Dapagliflozin, Empagliflozin)", "mechanism": "Reduces intraglomerular hypertension via tubuloglomerular feedback; slows eGFR annual slope decline by >40%."},
            {"class": "Non-steroidal Mineralocorticoid Receptor Antagonists (Finerenone)", "mechanism": "Blocks aldosterone-driven renal fibrosis and inflammation without severe hyperkalemia."},
            {"class": "Renin-Angiotensin System Blockers (ACEi / ARB)", "mechanism": "Decreases efferent arteriolar resistance, reducing intraglomerular capillary pressure and proteinuria."},
            {"class": "HIF-PH Inhibitors (Roxadustat, Vadadustat)", "mechanism": "Stimulates endogenous erythropoietin production to treat renal anemia."}
        ],
        "key_complications": [
            "Accelerated Cardiovascular Calcification & Uremic Pericarditis",
            "Severe Hyperkalemia-Induced Cardiac Arrest",
            "Renal Anemia & Refractory Fluid Overload",
            "Chronic Kidney Disease-Mineral and Bone Disorder (CKD-MBD)"
        ],
        "risk_factors": {
            "modifiable": ["Poorly Controlled Diabetes", "Uncontrolled Hypertension", "Chronic NSAID / Nephrotoxic Drug Use", "High Dietary Phosphorus / Ultra-Processed Foods"],
            "non_modifiable": ["Polycystic Kidney Disease (PKD1/2)", "Glomerulonephritis (IgA Nephropathy)", "Family History of Renal Failure"]
        }
    },

    "COPD & Chronic Respiratory Diseases": {
        "id": "COPD",
        "icon": "🫁",
        "category": "Pulmonary & Gas Exchange Dynamics",
        "icd10": "J44",
        "prevalence_global": "392 Million Individuals (3rd leading cause of death worldwide)",
        "annual_mortality": "3.23 Million deaths annually",
        "guidelines": "GOLD Strategy Report 2026 / ATS / ERS Guidelines",
        "summary": "A progressive, life-threatening lung disease characterized by chronic airflow limitation, alveolar destruction (emphysema), and airway inflammation (chronic bronchitis) resulting from toxic particulate inhalation.",
        "pathophysiology": "Chronic inhalation of noxious gases recruits neutrophils and CD8+ T-cells, triggering matrix metalloproteinase-mediated destruction of elastin fibers, loss of elastic recoil, small airway fibrosis, and dynamic hyperinflation (air trapping).",
        "primary_biomarkers": [
            {"name": "FEV1 / FVC Ratio (Post-Bronchodilator)", "unit": "Ratio", "optimal": "> 0.75", "pre_disease": "0.70 - 0.75", "target_managed": "Stable >0.70", "critical": "< 0.70 (Fixed Airway Obstruction)"},
            {"name": "FEV1 % Predicted", "unit": "%", "optimal": "> 80% (GOLD 1)", "pre_disease": "50 - 79% (GOLD 2)", "target_managed": "> 50%", "critical": "< 30% (GOLD 4 Very Severe)"},
            {"name": "Resting Pulse Oximetry (SpO2)", "unit": "%", "optimal": "96 - 99%", "pre_disease": "92 - 95%", "target_managed": "88 - 92% (COPD Target)", "critical": "< 85% (Respiratory Failure)"},
            {"name": "Blood Eosinophil Count", "unit": "cells/μL", "optimal": "< 100", "pre_disease": "100 - 300", "target_managed": "< 150", "critical": "> 300 (Steroid/Biologic Responsive)"},
            {"name": "Arterial Blood Gas PaCO2", "unit": "mmHg", "optimal": "35 - 45", "pre_disease": "46 - 50", "target_managed": "< 48", "critical": "> 55 (Hypercapnic Respiratory Failure)"}
        ],
        "pharmacological_pillars": [
            {"class": "Dual Bronchodilators: LAMA + LABA (Tiotropium / Olodaterol)", "mechanism": "Synergistic M3-muscarinic receptor blockade and beta-2 adrenergic receptor agonism to maximize bronchodilation."},
            {"class": "Inhaled Corticosteroids - ICS (Fluticasone, Budesonide)", "mechanism": "Suppresses airway eosinophilic inflammation and reduces annual exacerbation frequency."},
            {"class": "Biologics: Anti-IL-4Rα / Anti-IL-5 (Dupilumab, Mepolizumab)", "mechanism": "Targeted inhibition of Type 2 airway inflammation pathways for exacerbation-prone COPD."},
            {"class": "Phosphodiesterase-4 Inhibitors (Roflumilast)", "mechanism": "Reduces cyclic AMP degradation in inflammatory cells, preventing chronic bronchitis flares."}
        ],
        "key_complications": [
            "Acute Exacerbations Requiring Mechanical Ventilation",
            "Cor Pulmonale & Right Ventricular Heart Failure",
            "Severe Secondary Pulmonary Hypertension",
            "Spontaneous Pneumothorax & Hypercapnic Coma"
        ],
        "risk_factors": {
            "modifiable": ["Tobacco Smoking & Hookah Inhalation", "Biomass Fuel Smoke & Indoor Cooking Emissions", "Occupational Dust & Silica Exposure", "Severe Urban Ambient Air Pollution (PM2.5)"],
            "non_modifiable": ["Alpha-1 Antitrypsin Deficiency (SERPINA1)", "Severe Childhood Respiratory Infections", "Impaired In-Utero Lung Development"]
        }
    },

    "Alzheimer's & Neurodegenerative Disorders": {
        "id": "AD",
        "icon": "🧠",
        "category": "Neurocognitive & Synaptic Function",
        "icd10": "G30",
        "prevalence_global": "55 Million People with Dementia (Projected 139M by 2050)",
        "annual_mortality": "1.9 Million direct deaths annually",
        "guidelines": "NIA-AA Diagnostic Guidelines 2026 / Lancet Commission on Dementia",
        "summary": "A progressive irreversible neurodegenerative brain disorder characterized by cognitive impairment, memory degradation, and loss of executive function resulting from cortical synaptic and neuronal loss.",
        "pathophysiology": "Extracellular aggregation of amyloid-beta (Aβ42) senile plaques and intracellular hyperphosphorylated tau neurofibrillary tangles (NFTs) trigger neuroinflammation (microglial activation), mitochondrial dysfunction, and cholinergic synaptic degradation.",
        "primary_biomarkers": [
            {"name": "Plasma Phosphorylated Tau 217 (p-tau217)", "unit": "pg/mL", "optimal": "< 0.20", "pre_disease": "0.20 - 0.40", "target_managed": "< 0.30", "critical": "> 0.50 (High Amyloid/Tau Pathology)"},
            {"name": "Montreal Cognitive Assessment (MoCA)", "unit": "Score / 30", "optimal": "26 - 30", "pre_disease": "22 - 25 (MCI)", "target_managed": "Stable >=20", "critical": "< 14 (Severe Dementia)"},
            {"name": "Mini-Mental State Exam (MMSE)", "unit": "Score / 30", "optimal": "27 - 30", "pre_disease": "21 - 26", "target_managed": "Stable >=20", "critical": "< 10"},
            {"name": "CSF / Plasma Aβ42 / Aβ40 Ratio", "unit": "Ratio", "optimal": "> 0.10", "pre_disease": "0.07 - 0.09", "target_managed": "> 0.08", "critical": "< 0.06 (Heavy Amyloid Deposition)"},
            {"name": "Serum Neurofilament Light Chain (NfL)", "unit": "pg/mL", "optimal": "< 15", "pre_disease": "15 - 25", "target_managed": "< 20", "critical": "> 40 (Active Neuroaxonal Damage)"}
        ],
        "pharmacological_pillars": [
            {"class": "Amyloid-Targeting Monoclonal Antibodies (Lecanemab, Donanemab)", "mechanism": "Selectively binds soluble amyloid protofibrils and fibrillar plaques, clearing cortical burden and slowing clinical decline."},
            {"class": "Cholinesterase Inhibitors (Donepezil, Rivastigmine, Galantamine)", "mechanism": "Inhibits acetylcholinesterase, elevating synaptic acetylcholine availability to enhance cholinergic neurotransmission."},
            {"class": "NMDA Receptor Antagonists (Memantine)", "mechanism": "Uncompetitive NMDA receptor antagonist, preventing glutamate-mediated excitotoxicity and calcium overload."},
            {"class": "Dual Orexin Receptor Antagonists (Suvorexant, Lemborexant)", "mechanism": "Optimizes glymphatic deep-sleep clearance of neurotoxic proteins."}
        ],
        "key_complications": [
            "Severe Loss of Activities of Daily Living (ADLs)",
            "Aspiration Pneumonia & Swallowing Apraxia",
            "Neuropsychiatric Agitation, Delusions, & Sleep Cycle Reversal",
            "Total Immobility & Severe Sarcopenic Frailty"
        ],
        "risk_factors": {
            "modifiable": ["Midlife Untreated Hypertension", "Type 2 Diabetes / Brain Insulin Resistance", "Untreated Midlife Hearing Loss", "Social Isolation & Low Cognitive Reserve", "Physical Inactivity & Chronic Sedentary State"],
            "non_modifiable": ["Apolipoprotein E4 Allele (APOE ε4 Carrier)", "Familial Early-Onset Mutations (APP, PSEN1, PSEN2)", "Female Sex & Advanced Age (>=65)"]
        }
    }
}

class ChronicDiseasesManager:
    """Helper manager for chronic disease queries and metadata."""

    @staticmethod
    def get_all_disease_names() -> List[str]:
        return list(CHRONIC_DISEASES_DB.keys())

    @staticmethod
    def get_disease(name: str) -> Dict[str, Any]:
        return CHRONIC_DISEASES_DB.get(name, CHRONIC_DISEASES_DB["Type 2 Diabetes Mellitus"])
