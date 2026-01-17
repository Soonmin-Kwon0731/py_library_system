class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def show_info(self):
        print(f"회원명: {self.name} (ID: {self.member_id})")
        print(f"대출목록 : ", end='')

        if not self.borrowed_books:
            print("없음.")
        else:
            for book in self.borrowed_books:
                print(f'{book.title}',end='')

    