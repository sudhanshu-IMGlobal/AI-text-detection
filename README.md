# AI_Text_Detection

## Project Overview
AI_Text_Detection is a AI-based project designed to detect AI-generated text. The goal is to classify text as either AI-generated or human-written using advanced models. This project implements a FastAPI application that exposes RESTful endpoints for text detection and other utilities.

## Features
- Detect AI-generated text using a LLM model.
- Provides a health check API endpoint to monitor the status of the service.
- API is fast and lightweight, built using **FastAPI**.
  
## Project Structure
The project is organized into several modules to ensure maintainability and scalability.

### `app/` - Core Application Logic
- **`services/`**: Contains services responsible for AI detection logic and any helper functions.
- **`routes/`**: Defines the API routes and request handlers.
- **`middlewares/`**: Contains custom middleware, such as rate-limiting or logging.
- **`utils/`**: Utility functions, including logging and configuration handling.


### `requirements.txt` - Project Dependencies
List of Python dependencies needed to run the application.

### `.env` - Environment Configuration
Contains environment-specific settings like API keys, model configurations, etc.

---

## Requirements
- Python 3.x
- **FastAPI** for creating the API.
- Additional libraries in `requirements.txt`.

---

## Installation

Follow these steps to set up the project:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/AI_Text_Detection.git
    cd AI_Text_Detection
    ```

2. **Install Required Dependencies:**
    Create a virtual environment and install the necessary packages:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Run the Application:**
    You can start the FastAPI application using `uvicorn`:
    ```bash
    uvicorn app.main:app --reload
    ```

    This will run the server in development mode, with live reloading on code changes.

4. **Environment Configuration:**
    Ensure you have the `.env` file properly configured (e.g., with any model paths, keys, etc.).

---

## API Documentation

### **1. Detect AI-Generated Text**

**Endpoint**: `POST /detect/`

**Description**: This endpoint accepts text and determines whether it is AI-generated or human-written based on model predictions.

#### Request
- **Body**:
  - `text` (string): The text to be analyzed. The maximum length can depend on the model used.
  
**Example Request**:
```json
{
  "text": "This is an example of a generated sentence."
}
```

Response
  - Success:
  - Status Code: 200 OK
  - Body:
  ```json
  {
  "confidence": 85.4
}
```

Fields:

  - is_ai_generated (boolean): Whether the text is AI-generated.
  - confidence (float): The percentage confidence that the text is
  AI-generated.
Error:

  - Status Code: 400 Bad Request
  - Body:
    ```json
    {
    "detail": "Text field is required"
    }
```
