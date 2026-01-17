class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        status = "대출중" if self.is_borrowed else "대출가능"
        return f"[{status}] {self.title} (ISBN: {self.isbn})"