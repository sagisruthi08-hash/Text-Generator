🤖 Zuki Text Generator

An AI-powered text generation web application built with Python, Streamlit, Hugging Face Transformers, and DistilGPT-2.

Zuki Text Generator allows users to enter a sentence or prompt and generate AI-completed text through a simple and interactive web interface.

🚀 Features

✨ Simple and user-friendly interface

🤖 AI-powered text generation

📝 Enter your own sentence or prompt

⚡ Generate text with one click

🎯 Uses the pre-trained DistilGPT-2 language model

🌐 Built with Streamlit for an interactive web application

🛠️ Technologies Used

Python

Streamlit

Hugging Face Transformers

DistilGPT-2

PyTorch

📸 Application Preview

📂 Project Structure

LLM-skill-verse/ │ ├── text_generator.py ├── app.py ├── README.md └── screenshot.png

⚙️ Installation

Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL cd LLM-skill-verse

Install the required libraries
pip install streamlit transformers torch torchvision

Run the application
python -m streamlit run text_generator.py

💡 How It Works

Enter a sentence or prompt in the text box.

Click Generate Text.

The application sends the prompt to the DistilGPT-2 text-generation pipeline.

The generated text is displayed on the page.

🧠 Model

This project uses DistilGPT-2, a lightweight version of GPT-2 designed for text generation.

The model is loaded using the Hugging Face Transformers pipeline:

from transformers import pipeline

generator = pipeline( "text-generation", model="distilgpt2" )

🎯 Project Goal

The goal of this project is to gain practical experience in:

Generative AI

Natural Language Processing (NLP)

Pre-trained transformer models

Python application development

Streamlit web applications

Integrating AI models into real-world applications






