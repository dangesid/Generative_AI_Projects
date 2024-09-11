# Gemini AI Chatbot Project

This project is dedicated to building a QA Chatbot using a virtual environment setup. The chatbot is designed to handle questions and answers in a specified domain using AI models.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [Contact](#contact)

## Project Overview

The Gemini AI Chatbot is an AI-powered chatbot designed to answer questions efficiently in a conversational style. It uses machine learning models, NLP techniques, and a carefully curated dataset to provide accurate responses. 

## Features

- Natural Language Processing (NLP) based chatbot.
- Pre-trained AI models with customization capabilities.
- Easy-to-setup virtual environment using Python.
- Scalable for integration with web apps or other interfaces.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/dangesid/Gemini_Ai.git
   cd Invoice_Extractor

2. **Set up a Virtual Environment**
    ```bash
   conda create -p venv python==3.10 -y
   conda activate < Location of venv >

3. **Install the requirements file**
    ```bash
   pip install -r requirements.txt

4. **To run the GenAI App** 
    ```bash
   streamlit run app.py 
   
## Usage
This section provides detailed instructions on how to use the Gemini AI Chatbot after installation.
The chatbot may require some configuration before it can run effectively. Below are some common configuration steps:

Environment Variables: If the chatbot relies on API keys or specific environment settings, make sure to set them up before running. You can set environment variables using a .env file or directly in the command line.

Example .env file:

API_KEY= your_api_key_here

Create your cusotom api key from googleStudio (https://aistudio.google.com/app/apikey)
and add the api key in the .env file in your folder structure

## Folder Structer 
The following is an overview of the project's folder structure:

```plaintext
Gemini AI Chatbot Project/
│
├── venv/                        # Virtual environment (not tracked by Git)      
├── .env                         # Contains the API_KEY
├── requirements.txt             # Python dependencies
├── app.py                       # GenAI Application
└── README.md                    # Project documentation
```

## Contributing 
Contributions are welcome! If you'd like to improve the project or add new features, please follow these steps:

Fork the repository.
1. Create a new branch (git checkout -b feature-branch).
2. Make your changes and commit (git commit -m "Description of changes").
3. Push your branch (git push origin feature-branch).
4. Open a pull request.

## Contact
For questions, feedback, or support, feel free to contact:

Name: Siddharth Dange

Email: dangesid1999@gmail.com

GitHub: https://github.com/dangesid