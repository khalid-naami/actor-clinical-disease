"""Evidence-Based Medical Nutrition & Clinical Dietetics Engine.

Provides therapeutic dietary blueprints, macronutrient breakdowns, micronutrient guardrails,
therapeutic superfoods, and strictly contraindicated items for 7 chronic diseases.
"""

from typing import Dict, List, Any

DIET_PROTOCOLS: Dict[str, Dict[str, Any]] = {
    "Type 2 Diabetes Mellitus": {
        "diet_name": "Low-Glycemic Mediterranean-Ketogenic Hybrid (L-Med)",
        "scientific_rationale": "Minimizes postprandial glucose excursions, attenuates hyperinsulinemia, increases GLP-1 secretion via viscous soluble fiber, and improves hepatic insulin sensitivity.",
        "macros": {
            "Carbohydrates": 25,
            "Proteins": 25,
            "Healthy Fats": 50,
            "Daily Fiber": "40 - 50g (High Soluble Beta-Glucan)"
        },
        "micronutrient_targets": {
            "Sodium": "< 2,000 mg/day",
            "Potassium": "3,500 - 4,700 mg/day",
            "Magnesium": "400 - 500 mg/day (Enhances GLUT4 translocation)",
            "Chromium": "200 - 400 mcg/day"
        },
        "therapeutic_superfoods": [
            {"food": "Extra Virgin Olive Oil (Polyphenol-Rich)", "mechanism": "Oleocanthal and oleuropein reduce nuclear factor-kappa B (NF-κB) inflammatory signaling."},
            {"food": "Wild-Caught Salmon & Mackerel", "mechanism": "EPA/DHA omega-3 fatty acids activate PPAR-gamma, improving adipocyte insulin signaling."},
            {"food": "Legumes & Lentils (High Resistant Starch)", "mechanism": "Promotes short-chain fatty acid (butyrate) production by colonic microbiome, stimulating incretins."},
            {"food": "Apple Cider Vinegar (Acetic Acid)", "mechanism": "Inhibits disaccharidase activity and enhances muscle glucose uptake during carbohydrate digestion."},
            {"food": "Cinnamon Extract (Ceylon)", "mechanism": "Mimics insulin by phosphorylation of the insulin receptor subunit."}
        ],
        "strictly_prohibited_foods": [
            {"food": "High-Fructose Corn Syrup & Sugar-Sweetened Beverages", "hazard": "Induces rapid hepatic de novo lipogenesis, liver steatosis, and profound insulin resistance."},
            {"food": "Refined Grain Carbohydrates (White bread, instant rice)", "hazard": "Triggers dangerous postprandial glycemic spikes above 200 mg/dL."},
            {"food": "Industrial Trans Fats & Fried Fast Foods", "hazard": "Disrupts endothelial membrane fluidity and elevates cardiovascular mortality."},
            {"food": "Ultra-Processed Snack Bars with Maltodextrin", "hazard": "Higher glycemic index (110) than pure glucose (100)."}
        ],
        "sample_meal_plan": {
            "breakfast": "Omelette with baby spinach, wild mushrooms, and avocado cooked in extra virgin olive oil + unsweetened green tea.",
            "lunch": "Mediterranean wild salmon bowl with mixed leafy greens, cucumbers, pumpkin seeds, walnuts, and lemon-tahini dressing.",
            "dinner": "Grilled pasture-raised chicken breast with roasted broccoli, cauliflower mash, and garlic sautéed asparagus.",
            "snacks": "A handful of raw walnuts + 1 cup organic blueberries or Greek yogurt (unsweetened 10% fat)."
        }
    },

    "Cardiovascular & Coronary Artery Disease": {
        "diet_name": "Cardioprotective Portfolio & Mediterranean Diet",
        "scientific_rationale": "Lowers atherogenic apolipoprotein B (apoB) particles, reduces LDL-C oxidation, enhances endothelial nitric oxide synthase (eNOS) activity, and lowers plaque inflammation.",
        "macros": {
            "Carbohydrates": 40,
            "Proteins": 20,
            "Healthy Fats": 40,
            "Daily Fiber": "45g+ (Viscous Plant Sterols & Pectin)"
        },
        "micronutrient_targets": {
            "Sodium": "< 1,500 mg/day",
            "Potassium": "4,000 - 4,700 mg/day",
            "Coenzyme Q10": "100 - 200 mg/day (Crucial for patients on statins)",
            "Omega-3 Index Target": "> 8.0%"
        },
        "therapeutic_superfoods": [
            {"food": "Oat Beta-Glucan & Barley", "mechanism": "Binds intestinal bile acids, forcing the liver to clear circulating LDL to synthesize fresh bile."},
            {"food": "Raw Walnuts & Almonds (Plant Sterols)", "mechanism": "Displaces dietary and biliary cholesterol absorption in the micellar phase."},
            {"food": "Dark Leafy Greens & Nitrate Beetroot", "mechanism": "Supplies dietary inorganic nitrates, converted to nitric oxide to promote coronary vasodilation."},
            {"food": "Wild Blueberries & Pomegranate", "mechanism": "Anthocyanins inhibit LDL oxidation and prevent vascular cell adhesion molecule-1 (VCAM-1) expression."},
            {"food": "Aged Garlic Extract", "mechanism": "Reduces low-attenuation (soft vulnerable) coronary plaque volume."}
        ],
        "strictly_prohibited_foods": [
            {"food": "Processed Deli Meats (Salami, Sausages, Bacon)", "hazard": "High sodium, nitrites, and trimethylamine N-oxide (TMAO) precursors accelerate atherogenesis."},
            {"food": "Industrial Hydrogenated Vegetable Oils", "hazard": "Elevates small dense LDL (sdLDL) and lowers cardioprotective HDL."},
            {"food": "High-Sugar Bakery Pastries & Donuts", "hazard": "Drives visceral adiposity and advanced glycation end-products (AGEs)."},
            {"food": "Excessive Salted Canned Soups & Snacks", "hazard": "Induces volume expansion, increasing myocardial wall stress."}
        ],
        "sample_meal_plan": {
            "breakfast": "Steel-cut oats with chia seeds, raw walnuts, Ceylon cinnamon, and organic blackberries.",
            "lunch": "Large Niçoise-style salad with wild sardines, olive oil, capers, steamed green beans, and hard-boiled pasture-raised egg.",
            "dinner": "Baked Mediterranean sea bass with ratatouille (zucchini, bell peppers, tomatoes, garlic) and a side of quinoa.",
            "snacks": "Celery sticks with natural almond butter + roasted unsalted edamame."
        }
    },

    "Essential Hypertension": {
        "diet_name": "Clinical DASH Diet Protocol (Dietary Approaches to Stop Hypertension)",
        "scientific_rationale": "Maximizes the dietary Potassium-to-Sodium ratio (>3:1), enhances renal natriuresis, reduces sympathetic vascular tone, and lowers systolic arterial pressure by 8-14 mmHg.",
        "macros": {
            "Carbohydrates": 50,
            "Proteins": 20,
            "Healthy Fats": 30,
            "Daily Fiber": "35 - 40g"
        },
        "micronutrient_targets": {
            "Sodium": "< 1,200 - 1,500 mg/day (Strict Upper Limit)",
            "Potassium": "4,700 mg/day (Vital for natriuresis)",
            "Calcium": "1,200 mg/day (Regulates vascular smooth muscle tone)",
            "Magnesium": "500 mg/day (Natural calcium channel blocker)"
        },
        "therapeutic_superfoods": [
            {"food": "Fermented Beetroot & Beet Juice", "mechanism": "Potent dietary nitrate donor; achieves acute systolic reduction within 3 hours."},
            {"food": "Avocados & Bananas", "mechanism": "High potassium promotes urinary sodium excretion and arterial relaxation."},
            {"food": "Unsalted Pumpkin & Sunflower Seeds", "mechanism": "Rich source of bioavailable magnesium and arginine for endothelial health."},
            {"food": "Hibiscus Sabdariffa Herbal Tea", "mechanism": "Natural ACE-inhibitory bioflavonoids comparable to low-dose captopril in clinical trials."},
            {"food": "Plain Organic Kefir / Greek Yogurt", "mechanism": "Supplies bio-peptides that inhibit angiotensin-converting enzyme."}
        ],
        "strictly_prohibited_foods": [
            {"food": "Monosodium Glutamate (MSG) & Soy Sauce", "hazard": "Massive sodium load triggering acute fluid retention and pressure spikes."},
            {"food": "Commercial Pizza & Salted Cheeses", "hazard": "High sodium density and saturated fat combination."},
            {"food": "Pickled Vegetables & Brined Olives", "hazard": "Extreme sodium chloride concentration."},
            {"food": "Energy Drinks with High Caffeine & Taurine", "hazard": "Excessive sympathomimetic beta-adrenergic stimulation."}
        ],
        "sample_meal_plan": {
            "breakfast": "Greek yogurt parfait with crushed pistachios, kiwi slices, ground flaxseeds, and a cup of Hibiscus tea.",
            "lunch": "Grilled turkey breast wrap in sprouted grain tortilla with spinach, avocado, grated carrots, and low-sodium hummus.",
            "dinner": "Roasted salmon fillet seasoned with turmeric, rosemary, and lemon served over steamed broccoli and sweet potato.",
            "snacks": "Fresh apple slices with unsalted peanut butter + fresh cucumber slices with lime."
        }
    },

    "Oncology & Common Solid Tumors": {
        "diet_name": "Metabolically Targeted Anti-Inflammatory Oncological Diet",
        "scientific_rationale": "Mitigates tumor-driven systemic inflammation, combats cancer cachexia through adequate high-biological-value protein, and inhibits the PI3K/Akt/mTOR metabolic pathway.",
        "macros": {
            "Carbohydrates": 30,
            "Proteins": 30,
            "Healthy Fats": 40,
            "Daily Fiber": "35g (Supports microbiome during chemo/immunotherapy)"
        },
        "micronutrient_targets": {
            "Vitamin D3": "4,000 - 5,000 IU/day (Target blood 25(OH)D: 50-70 ng/mL)",
            "Selenium": "150 - 200 mcg/day (Glutathione peroxidase cofactor)",
            "Zinc": "25 - 30 mg/day (Cellular repair & immune competence)",
            "Curcumin (with Piperine)": "1,000 mg/day (NF-κB inhibition)"
        },
        "therapeutic_superfoods": [
            {"food": "Cruciferous Sprouts (Sulforaphane)", "mechanism": "Potent Nrf2 activator; upregulates Phase II detoxification enzymes and promotes cancer cell apoptosis."},
            {"food": "Organic Green Tea (EGCG)", "mechanism": "Epigallocatechin gallate inhibits vascular endothelial growth factor (VEGF) and tumor angiogenesis."},
            {"food": "Medicinal Mushrooms (Reishi, Turkey Tail, Maitake)", "mechanism": "Beta-glucans stimulate natural killer (NK) cells and cytotoxic CD8+ lymphocytes."},
            {"food": "Turmeric Root Extract (Curcumin)", "mechanism": "Downregulates cyclooxygenase-2 (COX-2) and matrix metalloproteinases (MMPs)."},
            {"food": "Fermented Kimchi & Sauerkraut", "mechanism": "Enhances gut microbiome biodiversity (Akkermansia muciniphila), boosting anti-PD-1 immunotherapy response."}
        ],
        "strictly_prohibited_foods": [
            {"food": "Charred / Flame-Grilled Meats (Heterocyclic Amines)", "hazard": "High concentrations of carcinogenic polycyclic aromatic hydrocarbons (PAHs)."},
            {"food": "Refined Cane Sugar & High-Glycemic Pastries", "hazard": "Excessive insulin and IGF-1 signaling accelerates tumor cell division (Warburg effect)."},
            {"food": "Alcohol & Ethanol Products", "hazard": "Group 1 human carcinogen; acetaldehyde causes direct DNA double-strand breaks."},
            {"food": "Processed Meats with Nitrates/Nitrites", "hazard": "Forms DNA-alkylating nitrosamines in gastric acid."}
        ],
        "sample_meal_plan": {
            "breakfast": "Anti-inflammatory smoothie: organic broccoli sprouts, wild blueberries, ginger root, hemp protein, and matcha green tea.",
            "lunch": "Poached pasture-raised eggs over warm quinoa, steamed kale, turmeric roasted chickpeas, and avocado.",
            "dinner": "Wild-caught cod fillet with shiitake and maitake mushroom sauté, steamed bok choy, and ginger-garlic dressing.",
            "snacks": "Bone broth with fresh grated turmeric and black pepper + handful of Brazil nuts (Selenium)."
        }
    },

    "Chronic Kidney Disease": {
        "diet_name": "Renal Protective Plant-Dominant Protocol (PLADO)",
        "scientific_rationale": "Reduces glomerular hyperfiltration and intraglomerular pressure, minimizes nitrogenous uremic toxin generation, and prevents hyperphosphatemia and metabolic acidosis.",
        "macros": {
            "Carbohydrates": 55,
            "Proteins": "12 - 15% (0.6 - 0.8g/kg/day controlled protein)",
            "Healthy Fats": 30,
            "Daily Fiber": "30 - 35g"
        },
        "micronutrient_targets": {
            "Sodium": "< 1,500 - 2,000 mg/day",
            "Phosphorus": "< 800 - 1,000 mg/day (Avoid inorganic phosphate additives)",
            "Potassium": "Individualized (2,000 - 3,000 mg/day based on serum K+)",
            "Protein Intake": "0.6g/kg/day (Non-dialysis CKD Stage 3-5)"
        },
        "therapeutic_superfoods": [
            {"food": "Plant-Based Proteins (Tofu, Tempeh, Legumes)", "mechanism": "Causes less glomerular hyperfiltration than animal protein and generates fewer uremic toxins (IS, pCS)."},
            {"food": "Cauliflower & Cabbage (Low Potassium/Low Phosphorus)", "mechanism": "Provides vital glucosinolates while keeping electrolyte levels in strict safety ranges."},
            {"food": "Red Bell Peppers & Garlic", "mechanism": "Rich in antioxidants with exceptionally low potassium and phosphorus burden."},
            {"food": "Extra Virgin Olive Oil & Flaxseed Oil", "mechanism": "Calorie-dense healthy lipids that preserve body weight without generating renal waste products."},
            {"food": "Cranberries & Blueberries", "mechanism": "Protects against recurrent urinary tract infections without overwhelming potassium limits."}
        ],
        "strictly_prohibited_foods": [
            {"food": "Ultra-Processed Foods with Inorganic Phosphate Additives", "hazard": "100% bioavailable phosphate induces vascular calcification and rapid CKD progression."},
            {"food": "High-Sodium Canned & Cured Foods", "hazard": "Severe fluid retention, refractory hypertension, and peripheral edema."},
            {"food": "Star Fruit (Carambola)", "hazard": "Contains neurotoxin 'caramboxin' that cannot be cleared by failing kidneys, causing fatal neurotoxicity."},
            {"food": "Excessive Dark Colas & Processed Cheeses", "hazard": "Dense inorganic phosphate additives with near-total intestinal absorption."}
        ],
        "sample_meal_plan": {
            "breakfast": "Cream of wheat / oatmeal with almond milk, fresh blueberries, and crushed macadamia nuts.",
            "lunch": "Stir-fried firm tofu with zucchini, cabbage, red bell peppers, garlic, and white Jasmine rice.",
            "dinner": "Pasta tossed with extra virgin olive oil, fresh basil, sautéed garlic, roasted eggplant, and a small side of grilled chicken.",
            "snacks": "Fresh apple or pear slices + unsalted rice crackers."
        }
    },

    "COPD & Chronic Respiratory Diseases": {
        "diet_name": "High-Healthy-Fat Low-Respiratory-Quotient (RQ) Diet",
        "scientific_rationale": "Metabolizing fat produces significantly less Carbon Dioxide ($CO_2$) per mole of Oxygen consumed ($RQ = 0.70$ for fats vs $1.00$ for carbs), reducing respiratory workload and dyspnea.",
        "macros": {
            "Carbohydrates": 35,
            "Proteins": 25,
            "Healthy Fats": 40,
            "Daily Fiber": "30g"
        },
        "micronutrient_targets": {
            "Vitamin C": "250 - 500 mg/day (Combats airway oxidative stress)",
            "Vitamin D3": "2,000 - 4,000 IU/day (Reduces annual COPD exacerbations)",
            "Magnesium": "400 mg/day (Natural bronchodilator via smooth muscle relaxation)",
            "Omega-3 EPA/DHA": "2,000 mg/day"
        },
        "therapeutic_superfoods": [
            {"food": "Avocados & Extra Virgin Olive Oil", "mechanism": "Supplies low-RQ clean energy without taxing the ventilatory reserve."},
            {"food": "Fatty Fish (Salmon, Sardines, Trout)", "mechanism": "Resolvins and protectins from omega-3 downregulate airway neutrophilic inflammation."},
            {"food": "Leafy Greens & Broccoli", "mechanism": "Rich in magnesium and antioxidants to support diaphragm muscle endurance."},
            {"food": "Citrus Fruits & Bell Peppers (Vitamin C)", "mechanism": "Scavenges reactive oxygen species generated by inhaled particulate matter."},
            {"food": "Raw Pumpkin Seeds (Magnesium & Zinc)", "mechanism": "Maintains respiratory muscle strength and prevents sarcopenia."}
        ],
        "strictly_prohibited_foods": [
            {"food": "Large High-Carbohydrate Meals", "hazard": "High $CO_2$ generation leads to severe shortness of breath and respiratory fatigue."},
            {"food": "Gas-Forming Foods (Carbonated drinks, heavy beans)", "hazard": "Abdominal distension pushes up against the diaphragm, restricting lung expansion."},
            {"food": "Sulfited Dried Fruits & Wine", "hazard": "Sulfites can trigger acute bronchospasm in sensitive airway patients."},
            {"food": "Excessive Dairy for Heavy Mucus Patients", "hazard": "Thickens oral secretions and impairs mucociliary clearance."}
        ],
        "sample_meal_plan": {
            "breakfast": "Scrambled pasture-raised eggs in olive oil with avocado slices, smoked salmon, and fresh papaya.",
            "lunch": "Chicken salad with olive oil mayonnaise, walnuts, celery, and spinach greens.",
            "dinner": "Baked trout with roasted asparagus, zucchini, and mashed cauliflower with grass-fed butter.",
            "snacks": "Handful of macadamia nuts + chia seed pudding in coconut milk."
        }
    },

    "Alzheimer's & Neurodegenerative Disorders": {
        "diet_name": "MIND Diet Protocol (Mediterranean-DASH Intervention for Neurodegenerative Delay)",
        "scientific_rationale": "Rich in polyphenolic flavonoids, lutein, folate, and docosahexaenoic acid (DHA); shown in Rush University clinical trials to slow cognitive brain aging by 7.5 years.",
        "macros": {
            "Carbohydrates": 45,
            "Proteins": 20,
            "Healthy Fats": 35,
            "Daily Fiber": "40g (Microbiome-gut-brain axis signaling)"
        },
        "micronutrient_targets": {
            "Vitamin B-Complex (B6, B12, Folate)": "Lowers neurotoxic homocysteine",
            "DHA (Docosahexaenoic Acid)": "1,000 mg/day (Maintains synaptic membrane fluidity)",
            "Choline": "450 - 550 mg/day (Precursor for acetylcholine neurotransmitter)",
            "Curcumin & Resveratrol": "Synergistic clearance of amyloid aggregates"
        },
        "therapeutic_superfoods": [
            {"food": "Wild Blueberries & Blackberries (Anthocyanins)", "mechanism": "Crosses the blood-brain barrier, accumulating in the hippocampus to enhance neurogenesis and spatial memory."},
            {"food": "Dark Leafy Greens (Kale, Spinach, Swiss Chard)", "mechanism": "Rich in lutein, folate, and phylloquinone, associated with significant preservation of cognitive function."},
            {"food": "Wild-Caught Salmon & Sardines (DHA)", "mechanism": "DHA is the principal structural lipid in brain synapses; protects against tau hyperphosphorylation."},
            {"food": "Extra Virgin Olive Oil (Oleocanthal)", "mechanism": "Enhances the clearance of amyloid-beta via up-regulation of P-glycoprotein and LRP1 at the BBB."},
            {"food": "Raw Walnuts (Alpha-Linolenic Acid & Polyphenols)", "mechanism": "Reduces microglial neuroinflammation and oxidative damage in cortical neurons."}
        ],
        "strictly_prohibited_foods": [
            {"food": "Commercial Pastries & Sweets", "hazard": "Induces brain insulin resistance ('Type 3 Diabetes') and accelerates tau pathology."},
            {"food": "Margarine & Hydrogenated Spreads", "hazard": "Trans fats compromise blood-brain barrier integrity."},
            {"food": "Fast Food & Fried Foods (>1x per week)", "hazard": "Promotes systemic inflammation and microvascular white matter lesions."},
            {"food": "High-Sodium Processed Cheeses", "hazard": "Accelerates cerebral microvascular disease and cognitive decline."}
        ],
        "sample_meal_plan": {
            "breakfast": "Steel-cut oatmeal topped with 1 cup fresh wild blueberries, crushed walnuts, and a sprinkle of ground flaxseeds.",
            "lunch": "Large MIND salad with 2 cups of kale/spinach, grilled salmon, chickpeas, avocado, and extra virgin olive oil dressing.",
            "dinner": "Roasted chicken breast with turmeric, steamed broccoli, carrots, and a side of brown rice or quinoa.",
            "snacks": "A handful of raw almonds + 2 squares of 85%+ dark cacao chocolate."
        }
    }
}

class NutritionEngine:
    """Manages clinical nutritional blueprints and dietary metrics."""

    @staticmethod
    def get_protocol(disease_name: str) -> Dict[str, Any]:
        return DIET_PROTOCOLS.get(disease_name, DIET_PROTOCOLS["Type 2 Diabetes Mellitus"])
