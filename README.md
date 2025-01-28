# Chatbot using Google LLM

This repository contains a chatbot application built using Google's Language Model (LLM). The chatbot is implemented in Python and can be used to interact with users in a conversational manner.

## Features

- Natural language understanding and generation
- Context-aware responses
- Easy to integrate and extend

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/BharatHBaddi0078/Chatbot-using-Google-LLM.git
    cd Chatbot-using-Google-LLM
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv .venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        .venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source .venv/bin/activate
        ```

4. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the chatbot, follow these steps:

1. **Set up your Google LLM API credentials**:
    - Obtain the API key from Google Cloud Platform.
    - Set the API key as an environment variable:
        ```bash
        export GOOGLE_API_KEY=your_api_key
        ```

2. **Run the chatbot**:
    ```bash
    python chatbot.py
    ```

## Configuration

You can configure the chatbot settings by modifying the `config.py` file. This file contains various parameters such as the chatbot's behavior, response style, and more.

## Contributing

We welcome contributions to improve the chatbot. If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

