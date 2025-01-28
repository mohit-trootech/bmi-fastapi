# BMI API

This is a simple BMI (Body Mass Index) calculator API built with FastAPI.

## Features

- Calculate BMI based on height and weight
- Categorize BMI results (Underweight, Normal weight, Overweight, Obesity)
- Fast and efficient API built with FastAPI

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/mohit-trootech/bmi-fastapi
    cd bmi-fastapi
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the API server:

    ```sh
    uvicorn main:app --reload
    ```

2. Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation (Swagger UI).

## API Endpoints

- `POST /bmi` - Calculate BMI
  - Request body:

```json
{
    "height": 1.75,
    "weight": 70
}
```

- Response:

```json
{
    "bmi": 22.86,
    "category": "Normal weight"
}
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
