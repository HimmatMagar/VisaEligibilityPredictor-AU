# Australia Visa Eligibility Prediction

This repository contains an end‑to‑end machine learning system for predicting whether an Australian visa
application will be granted.  The model is trained on historical application data (age, visa type,
documents submitted, etc.) and exposes a FastAPI service (`app.py`) so that predictions can be made
from a web form or other clients.

The goal of the project is to demonstrate a complete workflow from data ingestion through
validation, transformation, model building, evaluation and serving.

## Project Workflow
1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the app.py

### How to setup?
## Repository layout

Below is a high‑level view of the important files and folders.  The `research/` directory contains
notebooks used during development; only the high‑level `experiment.ipynb` and `trials.ipynb` are
listed here – the step‑by‑step notebooks have been omitted for brevity.

```
.
├── app.py                    # FastAPI application for predictions
├── main.py                   # entry point for running the pipeline
├── params.yaml               # hyperparameters and configuration values
├── schema.yaml               # expected schema for input data
├── config/
│   └── config.yaml           # configuration manager, settings
├── src/                      # source package for the visaPrediction module
│   └── visaPrediction/       # training pipeline, utilities, entities, etc.
├── artifact/                 # generated artifacts including models, transformers, logs
│   ├── data_ingestion/
│   │   └── australia_visa_applications.csv
│   ├── data_transformation/
│   ├── data_validation/
│   │   └── status.txt
│   ├── model_building/
│   │   └── model.pkl
│   └── model_evaluation/
│       └── mertic.json       # evaluation metrics produced after training
├── templates/                # HTML templates for the web UI
│   └── index.html
├── research/                 # Jupyter notebooks used during experimentation
│   ├── experiment.ipynb
│   └── trials.ipynb
├── requirements.txt          # Python dependencies
├── setup.py                  # packaging information
├── README.md                 # you are reading this file
└── dockerfile                # instructions for containerising the app
```

#### Steps:
1. Clone the Reprosetory
```bash
git clone https://github.com/HimmatMagar/VisaEligibilityPredictor-AU
cd folder name
```
## Getting started

### Prerequisites

Install Python 3.12 and `conda` if you wish to use a virtual environment.

### Setup steps

1. Clone the repository:
	```bash
	git clone https://github.com/HimmatMagar/VisaEligibilityPredictor-AU.git
	cd VisaEligibilityPredictor-AU
	```

2. Create and activate a conda environment:
	```bash
	conda create -p env python==3.12 -y
	conda activate env/
	```

3. Install dependencies:
	```bash
	pip install -r requirements.txt
	```

2. Create a conda environment
```bash
conda create -p env python==3.12 -y
```

3. Activate conda environment
```bash 
conda activate env/
```

## Model performance

The model was evaluated on a hold‑out set.  The following metrics are stored in
`artifact/model_evaluation/mertic.json`:

```json
{
	"Class_0": {
		"precision": 1.0,
		"recall": 0.8785236849752979,
		"f1-score": 0.9353341584158416,
		"support": 3441.0
	},
	"Class_1": {
		"precision": 0.8595901914679207,
		"recall": 1.0,
		"f1-score": 0.9244942196531792,
		"support": 2559.0
	},
	"accuracy": 0.9303333333333333
}
```

*Accuracy is approximately 93.0%, with strong precision/recall for both classes.*

These results can be updated by running the training pipeline (`main.py`) on new data.

---

Feel free to explore the notebooks under `research/` for more details about the data
preparation and model experimentation.
