# library_system/library.py

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.title in self.books:
            print(f"오류: '{book.title}'은(는) 이미 등록된 도서입니다.")
        else:
            self.books[book.title] = book
            print(f"등록 완료: {book.title}")

    def remove_book(self, title):
        if title not in self.books:
            print(f"오류: '{title}'이라는 책은 도서관에 없습니다.")
        else:
            del self.books[title]
            print(f"삭제 완료: {title}")

    def show_all_books(self):
        print("\n=== 도서관 보유 서적 ===")
        if not self.books:
            print("보유 중인 도서가 없습니다.")
        else:
            for book in self.books.values():
                print(book) 
        print("======================\n")
    
    def borrow_book(self,book_title,member):
        if book_title not in self.books:
            print("오류: 도서관에 없는 책입니다.")
            return
        else:
            book = self.books[book_title]
            if book.is_borrowed:
                print("오류: 이미 대출중인 도서입니다.")
                return
            else:
                book.is_borrowed = True
                member.borrowed_books.append(book)
                print(f'성공: [{book_title}]이 [{member.name}]님에게 대출되었습니다.')
    
    def return_book(self,book_title,member):
        if book_title not in self.books:
            print('오류: 대여 목록에 없습니다.')
        else:
            book = self.books[book_title]
            if book not in member.borrowed_books:
                print(f'오류: [{member.name}]님은 이 책을 빌린 적이 없습니다.')
            else:
                member.borrowed_books.remove(book)
                book.is_borrowed = False
                print(f"성공: [{book_title}이 반납되었습니다.]")
