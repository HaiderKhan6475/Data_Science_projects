🚀 Library Book Management System

A Python-based console project to manage library books, track issued copies, and calculate availability.






📌 Project Overview

This Library Book Management System allows users to manage a collection of books. It tracks the total copies, issued copies, and determines availability. The system also calculates total issued books, total available books, and identifies the most issued book.

🎯 Key Features

Book Management: Add multiple books with author, copies, and issued copies.

Availability Status: Automatically determines if a book is Available or Not Available.

Dictionary Storage: Stores book data in a structured dictionary for easy access.

Issue Tracking: Keeps count of total issued books and most issued book.

Console-based: Lightweight and easy to run in terminal or IDE.

🛠 Tech Stack

Language: Python 3.x

Version Control: Git & GitHub

Development Environment: PyCharm / VSCode / Jupyter

📂 Repository Structure
Library-Book-Management-System/
├── .gitignore                  <-- (Excludes .idea, __pycache__, etc.)
├── README.md                   <-- (Project Documentation)
└── Library_Management/
    └── Library_Management.py   <-- (Core Python Script)
▶️ How the Script Works
Step 1 — Enter Book Details

User inputs the number of books, and for each book:

Name

Author

Number of copies

Number of issued copies

Step 2 — Determine Availability

If issued copies = total copies → Not Available
Else → Available

Step 3 — Store Data

Each book’s details are stored in a dictionary:

{
 "Python": {"Author":"John", "Copies":5, "Issued_copies":3, "Status":"Available"}
}
Step 4 — Calculate Totals

Total issued books

Total available books

Most issued book

📊 Example Output
Enter the number of books: 2
Enter the name of book: Python
Enter the author : John
Enter the num of copies: 5
Enter the number of copies issued: 3
Enter the name of book: Java
Enter the author : Alice
Enter the num of copies: 3
Enter the number of copies issued: 3

Library Data:
{'Python': {'Name': 'Python', 'Author': 'John', 'Copies': 5, 'Issued_copies': 3, 'Status': 'Available'},
 'Java': {'Name': 'Java', 'Author': 'Alice', 'Copies': 3, 'Issued_copies': 3, 'Status': 'Not Available'}}

Total issued books: 6
Total available books: 2
Most issued book: Python
🎓 Learning Outcomes

By building this project, you will learn:

Python dictionaries and data structures

Loops and conditional logic

Tracking counts and statuses

Basic project organization and documentation

👨‍💻 Author

Haider Khan
GitHub: https://github.com/HaiderKhan6475

⭐ If you find this project useful, consider giving it a star on GitHub!