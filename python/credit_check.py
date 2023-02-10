import functools

def credit_check(str):
    my_string = list(str)
    my_numbers = list(map(lambda item : int(item), my_string))

    for i in range(0, len(my_numbers), 2):
        my_numbers[i] *= 2

   
    digits = []
    for elem in my_numbers:
        # print(type(my_numbers[j]))
        if elem > 9: 
            digits.append(elem-9)
        else:
            digits.append(elem)
            # two_digits = list(str(my_numbers[j]))
            # print(two_digits)
            # sum = int(two_digits[0]) + int(two_digits[1])
            # print(two_digits)

    # sumOfNums = sum(digits)
    sumOfNums = functools.reduce(lambda aggregateVariable, item: aggregateVariable + item, digits)

    if sumOfNums % 10 == 0:
        return "The number is valid!"
    else:
        return "The number is invalid!"

   

# print(credit_check('5541808923795240'))
