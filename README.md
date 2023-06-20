# My Personal Chat

Welcome to My Personal Chat, a simple and intuitive message board designed for personal use. This is my first ever project using Python and Flask, and it easily allows anyone to anononymously send messages to themselves and track them with timestamps.

## Prerequisites

Before running this project, please ensure that you have the following software installed on your machine:

- Python 3: [Download Python](https://www.python.org/downloads/)
- Flask: Install Flask by running the command `pip install flask`

## Getting Started

To run this project locally, follow the steps below:

1. Clone this repository to your local machine.
2. Open your preferred terminal and navigate to the project directory: `cd my-personal-chat`
3. Create a virtual environment for the project: `python -m venv venv`
4. Activate the virtual environment:
   - For Windows: `venv\Scripts\activate`
   - For macOS/Linux: `source venv/bin/activate`
5. Install the project dependencies: `pip install -r requirements.txt`
6. Start the Flask server: `flask run --app server.py`
7. Open your web browser and visit `http://localhost:5000` to access the chat application.

## Project Description

This chat application is specifically designed for personal use, enabling anyone to easily send messages to themselves in and track them using timestamps. It serves as a personal journal, allowing you to record your thoughts, ideas, and important notes in a convenient and accessible manner.

The server.py file acts as the main Flask application file, handling the backend functionality and routing. All HTML and CSS code is contained within this file, eliminating the need for separate template or static files.

## Goal and Use Case

The purpose of this project was to buiild the basics of a another chat that I am buiding right now, a personal chat using the ChatGPT API. Thisprovides a personal chat environment that will enable the user to have conversations with ChatGPT even when ChatGPT overloads or crashes.

## Contributing

Contributions, suggestions, and improvements are always welcome! If you have any ideas to enhance this project, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
