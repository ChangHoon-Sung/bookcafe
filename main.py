import csv, shutil
import local, remote
from parser import Book_Parser

# local = 1, remote = 2
WORKSPACE = 2

def set_workspace():
    global WORKSPACE
    check = '✔'

    print("작업 환경을 설정합니다.")
    print("1. [%c] 로컬PC (기본값) " % (check if WORKSPACE == 1 else ' '))
    print("2. [%c] 구글 스프레드시트(온라인)" % (check if WORKSPACE == 2 else ' '))

    while(True):
        print("선택 > ", end = '')
        try:
            value = int(input())
            if(not(1 <= value <= 2)):
                raise Exception
        except:
            print("<< 잘못된 입력입니다 >>\n")
        else:
            WORKSPACE = value
            break

def set_worker():
    global WORKSPACE
    if WORKSPACE == 1:
        return local.worker()
    else:
        return remote.worker()

# Main
def main():
    p = Book_Parser()
    worker = remote.worker()

    while(True):
        print("\n~ Book 관리 프로그램 ~")
        print("1. 도서 추가")
        print("2. DB 출력")
        print("3. 백업 생성")
        print("4. 작업 환경 설정")
        print("5. 종료")
        print(">> ", end='')

        try:
            sel = int(input())
            print()
        except:
            print("<< 잘못된 입력입니다. >>")
            continue
        if sel == 1:
            worker.add_book(p)
        elif sel == 2:
            worker.print_book()
        elif sel == 3:
            worker.make_backup()
        elif sel == 4:
            set_workspace()
            worker = set_worker()
            print("<< 설정이 완료되었습니다 >>\n")
        elif sel == 5:
            print("<< 종료합니다 >>")
            break
        else:
            print("<< 메뉴에 없는 선택지 >>")


main()