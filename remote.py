# -*- coding: utf-8 -*-

from httplib2 import Http
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import info


class worker:

    def __init__(self):
        # Google API 요청 시 필요한 권한 유형
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        # 구글 시트 ID 설정
        if not info.SPREADSHEET_ID:
            print("\n스프레드 시트 ID를 입력하세요.")
            print("예시) https://docs.google.com/spreadsheets/d/spreadsheetId(이 부분)/edit#gid=0")
            self.SPREADSHEET_ID = input("ID > ")
        else:
            self.SPREADSHEET_ID = info.SPREADSHEET_ID

        # 작업 시트 이름 설정
        if not info.SHEETNAME:
            print("\n시트 이름을 입력하세요.")
            self.SHEETNAME = input("시트 이름 > ")
        else:
            self.SHEETNAME = info.SHEETNAME

        # 서비스 계정 키 경로 설정
        if not info.KEYPATH:
            print("\n서비스 계정 키의 전체 경로를 입력하세요.")
            self.KEYPATH = input("경로 > ")
        else:
            self.KEYPATH = info.KEYPATH

        # json 파일로 서비스 계정 credential 정의
        try:
            credential = ServiceAccountCredentials.from_json_keyfile_name(self.KEYPATH, SCOPES)
        except Exception as e:
            print("key 오류!", e)
        else:
            http_auth = credential.authorize(Http())
            self.service = build('sheets', 'v4', http=http_auth)
            print("<< 구글 서버와 성공적으로 연결되었습니다. >>")

    def add_book(self, parser):
        while(True):
            new_book = parser.get_bookinfo()
            if new_book:
                values = [ [v for v in new_book.values()], ]
                body = {'values': values}

                # 업데이트 요청 및 실행
                request = self.service.spreadsheets().values().append(spreadsheetId=self.SPREADSHEET_ID,
                                                                range=self.SHEETNAME + '!A1:F1', # 2
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