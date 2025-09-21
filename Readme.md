# Sentiment Analysis MLOps API

This project is a simple REST API for sentiment analysis, built with an MLOps approach. It provides a web endpoint to classify text as either positive or negative using a pre-trained Scikit-learn model.

The primary goal is to demonstrate a basic CI/CD pipeline using Docker and GitHub Actions.

---

## Features
-   Classifies English text into "Positive" or "Negative" sentiment.
-   REST API endpoint for easy integration.
-   Packaged with Docker for consistent deployment.
-   Automated testing pipeline with GitHub Actions.

---

## Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd sentiment_analysis_mlops
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For Mac/Linux
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    The application will be running at `http://127.0.0.1:5000`.

---

## API Usage

You can test the API endpoint using a tool like `curl` or Postman.

**Endpoint:** `/predict`
**Method:** `POST`
**Body:** JSON with a "text" key.

**Example using `curl`:**
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"text\":\"I absolutely loved this movie, it was fantastic!\"}" [http://127.0.0.1:5000/predict](http://127.0.0.1:5000/predict)