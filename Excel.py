
import win32com.client

#Dispatch 메서드
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

#해당 경로의 엑셀파일 열기
wb = excel.Workbooks.Open('C:\\Users\\bshon\\Desktop\\selenium_new\\TestData\\TestData1.xlsx')
ws = wb.ActiveSheet

#지정해준 셀을 읽어오기
print(ws.Range('A1:C5').Value)