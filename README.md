# Kitchen Helper

A Python desktop application for personalized recipe discovery and automated shopping list generation using the Spoonacular API.

## Overview

Kitchen Helper is a desktop application designed to simplify meal planning. Users can search for recipes based on their dietary preferences and available ingredients, explore cooking instructions, and generate a consolidated shopping list from the selected recipes.

The project combines a graphical user interface with external REST API integration to provide a practical and user-friendly cooking assistant.

## Features

- **Personalized Recipe Search:** Find recipes based on dietary preferences, such as vegan, keto, or gluten-free, and available ingredients.
- **Recipe Details:** View ingredient lists and cooking instructions.
- **Shopping List Generation:** Consolidate ingredients from selected recipes into a single shopping list.
- **Desktop Interface:** Interact with the application through a graphical interface built with Tkinter.

## Technologies

- **Language:** Python 3
- **GUI:** Tkinter
- **HTTP Requests:** Requests
- **External API:** Spoonacular API via RapidAPI

## Getting Started

### Prerequisites

Before running the application, make sure you have:

- Python 3 installed.
- A RapidAPI account with access to the Spoonacular API.
- The API key required to make requests.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Goncaloctomas/kitchen-helper-app.git
   cd kitchen-helper-app
   ```

2. Install the required dependency:

   ```bash
   python -m pip install requests
   ```

3. Configure the API key.

   Set up your RapidAPI key in the configuration used by the application. Keep your API key private and avoid committing credentials to the repository.

4. Run the application using the Python file that contains the main entry point. For example, if the entry point is `appcolinaria.py`:

   ```bash
   python appcolinaria.py
   ```

   If your main file has a different name, replace `appcolinaria.py` with the correct filename.

## Learning Objectives

This project provided practical experience with:

- Python application development.
- Building graphical user interfaces with Tkinter.
- Consuming external REST APIs.
- Making HTTP requests and handling API responses.
- Organizing recipe information and generating shopping lists.

## License

This project was developed for educational and demonstration purposes.
