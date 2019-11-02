import csv, shutil, datetime
from parser import ISBN_Parser

# 백업
today = datetime.datetime.now()
shutil.copy2('./YJ_Book.csv', './YJ_Book'+today.strftime('%Y-%m-%d %H:%M')+'.csv')


# 파일 쓰기
fw = open('./YJ_Book.csv', 'a', encoding='euc-kr')
writer = csv.writer(fw)

def print_book():
    with open('./YJ_Book.csv', 'r', encoding='euc-kr') as fr:
        reader = csv.reader(fr)
        for line in reader:
            print(line)

def add_book(p):
    print("도서 ISBN을 입력하세요.")
    print(">> ", end='')

    b = p.parse_bookinfo(input())
    new_book = [v for v in b.values()]

    with open('./YJ_Book.csv', 'a', encoding='euc-kr') as fw:
        writer = csv.writer(fw)
        writer.writerow(new_book)
    
    print("\n새로운 책이 추가되었습니다.")
    print("내용을 확인하세요.")

    print(new_book)

# Main
def main():
    ps = ISBN_Parser()
    sel = 1
    while(sel is not 3):
        print("~ Book 관리 프로그램 ~")
        print("1. 책 추가")
        print("2. DB 출력")
        print("3. 종료")
        print(">> ", end='')

        sel = int(input())
        if sel == 1:
            add_book(ps)
        elif sel == 2:
            print_book()
        elif sel == 3:
            print("<< 종료합니다 >>\n")
            fw.close();
            break
        else:
            print("<< 메뉴에 없는 선택지 >>\n")
        print('\n')


main()