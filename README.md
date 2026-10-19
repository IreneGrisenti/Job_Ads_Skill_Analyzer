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

### Hitorical job ads
**Source**: JobTech Historical API (Arbetsförmedlingen / Platsbanken), https://historical.api.jobtechdev.se/search, license CC0.  
**Period**: 2026-01-01 to date of retrieval 
**Retrieved on**: 2026-10-08  
**Limits**: the data does not account for currently pubblished ads and duplicates remain.

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
The taxonomy and labeled sets are available in the repo.  
But if you want to reproduce the raw data, run the two scripts from the project root.

```python
python src/get_active_job_ads.py
python src/get_historic_job_ads.py
python src/get_skills.py # run this too if you want to get the latest version of the taxonomi
```

## Quick Start
Clone the repo:  
`git clone https://github.com/IreneGrisenti/Job_Ads_Skill_Analyzer.git`  

Create and activate a virtual environment:  
`cd Job_Ads_Skill_Analyzer`    
`python -m venv .venv`  
`source .venv/bin/activate` (for macOS/Linux) or `.venv\Scripts\Activate` (for Windows PowerShell)  

Install dependencies:  
`python -m pip install -e .`  


## Environment  
Python 3.13.7  
Packages: NumPy, Pandas, Jupyter, Spacy (see `pyproject.toml`)  

## Project structure

```text
Job_Ads_Skill_Analyzer/
├── data/
│   ├── labeled_set_set.json
│   ├── labeled_test_set.json
│   ├── labeled_val_set.json
│   └── taxonomi_2511.json
├── notebooks/00  
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