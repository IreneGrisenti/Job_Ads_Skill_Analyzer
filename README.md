# Project description
This project aims at extracting skills from swedish job postings from 2026 for the occupation group classified as **SSYK 2511** (Systemanalytiker och IT-arkitekter m.fl.).


## Data
This project combines three datasets from Arbetsförmedlingen: a collection of active job ads, a collection of unpublished job ads and a taxonomy of skills. The goal was to collect as many ads as possible from 2026.
In Arbetsförmedlingen's taxonomy every occupation group has a concept ID, and the ID for 2511 is `UXKZ_3zZ_ipB`.

### Active job ads
**Source**: JobTech API (Arbetsförmedlingen / Platsbanken), https://jobsearch.api.jobtechdev.se/search, license CC0.  
**Period**: 2026-01-01 to date of retrieval 
**Retrieved on**: 2026-10-08  
**Limits**: the ads can contain personal information like names and phone numbers. Platsbanken also does not account for all the currently active job postings on the market.

### Historical job ads
**Source**: JobTech Historical API (Arbetsförmedlingen / Platsbanken), https://historical.api.jobtechdev.se/search, license CC0.  
**Period**: 2026-01-01 to date of retrieval 
**Retrieved on**: 2026-10-08  
**Limits**: the data does not account for currently published ads and duplicates remain.

### Skills taxonomy
**Source:** latest version from Arbetsförmedlingen open data, dataset *SSYK nivå fyra med relationer till kompetensbegrepp och yrkesbenämningar* (https://data.arbetsformedlingen.se/taxonomy/version/31/query/skills-with-related-skill-headlines-and-ssyk-level-4-groups), license CC0.
Only the group with concept id `UXKZ_3zZ_ipB` (SSYK 2511) is kept, this is the same id that the ads carry in `occupation_group.concept_id`  
**Retrieved on:** 2026-10-08, current version n. 31

### Labelled dataset
In order to evaluate the results of the models, I labeled a small dataset (120 ads) via Label Studio individuating hard skills.  
The definition of hard skill in this project is:  
*specific, teachable and measurable technical abilities required to perform job-related tasks, such as coding, data analysis, or cloud infrastructure management*.  
**Limits**: the labeling task was only performed by me, this means it reflects only my perspective and current knowledge of hard skills in the entire occupational group: some hard skills might have not been recognised or wrongly labeled.

### Reproducing the data
The labeled sets in `data/` are frozen, so the evaluation results can be reproduced from them.

If you re-run the fetch scripts, you will get a different snapshot of the ads. Running notebook `03_test_set_extraction.ipynb` on that new data will then extract a new sample of ads, which has to be labeled by hand again in Label Studio.

```python
python src/get_active_job_ads.py
python src/get_historic_job_ads.py
python src/get_skills.py # run this too if you want to get the latest version of the taxonomy
```

## Results

Evaluated on the labeled test set (micro-averaged, exact match after normalization):

| Metric    | Baseline | EntityRuler |
|-----------|----------|-------------|
| Precision | 0.500    | 0.692       |
| Recall    | 0.021    | 0.187       |
| F1        | 0.039    | 0.295       |


## Conclusions

- Matching taxonomy terms directly is not enough: the baseline finds only 2% of the labeled skills.
- A rule-based EntityRuler improves in all the metrics, but recall is still low (0.19). It finds few skills, and those are usually right.
- Most misses are English technical terms and long descriptive phrases that a fixed pattern list cannot cover.
- Occupational group 2511 is very small and heterogeneous. Each role comes with its own vocabulary and this partly explains the low recall.
- Some errors come from the labeling itself: languages and generic nouns are not labeled consistently, and very long spans count as a single skill.


## Next steps

1. Narrow the scope to data roles (e.g. data analyst, data engineer, data scientist, BI), so the skill vocabulary is more coherent.
2. Build a new labeled set for these roles, with a documented definition of hard skills and a clear rule for languages, generic terms and span length.
3. Restart from the EntityRuler, building patterns from the frequent skills in the new training set and adding case-insensitive and lemma variants.
4. Add partial-match evaluation next to exact match.
5. If recall is still low, try a trained NER model on the labeled spans.

<details>
<summary><b>Quick Start</b></summary>

Clone the repo:  
`git clone https://github.com/IreneGrisenti/Job_Ads_Skill_Analyzer.git`  

Create and activate a virtual environment:  
`cd Job_Ads_Skill_Analyzer`    
`python -m venv .venv`  
`source .venv/bin/activate` (for macOS/Linux) or `.venv\Scripts\Activate` (for Windows PowerShell)  

Install dependencies:  
`python -m pip install -e .` 

</details>

<details>
<summary><b>Environment</b></summary>

Python 3.13.7  
Packages: NumPy, Pandas, Jupyter, Spacy (see `pyproject.toml`) 
 
</details>


<details>
<summary><b>Project structure</b></summary>

```
Job_Ads_Skill_Analyzer/  
├── data/  
│   ├── labeled_set.json  
│   ├── labeled_test_set.json  
│   ├── labeled_val_set.json  
│   └── taxonomy_2511.json  
├── notebooks/   
│   ├── 01_exploration.ipynb  
│   ├── 02_cleaning.ipynb  
│   ├── 03_test_set_extraction.ipynb  
│   ├── 04_baseline.ipynb  
│   ├── 05_entity_ruler.ipynb  
│   └── 06_evaluation.ipynb  
├── src/   
│   ├── evaluation.py  
│   ├── get_active_job_ads.py    
│   ├── get_historic_job_ads.py  
│   ├── get_skills.py  
│   ├── models.py  
│   └── skills.py  
└── README.md  
```

</details>
