import math
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver

print("---------- 출발지와 목적지 사이의 각도를 알아내는 코드입니다. ----------")
print("\n------ 이 코드를 실행하기 위해서는 Chrome 브라우저가 필요합니다. ------\n")
print("------------------- 점A(출발지)의 좌표를 입력하세요. -------------------")
x1 = float(input('x1 값을 입력하세요: '))
y1 = float(input('y1 값을 입력하세요: '))
print("------------------- 점B(목적지)의 좌표를 입력하세요. -------------------")
x2 = float(input('x2 값을 입력하세요: '))
y2 = float(input('y2 값을 입력하세요: '))

#좌표를 백터로 계산
a1 = (x2 - x1)
a2 = (y2 - y1)

#수직선의 백터 값
if a1 > -1:
    b1 = (0)
    b2 = (7) #임의 값
else:
    b1 = (0)
    b2 = (-7) #역방향 벡터의 수직선

#백터의 내적을 이용한 연산
#cos θ = a1*b1 + a2*b2 / math.sqrt(a1**2 + a2**2) * math.sqrt(b1**2 + b2**2) 
#        ->third         ->first                    ->second                   

first = (math.sqrt(a1**2 + a2**2))
second = (math.sqrt(b1**2 + b2**2))
third = (a1*b1)+(a2*b2)

# (first) X (second) = (number)
number = (first)*(second)

#cos θ(theta)
theta = (third) / (number) 

#삼각비표에서 cos 값만 추가
#각도
threef1 = (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100,
          105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180)
#해당 소수
threef2 = (1.0000, 0.9962, 0.9848, 0.9659, 0.9397, 0.9063, 0.8660, 0.8192, 0.7660, 0.7071,
           0.6428, 0.5736, 0.5000, 0.4226, 0.3420, 0.2588, 0.1736, 0.0872, 0.0000, -0.0872,
           -0.1736, -0.2588, -0.3420, -0.4226, -0.5000, -0.5736, -0.6428, -0.7071, -0.7660,
           -0.8192, -0.8660, -0.9063, -0.9397, -0.9659, -0.9848, -0.9962, -1.0000)

#θ와 가장 가까운 값 찾기
for i in range(0, 37):
    if threef2[i] < (theta):
        break
a = (threef2[i-1]) - (theta)
b = (theta) - (threef2[i])
#절댓값 만들기
a = math.sqrt(a**2)
b = math.sqrt(b**2)
#가까운 값 출력
if a > b:
    real = (threef1[i])
else:
    real = (threef1[i-1])

#Suncalc 사이트 주소 받기(시간 갱신을 안해서...)
print("\n---------------- Suncalc 사이트의 주소가 필요합니다! -----------------")
site = input("Suncalc 주소를 입력하세요: ")

#크롤러로 방위각 가져오기
driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
driver.implicitly_wait(3)

driver.get("%s" % site)
html = driver.page_source
soup = bs(html, 'html.parser')

time.sleep(5)
element = driver.find_element_by_id("azimuth")

bring = element.text
driver.close()

azimuth = ("%.3s"% bring)

#가져온 방위각에서 정수 부분만 살리기
sum = float(azimuth)

#햇빛 방위각 계산에 맞게 조절
if a1 > -1:
    realazimuth = sum
else:
    if sum > 180:
        realazimuth = sum - 180
    else:
        realazimuth = sum

    
#최종연산 & 각도 결과에 따른 화살표 표시
print("\n이 가는 방향에서 햇빛은....")
if realazimuth > real:
    result = realazimuth - real
    if 11> result > -1:
        print("↓")
    elif 80 > result > 10:
        print("↙")
    elif 101 > result > 79:
        print("←")
    elif 170 > result > 100:
        print("↖")
    elif 191 > result > 169:
        print("↑")
    elif 260 > result > 190:
        print("↗")
    elif 281 > result > 259:
        print("→")
    elif 350 > result > 280:
        print("↘")
    elif 361 > result > 349:
        print("↓")
else:
    result = real - realazimuth
    if 11> result > -1:
        print("↓")
    elif 80 > result > 10:
        print("↘")
    elif 101 > result > 79:
        print("→")
    elif 170 > result > 100:
        print("↗")
    elif 181 > result > 169:
        print("↑")

print("이 방향에서 햇빛이 오겠네요!")
