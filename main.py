import csv, shutil, datetime
from parser import Book_Parser

# 파일 쓰기
fw = open('./YJ_Book.csv', 'a', encoding='euc-kr')
writer = csv.writer(fw)

# 백업
def make_backup():
    today = datetime.datetime.now()
    filename = './YJ_Book'+today.strftime('%Y-%m-%d %H:%M')+'.csv'

    try:
        shutil.copy2('./YJ_Book.csv', filename)
    except FileExistsError:
        print("백업 생성 실패!")
        print("백업할 파일이 없습니다.")
    except:
        print("알 수 없는 오류 발생!")
    else:
        print("백업 파일이 생성되었습니다.")
        print(filename)

def print_book():
    with open('./YJ_Book.csv', 'r', encoding='euc-kr') as fr:
        reader = csv.reader(fr)
        for line in reader:
            print(line)

def add_book(parser):   
    b = parser.get_bookinfo()
    if b:
        new_book = [v for v in b.values()]

        with open('./YJ_Book.csv', 'a', encoding='euc-kr') as fw:
            writer = csv.writer(fw)
            writer.writerow(new_book)
        
        print("\n새로운 책이 추가되었습니다.")
        print("내용을 확인하세요.")

        print(new_book)

# Main
def main():
    p = Book_Parser()

    while(True):
        print("\n~ Book 관리 프로그램 ~")
        print("1. 도서 추가")
        print("2. DB 출력")
        print("3. 백업 생성")
        print("4. 종료")
        print(">> ", end='')

        try:
            sel = int(input())
        except:
            print("<< 잘못된 입력입니다. >>")
            continue
        if sel == 1:
            add_book(p)
        elif sel == 2:
            print_book()
        elif sel == 3:
            make_backup()
        elif sel == 4:
            print("<< 종료합니다 >>")
            fw.close()
            break
        else:
            print("<< 메뉴에 없는 선택지 >>")


main()