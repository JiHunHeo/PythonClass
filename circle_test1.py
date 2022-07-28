# circle_test1.py

import circle

def sub_function():
    print("하하하하하하 수정된 내용이지롱")

def main():
    r = float(input("반지름 입력: "))
    ar = circle.ar_circle(r)
    print("넓이:", ar)
    ci = circle.ci_circle(r)
    print("둘레:", ci)

main()
