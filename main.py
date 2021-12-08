
"""
1. Update date : 21-12-07
2. login.py과 동일한 폴더에 위치시킴.
3. caps lock_대문자주의 (추후 추가예정)
"""

import sys
import time
import login as lo


#시작알림 및 시작시간 체크
print("Process Start.")
start_time = time.time()


#사이트 주소 입력받음
site = sys.argv[1]

#아이디 입력받음
id = sys.argv[2]

#패스워드 입력받음
ps = sys.argv[3]

#login.py 에서 크롤러 불러오기
crawler = lo.LoginBot(site)

#입력받은 아이디,비번을 크롤러가 입력함
crawler.login(id, pw)



#종료알림 및 총 러닝시간 확인 (윈도우박스 추후 추가예정)
print("Process Done.")
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
