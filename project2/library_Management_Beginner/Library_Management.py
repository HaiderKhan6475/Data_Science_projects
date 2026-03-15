"""Task #03: Library Book Management System

Scenario:
a. Take number of books

b. For each book input:
Book Name
Author
Number of copies
Number of issued copies

c. Determine availability:
If issued == copies → "Not Available"
Else → "Available"

d. Store in dictionary:
{
 "Python": {"author":"John", "copies":5, "issued":3, "status":"Available"}
}

e. Store issued count in list

f. Find:
Total issued books
Total available books
Most issued book"""

num_of_books = int(input("Enter the number of books:"))

data = {}
books_list = []
total_issued = 0

for books in range(num_of_books):

    name = input("Enter the name of book:")
    author = input("Enter the author :")
    copies = int(input("Enter the num of copies:"))
    issued_copies = int(input("Enter the number of copies issued:"))

    if issued_copies == copies:
        status = "Not Available"
    else:
        status = "Available"

    books_info = {
        "Name": name,
        "Author": author,
        "Copies": copies,
        "Issued_copies": issued_copies,
        "Status": status
    }

    data[name] = books_info

    books_list.append(issued_copies)

    total_issued += issued_copies


# Total available books
total_available = sum(data[book]["Copies"] - data[book]["Issued_copies"] for book in data)


# Most issued book
max_issued = 0
most_issued_book = ""

for book in data:

    if data[book]["Issued_copies"] > max_issued:

        max_issued = data[book]["Issued_copies"]

        most_issued_book = book


print("\nLibrary Data:")
print(data)

print("\nTotal issued books:", total_issued)

print("Total available books:", total_available)

print("Most issued book:", most_issued_book)