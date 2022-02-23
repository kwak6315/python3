#반복제어문1 - 자가진단5 540

#break - while true  무한루프 생성
num = int(input("정수를 입력하세요>>  "))

while True:
    if num % 3 != 0:
        if num == -1:
            break
        continue


    elif num % 3 == 0:
        print(num / 3)
        num = int(input("정수를 입력하세요>>  "))

    else:
        break