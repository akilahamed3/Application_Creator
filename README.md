# Application_Creator
Application Creator is an AI-powered application generator built with LangGraph. It functions as a multi-agent development pipeline that takes a natural language prompt and transforms it into a complete, fully functional web application — generating every file from scratch using a structured, real-world software engineering workflow.

# Architecture
Planner Agent – Analyzes your request and generates a detailed project plan.
Architect Agent – Breaks down the plan into specific engineering tasks with explicit context for each file.
Coder Agent – Implements each task, writes directly into files, and uses available tools like a real developer.

# Installation and Startup
Create a virtual environment using: uv venv and activate it using source .venv/bin/activate
Install the dependencies using: uv pip install -r pyproject.toml
Create a .env file and add the variables and their respective values mentioned in the .sample_env file
After all the set-up & installation steps we can start the application using the following command:
  python main.py

# Example Prompts
Create a to-do list application using html, css, and javascript.
Create a simple calculator web application.
Create a simple blog API in FastAPI with a SQLite database.
