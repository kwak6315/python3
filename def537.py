#반복제어문1- 자가진단 2 537

user = int(input("100이하의 양의 정수만 입력하세요>>  "))
while user > 100:
    user = int(input("100이하의 양의 정수만 다시 입력하세요>>  "))
i = 0
sum = 0
while i <= user:
    i += 1
    sum += i
print("숫자의 총합은 {}입니다.".format(sum))

