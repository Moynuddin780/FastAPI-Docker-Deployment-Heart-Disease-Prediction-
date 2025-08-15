# Heart Disease Prediction API 

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)](https://www.docker.com/)
[![Deployed on Render](https://img.shields.io/badge/Deployed%20on-Render-blue?logo=render)](https://render.com/)

A simple, dockerized FastAPI application for predicting heart disease using a Random Forest classifier trained on the UCI Heart Disease dataset. This project emphasizes API development, containerization with Docker, and cloud deployment on Render, with minimal focus on model optimization.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Training the Model](#training-the-model)
- [Running Locally](#running-locally)
- [Dockerization](#dockerization)
- [Deployment to Render](#deployment-to-render)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview
This API predicts whether a patient has heart disease based on 13 clinical features (e.g., age, cholesterol, chest pain type). The model is trained on the [UCI Heart Disease dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset), serialized with Joblib, and served via FastAPI. The app is containerized with Docker and deployed to Render for easy access.

**Note**: The focus is on deployment and API setup, not on achieving high model accuracy.

## Features
- **Health Check Endpoint**: Verify API status with a simple GET request.
- **Info Endpoint**: Retrieve model metadata (type and input features).
- **Prediction Endpoint**: Submit patient data to get a binary heart disease prediction.
- **Interactive Docs**: Swagger UI for testing endpoints.
- **Docker Support**: Run locally with Docker Compose.
- **Cloud Deployment**: Hosted on Render for live access.

## Tech Stack
- **Backend**: FastAPI (async Python framework)
- **Machine Learning**: Scikit-learn (Random Forest Classifier)
- **Serialization**: Joblib
- **Input Validation**: Pydantic
- **Containerization**: Docker, Docker Compose
- **Deployment**: Render (free tier supported)
- **Dependencies**: Pandas, NumPy

## Project Structure
```
heart-disease-prediction/
├── app/
│   ├── main.py           # FastAPI app with endpoints
│   └── schemas.py        # Pydantic model for input validation
├── model/
│   └── heart_model.joblib  # Trained model (generated)
├── data/
│   └── heart.csv         # Dataset (download from Kaggle)
├── train_model.py        # Script to train and save model
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
└── README.md             # This file
```

## Setup and Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/heart-disease-prediction.git
   cd heart-disease-prediction
   ```

2. **Create a Virtual Environment** (optional, but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Dataset**:
   - Visit [Kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset).
   - Download `heart.csv` and place it in the `data/` folder.
   - **Note**: Add `data/` to `.gitignore` to avoid committing the dataset.

## Training the Model
1. Run the training script to generate the Random Forest model:
   ```bash
   python train_model.py
   ```
2. This creates `model/heart_model.joblib`.
3. The dataset includes 14 columns: `age`, `sex`, `cp`, `trestbps`, `chol`, `fbs`, `restecg`, `thalach`, `exang`, `oldpeak`, `slope`, `ca`, `thal`, `target` (1 = disease, 0 = no disease).

## Running Locally
Run the FastAPI app directly (without Docker):
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
- Access Swagger UI at: http://localhost:8000/docs
- Use `/health`, `/info`, or `/predict` endpoints.

## Dockerization
1. **Build the Docker Image**:
   ```bash
   docker-compose build
   ```

2. **Run the Container**:
   ```bash
   docker-compose up
   ```

3. Access the app at http://localhost:8000/docs.

The `Dockerfile` uses `python:3.10-slim`, installs dependencies, copies the app and model, and runs Uvicorn on port 8000.

## Deployment to Render
1. **Push to GitHub**:
   - Ensure `model/heart_model.joblib` is committed.
   - Add `data/heart.csv` to `.gitignore` if not already done.
   - Push to your repository:
     ```bash
     git add .
     git commit -m "Initial commit"
     git push origin main
     ```

2. **Deploy on Render**:
   - Sign up/login at [Render](https://render.com).
   - Create a new **Web Service** and select **Docker** as the environment.
   - Connect your GitHub repository.
   - Set the build context to the root directory (where `Dockerfile` is).
   - Deploy and wait for the build to complete.
   - Get your live URL (Render App Link - 'https://fastapi-docker-deployment-for-heart.onrender.com/docs`).

3. Test endpoints via Swagger UI (`/docs`) or tools like Postman.

**Alternative Hosts**: You can use Heroku, AWS, or GCP with similar Docker-based deployment steps.

## API Endpoints
| Method | Endpoint       | Description                              | Example Response                     |
|--------|----------------|------------------------------------------|-------------------------------------|
| GET    | `/health`      | Check API status                         | `{"status": "healthy"}`            |
| GET    | `/info`        | Get model type and feature list          | `{"model_type": "RandomForestClassifier", "features": [...]}` |
| POST   | `/predict`     | Predict heart disease from input features | `{"heart_disease": true}`          |

**POST /predict Example**:
```json
{
  "age": 63,
  "sex": 1,
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}
```
Response: `{"heart_disease": true}` or `{"heart_disease": false}`.

## Testing
- **Swagger UI**: Open `http://localhost:8000/docs` (local) or `https://your-app.onrender.com/docs` (deployed) to test interactively.
- **curl**:
  ```bash
  curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"age":63,"sex":1,"cp":3,"trestbps":145,"chol":233,"fbs":1,"restecg":0,"thalach":150,"exang":0,"oldpeak":2.3,"slope":0,"ca":0,"thal":1}'
  ```
- **Postman**: Import the OpenAPI spec from `/openapi.json` for testing.

## Troubleshooting
- **Model not found**: Ensure `train_model.py` was run and `model/heart_model.joblib` exists.
- **Docker build fails**: Check `requirements.txt` for version conflicts or missing dependencies.
- **Render deployment fails**: Verify `Dockerfile` is at the repo root and `model/` is committed.
- **Prediction errors**: Ensure input JSON matches the Pydantic schema in `schemas.py`.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Issues and suggestions are welcome via GitHub Issues!

## License
MIT License. See [LICENSE](LICENSE) for details.

---

Built with by Moynuddin Al Masum. For questions, reach out via GitHub Issues.
