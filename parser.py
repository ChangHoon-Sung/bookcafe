#-*- coding:utf-8 -*-

import requests, json
import info

class ISBN_Parser:
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    URL = "http://seoji.nl.go.kr/landingPage/SearchAjax.do"

    def __init__(self):
        self.book = dict()

    def parse_bookinfo(self, isbn):
        self.isbn = isbn
        data = 'start=0&tSrch_isbn=' + isbn + '&fq_select=tSrch_isbn&q=' + isbn

        res = requests.post(self.URL, headers = self.headers, data=data)
        
        try:
            if(res.status_code != 200):
                raise RuntimeError
            else:
                res = json.loads(res.text)['response']['docs'][0]
        except:
            print("파싱 중 에러 발생!")
            return False

        # AUTHOR의 Value 예 -> '지은이(저자): 테드 창; 역자(옮긴이) 김상훈;'
        # 추출할 작가 이름 테드 창
        #sep1 = res['AUTHOR'].find(':')
        #sep2 = res['AUTHOR'].find(';')
        
        self.book = {
            '제목' : res['TITLE'],
            '저자' : res['AUTHOR'],
            '분류' : info.CATEGORY[res['EA_ADD_CODE'][2]],
            '출판사' : res['PUBLISHER'],
            '발행일' : res['PUBLISH_PREDATE'],
            #'대상' : info.READER[res['EA_ADD_CODE'][0]],
            'ISBN' : res['EA_ISBN']
        }
        
      
      
    
        return self.book

if __name__ == "__main__":
    p = ISBN_Parser()
    for n in ('9788934998952', '9791164050444'):
        b = p.parse_bookinfo(n)
        for k, v in b.items():
            print(k, v)
        print()
