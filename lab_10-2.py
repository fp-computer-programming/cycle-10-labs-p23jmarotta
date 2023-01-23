# Creator JM 1/20/2023

listy = []

while True:
    num = int(input('number please: '))
    if num%3 == 1:
        continue
    elif num == -1:
        print(listy)
        break
    else:
        listy.append(num)