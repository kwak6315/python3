    # 반복제어문1 - 자가진단4 539

a = []
user = int(input("정수를 입력하세요 >>  "))
sum = 0
i = 0
while True :
    a.insert(i, user) #인덱스 지정, 해당 인덱스에 user 값 저장
    sum += a[i]
    if a[i] >= 100:
        break
    i += 1
    user = int(input("정수를 입력해주세요 >> "))
print(sum)
print("%.1f"%(sum/len(a))) #소수점 첫째 자리수까지 출력





