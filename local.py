import os, shutil
import csv
import datetime

class worker():
    FILEPATH = os.getcwd() + '/YJ_Book.csv'

    def make_backup(self):
        today = datetime.datetime.now()
        filename = FILEPATH[:-4]+today.strftime('%Y-%m-%d %H:%M')+'.csv'

        try:
            shutil.copy2(FILEPATH, filename)
        except FileNotFoundError:
            print("백업 생성 실패!")
            print("백업할 파일이 없습니다.")
        except:
            print("알 수 없는 오류 발생!")
        else:
            print("백업 파일이 생성되었습니다.")
            print(filename)

    def print_book(self):
        with open(FILEPATH, 'r') as fr:
            reader = csv.reader(fr)
            for line in reader:
                print(line)

    def add_book(self, parser):   
        b = parser.get_bookinfo()
        if b:
            new_book = [v for v in b.values()]

            with open(FILEPATH, 'a') as fw:
                writer = csv.writer(fw)
                writer.writerow(new_book)
            
            print("\n새로운 책이 추가되었습니다.")
            print("내용을 확인하세요.")

            print(new_book)
        else:
            print("추가 취소")
