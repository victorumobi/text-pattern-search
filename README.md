# text-pattern-search
A repository containing code for an application that searches through a given text string and counts occurrences of a specified pattern. Implements the workflow using the Apollo runtime system for Cloud, Edge, and IoT Computing. Tasks include text batching, pattern counting, and overall occurrence summation.


# Text Pattern Search

This project implements an application for searching through a given text string and counting occurrences of a specified pattern. The workflow is orchestrated using the Apollo runtime system for Cloud, Edge, and IoT Computing.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Tasks](#tasks)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Describe the purpose of your project and provide a brief overview. Mention any technologies or frameworks used, such as the Apollo runtime system.

## Project Structure

- `lambda_handler.py`: AWS Lambda handler function for the application.
- `divide_into_batches.py`: Function for dividing the text into batches.
- `count_occurrences.py`: Function for counting occurrences in a batch.
- `sum_occurrences.py`: Function for summing up overall occurrences.
- `composition.afcl`: Apollo Composition file describing the workflow.

## Usage

Explain how to use the application, including any input parameters or configuration. Provide examples or sample inputs if applicable.

## Tasks

- **Task 1**: Implement the basic workflow.
- **Task 2**: Implement the complete application with potential input string modification.
- **Task 3**: Deploy functions on AWS/IBM and as Docker images with a custom scheduler.

## Contributing

If you'd like to contribute to this project, please follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

