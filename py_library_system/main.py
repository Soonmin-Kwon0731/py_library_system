from library_system.book import Book
from library_system.member import Member
from library_system.library import Library

def main():
    print("=== [시스템 시작] 도서관 관리 프로그램 초기화 ===")
    
    # 1. 도서관 설립
    my_lib = Library()

    # 2. 책 입고 (객체 생성)
    b1 = Book("파이썬의 정석", "978-1")
    b2 = Book("인공지능의 미래", "978-2")
    b3 = Book("해리포터와 마법사의 돌", "978-3")

    # 3. 도서관 시스템에 등록
    my_lib.add_book(b1)
    my_lib.add_book(b2)
    my_lib.add_book(b3)

    # 4. 회원 가입
    user = Member("김코딩", "User001")

    print("\n--- [시나리오 1] 정상 대출 테스트 ---")
    my_lib.borrow_book("파이썬의 정석", user)
    my_lib.borrow_book("해리포터와 마법사의 돌", user)
    
    # 확인: 회원의 가방 확인
    user.show_info()


    print("\n--- [시나리오 2] 예외 처리 테스트 (방어력 확인) ---")
    my_lib.borrow_book("파이썬의 정석", user)  # 이미 빌린 거 또 빌리기
    my_lib.borrow_book("없는 책", user)        # 없는 책 빌리기


    print("\n--- [시나리오 3] 반납 테스트 ---")
    my_lib.return_book("파이썬의 정석", user) # 정상 반납
    
    user.show_info()
    
    
    my_lib.show_all_books()

if __name__ == "__main__":
    main()