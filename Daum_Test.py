
from selenium import webdriver
import pyautogui
import time

#프로세스 시작 알림
start_time = time.time()
print("Process Start")


#크롬드라이버 실행
driver = webdriver.Chrome('chromedriver')

#url입력 후 창 최대화
driver.get(url='https://www.daum.net/')
driver.maximize_window()
time.sleep(3)


#element(로그인버튼) 클릭
#참고 : 다음로그인박스 인식 안돼서, 다음로고 버튼 클릭하게 적용하였음.
driver.find_element_by_class_name('ico_daum').click()


#타이틀명으로 구분
title_name = driver.title
print(title_name)
if title_name == "Daum 로그인":
    assert True
    print("First : Pass")
else:
    assert False
    print("First : Fail")

#미리저장한 아이디, 패스워드를 입력
id = '<아이디>'
pw = '<비밀번호>'

driver.find_element_by_id('id'). send_keys(id)
time.sleep(1.5)
driver.find_element_by_id('inputPwd'). send_keys(pw)
time.sleep(1.5)

#로그인 버튼 클릭
driver.find_element_by_class_name('btn_comm').click()

#정상로그인 여부
title_name2 = driver.title
print(title_name2)
if title_name2 == "Daum":
    assert True
    print("Second : Pass")
else :
    assert False
    print("second : Fail")



#프로세스 종료 및 실행시간 표시
end_time = time.time()
print("Process End")
print("수행시간 : " + str(end_time - start_time) + " seconds")

#실행시간 표시 메세지박스
pyautogui.alert(title = '알림', text = "수행시간 : " + str(end_time - start_time) + " seconds", button='OK')
