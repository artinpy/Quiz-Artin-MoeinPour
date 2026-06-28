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
