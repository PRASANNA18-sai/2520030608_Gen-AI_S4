# Week 1 - First LLM Call Using Ollama

## Objective
To install and configure a locally running Large Language Model (LLM) using Ollama and generate responses to user prompts through Python.

## Technologies Used
- Python
- Ollama
- Llama 3.2 (1B)
- VS Code

## Prerequisites
- Python installed
- Ollama installed
- Llama 3.2 (1B) model downloaded

## Setup Instructions

1. Install Ollama from https://ollama.com/
2. Download the model:

   ollama pull llama3.2:1b

3. Install Python dependencies:

   python -m pip install -r requirements.txt

4. Run the Python program:

   python main.py

## Experiments
The model was tested with the following prompts:

1. What is Artificial Intelligence? Explain in simple words.
2. Explain Generative AI with two real-world examples.
3. What is a Large Language Model? Explain for a first-year engineering student.
4. Differentiate Artificial Intelligence, Machine Learning, and Deep Learning.

## Result
Successfully configured Ollama, connected the local LLM with Python, and generated responses to multiple prompts without requiring an external API key.
