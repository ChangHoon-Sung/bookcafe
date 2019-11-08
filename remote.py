# -*- coding: utf-8 -*-

from httplib2 import Http
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import info


class worker:

    def __init__(self):
        # Google API 요청 시 필요한 권한 유형
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        # 구글 시트 ID
        self.SPREADSHEET_ID = info.SPREADSHEET_ID

        # json 파일로 서비스 계정 credential 정의
        credential = ServiceAccountCredentials.from_json_keyfile_name(info.KEYPATH, SCOPES)
        http_auth = credential.authorize(Http())
        self.service = build('sheets', 'v4', http=http_auth)

    def add_book(self, parser):
        while(True):
            new_book = parser.get_bookinfo()
            if new_book:
                values = [ [v for v in new_book.values()], ]
                body = {'values': values}

                # 업데이트 요청 및 실행
                request = self.service.spreadsheets().values().append(spreadsheetId=self.SPREADSHEET_ID,
                                                                range='Sheet1!A1:F1', # 2
                                                                valueInputOption='RAW',
                                                                body=body)
                request.execute()
                print("\n새로운 책이 추가되었습니다.")
                print("내용을 확인하세요.")

                print(new_book)
            else:
                break

    def print_book(self):
        import webbrowser
        URL = 'https://docs.google.com/spreadsheets/d' + self.SPREADSHEET_ID
        webbrowser.open(URL, new=2)
        print(URL)

    def make_backup(self):
        print("준비중입니다!")