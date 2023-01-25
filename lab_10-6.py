# Creator JM 1/25/23

def add_nums(numbers):
    n = input('Input a number: ')
    try:
        for i,v in enumerate(numbers):
            numbers[i] += int(n)
    except:
        print('Sorry, you need to put a valid number.')
    finally:
        print(f'Passed list: {numbers}; User input: {n}')


# User input = 1
add_nums([0,1,2]) # Result = "Passed list: [1, 2, 3]; User input: 1"

# User input = 'one'
add_nums([0,1,2]) # Result = "Sorry, you need to input a valid number" "Passed list: [0, 1, 2]; User input: one"

# User input = 200
add_nums([0,1,2]) # Result = "Passed list: [200, 201, 202]; User input: 200"
