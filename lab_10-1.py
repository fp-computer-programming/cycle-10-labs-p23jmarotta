# creator JM 1/20/23

sum = 0

while True:
    num = int(input('please give number: '))
    if num == -1:
        print(sum)
        break
    sum += num