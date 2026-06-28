# 🧠 Quiz Management System (CLI)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0+-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge" />
</p>

<p align="center">
  <b>A modern Command-Line Quiz Management System built with Python, SQLAlchemy and SQLite.</b>
</p>

<p align="center">
Create quizzes, manage students, store questions in a database, and calculate scores automatically — all from an interactive terminal interface.
</p>

---

# 📑 Table of Contents

* [Overview](#-overview)
* [Features](#-features)
* [Tech Stack](#-tech-stack)
* [Installation](#-installation)
* [Quick Start](#-quick-start)
* [Usage](#-usage)
* [Project Structure](#-project-structure)
* [Database Architecture](#-database-architecture)
* [Future Improvements](#-future-improvements)
* [Contributing](#-contributing)
* [License](#-license)
* [Author](#-author)

---

# 📖 Overview

The **Quiz Management System** is a Python-based Command-Line Interface (CLI) application designed for creating, managing, and taking multiple-choice quizzes.

The application allows instructors to maintain a database of quiz questions while enabling students to participate in quizzes interactively. It automatically calculates scores, stores user information, and provides an organized workflow for quiz management.

This project demonstrates practical usage of:

* Object-Oriented Programming (OOP)
* SQLAlchemy ORM
* SQLite Database
* CRUD Operations
* Modular Python Architecture
* Interactive Command-Line Interfaces

---

# ✨ Features

## 👨‍🎓 Student Management

* Register new students
* Store participant information
* Manage user records

---

## 📝 Question Management

* Store multiple-choice questions
* Save correct answers
* Populate database using `seed.py`
* Easily expand the question bank

---

## 🎮 Interactive Quiz

* Terminal-based menu
* User-friendly navigation
* Multiple-choice answering system
* Automatic validation

---

## 📊 Score Calculation

* Instant grading
* Display final score
* Performance evaluation

---

## 🏆 Leaderboard

* View highest scores
* Compare student performance

---

## 🛠 CRUD Operations

Supports complete database operations:

* Create
* Read
* Update
* Delete

---

# 🧰 Tech Stack

| Technology  | Purpose                        |
| ----------- | ------------------------------ |
| Python 3.8+ | Main programming language      |
| SQLAlchemy  | Object Relational Mapper (ORM) |
| SQLite      | Local database                 |
| CLI         | User Interface                 |
| Seed Script | Database initialization        |

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/artinpy/Quiz-Artin-MoeinPour.git
```

Move into the project

```bash
cd Quiz-Artin-MoeinPour
```

Install dependencies

```bash
pip install -r requirements.txt
```

Initialize the database

```bash
python seed.py
```

Run the application

```bash
python main.py
```

---

# 🚀 Quick Start

After launching the application, users are presented with an interactive menu where they can:

* Register students
* Start quizzes
* Answer questions
* View scores
* Display rankings
* Exit the application

Everything is handled directly through the terminal.

---

# 💻 Example Workflow

```text
=============================
 Quiz Management System
=============================

1. Start Quiz

2. Register Student

3. Leaderboard

4. Exit

Select an option:
```

Example:

```text
Question 1

Which language is used with SQLAlchemy?

A) Java

B) Python

C) C++

D) PHP

Answer: B

✔ Correct!

Current Score: 1
```

---

# 📂 Project Structure

```text
Quiz-Artin-MoeinPour
│
├── main.py
│   └── Application entry point
│
├── db.py
│   └── Database engine & session configuration
│
├── models.py
│   └── SQLAlchemy ORM models
│
├── crud.py
│   └── CRUD operations
│
├── seed.py
│   └── Insert initial quiz questions
│
├── requirements.txt
│   └── Project dependencies
│
└── README.md
    └── Project documentation
```

---

# 🗄 Database Architecture

The project uses **SQLite** together with **SQLAlchemy ORM** to simplify database interactions.

Main entities include:

* Students
* Questions
* Answers
* Scores

The ORM layer abstracts SQL queries and provides a clean Pythonic interface for data manipulation.

---

# 📈 Future Improvements

* [ ] Login system
* [ ] Question categories
* [ ] Difficulty levels
* [ ] Randomized quizzes
* [ ] Timer support
* [ ] Statistics dashboard
* [ ] Export results
* [ ] JSON import/export
* [ ] PostgreSQL support
* [ ] Web version (Flask/FastAPI)
* [ ] REST API
* [ ] Docker support

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve this project:

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

# 📜 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute it according to the license terms.

---

# 👨‍💻 Author

**Artin MoeinPour**

GitHub:

https://github.com/artinpy

---

<p align="center">

⭐ If you found this project useful, consider giving it a star!

</p>
