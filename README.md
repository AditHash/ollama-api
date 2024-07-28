# Ollama API

This repository contains two Flask applications that utilize Langchain for natural language processing. The first application handles text inputs (`llama31.py`), while the second application processes both text and image inputs (`llava.py`).

## Prerequisites

- Python 3.7+

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/AditHash/ollama-api.git
    cd ollama-api
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Text Input Application (`llama31.py`)

This application processes text inputs and generates responses using the Langchain model with conversation memory.

#### Running the Application

1. Navigate to the directory containing `llama31.py`:
    ```bash
    cd path/to/llama3.1
    ```

2. Run the Flask application:
    ```bash
    python llama31.py
    ```

3. The application will be available at `http://127.0.0.1:5000/chat`.

#### API Endpoint

- `POST /chat`
    - **Request Body**: JSON object containing `user_input`.
    - **Response**: JSON object containing the generated response.

    ```json
    {
        "user_input": "What is the capital of France?"
    }
    ```

### Text and Image Input Application (`llava.py`)

This application processes both text and image inputs, converts the image to a Base64 encoded string, and generates responses using the Langchain model with conversation memory.

#### Running the Application

1. Navigate to the directory containing `llava.py`:
    ```bash
    cd path/to/llava
    ```

2. Run the Flask application:
    ```bash
    python llava.py
    ```

3. The application will be available at `http://127.0.0.1:5000/image-chat`.

#### API Endpoint

- `POST /image-chat`
    - **Request Parameters**:
        - `image_input`: File (JPEG, JPG, PNG).
        - `user_input`: Text input.
    - **Response**: JSON object containing the generated response.

    Example using `curl`:
    ```bash
    curl -X POST http://127.0.0.1:5000/image-chat \
        -F "image_input=@/path/to/image.jpg" \
        -F "user_input=What is the animal shown in image?"
    ```

