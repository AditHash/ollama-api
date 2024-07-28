# ollama-demo
Python APIs built with ollama models (llama3.1 &amp; llava)


# Flask Applications with Langchain

This repository contains two Flask applications that utilize Langchain for natural language processing. The first application handles text inputs, while the second application processes both text and image inputs.

## Prerequisites

- Python 3.7 or higher
- Flask
- PIL (Pillow)
- Langchain
- Langchain Ollama

## Installation

1. Clone this repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required packages:
    ```bash
    pip install flask pillow langchain-core langchain-ollama
    ```

## Usage

### Text Input Application

This application processes text inputs and generates responses using the Langchain model with conversation memory.

#### Running the Application

1. Navigate to the directory containing `app_text.py`:
    ```bash
    cd path/to/app_text
    ```

2. Run the Flask application:
    ```bash
    python app_text.py
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

### Text and Image Input Application

This application processes both text and image inputs, converts the image to a Base64 encoded string, and generates responses using the Langchain model with conversation memory.

#### Running the Application

1. Navigate to the directory containing `app_image.py`:
    ```bash
    cd path/to/app_image
    ```

2. Run the Flask application:
    ```bash
    python app_image.py
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
        -F "user_input=What is the dollar based gross retention rate?"
    ```

if __name__ == '__main__':
    app.run(debug=True)
