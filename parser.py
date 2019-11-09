# -*- coding:utf-8 -*-

import requests
import json
import info


class Book_Parser:
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    URL = "http://seoji.nl.go.kr/landingPage/SearchAjax.do"

    def __init__(self):
        self.book = dict()

    def parse(self, data):
        res = requests.post(self.URL, headers=self.headers,
                            data=data.encode('utf-8'))
        try:
            if(res.status_code != 200):
                raise RuntimeError
            else:
                totalCnt = json.loads(res.text)['response']['numFound']
                docs = json.loads(res.text)['response']['docs']

        except Exception as e:
            print(e)
            print("파싱 중 에러 발생!")


        print('\n\n')
        print("총 %d개의 책을 찾았습니다." % totalCnt)
        candidate = list()
        
        if(not totalCnt):
            print("<< 없거나 등록되지 않은 도서입니다. >>")

        elif(totalCnt > 21):
            print("찾는 도서가 너무 많습니다!\n수동으로 찾아주세요!")
            return dict()

        else:
            for idx in range(len(docs)):
                if not docs[idx]['EA_ADD_CODE']:
                    candidate.append(None)
                else:
                    candidate.append(docs[idx])

            print("검색 결과 상위 20개 항목을 출력합니다.\n\n")
            for idx, b in enumerate(candidate):
                print("%d)" % (idx+1))
                if b:
                    self.print_book(b)
                else:
                    print("세트 정보입니다.\n")

            print("원하는 도서의 번호를 입력해주세요.")
            print("ex)3번째 도서면 3 입력")
            print("찾는 도서가 없으면 0번을 입력하세요.")
            print("선택 > ", end = '')

            sel = int(input())

            if 1 <= sel <= len(candidate)+1:
                return self.simplify(candidate[sel-1])
            elif sel == 0:
                print("입력 취소")
            else:
                print("잘못된 입력입니다.")

        return dict()


    def print_book(self, book):
        data = [book['TITLE'], book['AUTHOR'], info.CATEGORY[book['EA_ADD_CODE'][2]],
            book['PUBLISHER'], book['PUBLISH_PREDATE'], book['EA_ISBN']]

        for s, d in zip(info.CONTENTS, data):
            print(s, d)
        print()
        
    def simplify(self, book):
        simple = {
        '제목' : book['TITLE'],
        '저자' : book['AUTHOR'],
        '분류' : info.CATEGORY[book['EA_ADD_CODE'][2]],
        '출판사' : book['PUBLISHER'],
        '발행일' : book['PUBLISH_PREDATE'],
        'ISBN' : book['EA_ISBN']
        }
        return simple
    

    def get_bookinfo(self):
        srch = list()
        for w in '제목', '저자', '출판사':
            print("\n%s을(를) 입력하세요. (0 입력시 종료)\n%s > " % (w, w), end='')
            s = input()

            if s == '0' or s == 0:
                return None
            srch.append(s)

        fq = 'TITLE_NGRAM : "' + \
            srch[0] + '" AND AUTHOR : "' + srch[1] + \
            '" AND PUBLISHER : "' + srch[2] + '"'
        data = 'start=0&rows=20&fq_select: tSrch_author&detailSearchYn=Y&fq=' + fq

        return self.parse(data)


    def get_info_by_isbn(self, isbn):
        self.isbn = isbn
        data = 'start=0&tSrch_isbn=' + isbn + \
            '&fq_select=tSrch_isbn&q=' + isbn + '&rows=30'

        return self.parse(data)


if __name__ == "__main__":
    p = Book_Parser()
    b = p.get_bookinfo()
    for k, v in b.items():
        print(k, v)
    print()

    # b = p.get_info_by_isbn('9791164357697')
    # for k, v in b.items():
    #     print(k, v)
    # print()
