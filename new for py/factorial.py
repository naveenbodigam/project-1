for x in range(1, 11):
    factorial = 1
    num = x
    while (num>1):
        factorial = factorial*num
        num = num-1
    print('factorial of', x,'is', factorial)
