# 2024 Rokken - Infrastructure Engineer Take-Home Assessment

## Overview

This assessment is designed to evaluate your skills in containerization, Kubernetes deployment, CI setup, Git usage, and technical documentation. You will be working with a sample application that consists of a FastAPI backend, a simple frontend, and a PostgreSQL database.

## Repository Contents

The provided GitHub repository contains the following:

1. A FastAPI backend (`main.py`)
2. A simple HTML/JavaScript frontend (`static/index.html`)
3. Basic API tests (`test_main.py`)
4. Instructions to run the application locally

## Tasks

Please complete the following tasks:

1. **Containerization:**
   - Containerize the application using Docker.
   - Create a Dockerfile for the backend that does not already contain python3.12 (not an official Python image, for example an Ubuntu base image) and installs Python 3.12 within the container.
   - Make the necesseary changes to the code to ensure everything runs correctly.

2. **Kubernetes Deployment:**
   - Create Kubernetes deployment configurations to run multiple instances of the application using "kind" (Kubernetes in Docker).
   - Include configurations for the backend, frontend, and database (PostgreSQL).
   - Ensure proper service discovery and networking between components.

3. **CI Setup:**
   - Set up a GitHub Actions workflow to:
     - Run the provided tests for the API.
     - Build the Docker image.
     - Verify the Kubernetes deployment (e.g., by creating a Kind cluster, applying your configurations, and checking the status of the pods and services).

4. **Git and GitHub:**
   - Make all your changes in a new branch of the provided repository.
   - Create a Pull Request with your changes to the main branch of the repository.

5. **Documentation:**
   - Write a (short) README.md file that includes:
     - An explanation of your design choices.
     - Instructions for running the application using Docker and Kubernetes.
     - Potential improvements or optimizations for the infrastructure setup.

You can make any necessary changes to the code python, html and javascript files to ensure everything runs correctly.
But you will not be evaluated on the code itself, only on the infrastructure setup.

## Running the Application Without Docker

To run the application without Docker, use the following commands:

```bash
# Start the PostgreSQL database (make sure it's installed and running)

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI backend
python main.py

# In a separate terminal, start the frontend server
python -m http.server 8080 --directory static

# Run tests
pytest
```

## Submission

1. Ensure all your changes are committed and pushed to your branch in the provided repository.
2. Create a Pull Request to the main branch of the same repository.
3. Submit the URL of your Pull Request.

If you find any issues with the assessment or have any questions, please reach out to us.

## Evaluation Criteria

You will be evaluated based on:

- Correctness and efficiency of the Docker and Kubernetes configurations.
- Proper setup and functionality of the CI pipeline.
- Git usage and Pull Request quality.
- Clarity and completeness of documentation.
- Overall code quality and best practices followed.

## Time Expectation

This assessment is designed to take approximately 3-4 hours for a qualified candidate. However, you have 7 days from the date of receiving this assessment to submit your solution. This extended timeframe is to accommodate different schedules and allow for thoughtful completion of the tasks.

If you find yourself spending significantly more time, please submit what you have completed along with notes on what you would do with more time.

Good luck!