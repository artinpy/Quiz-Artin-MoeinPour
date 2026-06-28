# 🧠 Quiz Management System (CLI)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-red.svg)](https://www.sqlalchemy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A robust **Command-Line Interface (CLI)** application built with Python and SQLAlchemy to streamline the creation, management, and execution of multiple-choice quizzes. This platform empowers instructors to seed dynamic questions and enables students to participate in quizzes interactively with instant scoring.

---

## ✨ Features

- **User Management**: Add and manage student profiles.
- **Question Bank**: Pre-define multiple-choice questions with correct answers (via `seed.py`).
- **Interactive CLI**: Intuitive menu-driven interface for students to take quizzes.
- **Real-time Scoring**: Automatically calculates scores and displays results instantly.
- **Performance Tracking**: View top performers and leaderboards to track progress.
- **Full CRUD Support**: Create, Read, Update, and Delete questions/answers programmatically.

---

## 🛠️ Technologies Used

- **Python 3.8+** – Core programming language.
- **SQLAlchemy (ORM)** – Database abstraction and object-relational mapping.
- **SQLite** – Lightweight embedded database (default, easily configurable).
- **Argparse/Click** – (Optional) Advanced CLI parsing.

---

## 📁 Project Structure

The repository is structured to keep concerns separated and maintainable:

```plaintext
.
├── main.py          # CLI entry point. Runs the interactive menu.
├── models.py        # SQLAlchemy ORM models (User, Question, Answer, etc.).
├── db.py            # Database engine, session factory, and base class.
├── crud.py          # Core database operations (YOUR TASK: complete 3 functions).
├── seed.py          # Pre-populates the database with initial questions.
├── requirements.txt # Project dependencies.
└── README.md        # Project documentation (this file).
```
🚀 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine for development and testing.

Prerequisites
Python 3.8 or higher installed on your system.

pip package manager.

Installation
Clone the repository

bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
Create a virtual environment (Recommended)

bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
# OR
venv\Scripts\activate      # On Windows
Install dependencies

bash
pip install -r requirements.txt
(If requirements.txt is not provided, install SQLAlchemy manually: pip install sqlalchemy)

Initialize the Database
Run the seed script to create the database file and populate it with sample questions:

bash
python seed.py
💻 Usage
To start the quiz manager, simply run:

bash
python main.py
Follow the on-screen prompts to:

Create a new user profile.

Start a quiz session.

Answer the multiple-choice questions.

View your final score and the leaderboard.

🧩 Implementation Tasks (Homework Guide)
Based on the course requirements (Dore 5 - Fanavari Tehran), you need to complete the following 3 programming tasks:

1. Design 4 Questions in seed.py
You must define 4 multiple-choice questions inside the seed.py file. Ensure they are relevant and properly structured (e.g., question text, 4 options, and the correct answer index). Run this script to populate your database.

2. Test the Application in main.py
Ensure the main CLI loop handles user inputs robustly. Validate that:

Users can select a question and submit answers.

The system properly transitions between questions.

Scores are calculated and displayed correctly at the end.

3. Complete the 3 Functions in crud.py
You will find 3 incomplete functions in this file (marked with # TODO or pass). Your job is to implement their logic:

Function A: Likely handling quiz submission or answer validation.

Function B: Fetching or aggregating user scores.

Function C: Updating or deleting a specific record (e.g., a question).

💡 Tip: Refer to the models.py file to understand the table structures (columns and relationships) before writing your SQLAlchemy queries.

🤝 Contributing & Collaboration
This project is part of an academic course. To submit your work and receive feedback:

Create a repository with a standard name (as specified by your instructor).

Upload your fully implemented code.

Add your professor as a Collaborator on GitHub:

Go to Settings > Collaborators > Add People.

Enter your professor's GitHub username or email.

📅 Deadline
Duration: 2 Weeks from the project announcement.

Final Submission: Send the GitHub repository link 1 day before the final deadline.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

📬 Contact
For any questions or support regarding this project, please reach out via the course platform or contact your instructor.

Fanavari Tehran
www.Fanavari.co
