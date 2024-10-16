# Ollama Tool Calling

This project demonstrates how to interact with the Ollama API to handle user queries and dynamically register and execute tools using a conversational AI model.

## Features

- Dynamically registers functions for tool calling.
- Executes a conversation flow with a user query.
- Handles API calls to process function calls and AI responses.
- Supports command-line input and a verbose mode for detailed output.
- Easily add or remove functions in `tools.py`.

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Shehryar718/OllamaToolCalling.git
   cd OllamaToolCalling
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the script with a default query:

```bash
python main.py
```

To pass a custom question and enable verbose output:

```bash
python main.py "What is 42+4123?" -v
```

## Customization

You can easily add or remove functions by modifying the `tools.py` file. Update the functions as needed to extend or change the capabilities of the tool calling functionality.
