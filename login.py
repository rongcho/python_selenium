
#크롬드라이버 실행하여 사이트 자동로그인

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import time


# 사이트의 로그인 페이지 주소저장 (원하는 사이트 경로 저장하면 됨)
    "daum": "https://logins.daum.net/accounts/signinform.do"
    "naver" : "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"



class LoginBot:
    def __init__(self, site):
        # 웹드라이버에 입력할 옵션지정
        self.options = Options()
        # 옵션에 해상도 입력
        self.options.add_argument("--window-size=1700,1000")
        # 크롬 웹드라이버를 로드
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)
        # 사이트로 이동하여 로그인 시도
        try:
            self.driver.get(LOGIN_URLS[site.lower()])
            # 페이지 이동 대기
            time.sleep(3)
        except KeyError:
            # 저장되지 않은 주소는, 주소를 기재해야 함
            self.driver.get(site)
            # 로딩 대기
            time.sleep(3)


    def kill(self):
        self.driver.quit()  #크롤러 종료





        


