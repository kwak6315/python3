#반복제어문1 - 자가진단6 633

while True:
    print("1.korea \n2. USA \n3. Japan \n.4. china")
    a = int(input("number? "))
    if a == 1:
        print("\nSeoul\n")
    elif a == 2:
        print("\nWashington\n")
    elif a == 3:
        print("\nTokyo\n")
    elif a == 4:
        print("\nBeijing\n")
    else:
        print("none")
        break