# CineScore – IMDB Sentiment Analyzer

A lightweight web application that classifies movie reviews (trained on the IMDB dataset) as **positive** or **negative** using a scikit‑learn model.

## Features
- FastAPI backend exposing `/analyze` endpoint
- Tailwind CSS CDN UI with cinematic amber theme, star rating, confidence bar, and example reviews
- Real‑time character counter, `Ctrl+Enter` shortcut, and animated result panel
- Model returns both sentiment label and confidence score

## Setup
```bash
# Clone the repo (if not already)
git clone <repo-url>
cd "ML Projects/Sentimental Analysis"

# Create virtual environment
python -m venv venv
source venv/Scripts/activate   # Windows PowerShell

# Install dependencies
pip install -r requirements.txt
```

The `requirements.txt` should contain:
```
fastapi
uvicorn[standard]
scikit-learn
nltk
joblib
```

## Run the application
```bash
uvicorn main:app --reload   # default port 8000
# or custom port
uvicorn main:app --reload --port 3000
```
Open your browser at `http://127.0.0.1:8000` (or the chosen port) and start analyzing movie reviews!

## Project structure
```
├─ index.html          # Tailwind UI (CineScore)
├─ main.py             # FastAPI server with /analyze endpoint
├─ preprocessing/
│   ├─ clean_text.py   # text cleaning utilities
│   └─ Sentiment_Model.pkl  # trained scikit‑learn model
└─ README.md           # <-- this file
```

## License
MIT – feel free to fork, modify, and improve!
