def countdown(n):
    if n <= 0:
        print('We are done!')
    else:
        print(n)       # print the current value of n
        n = n - 1      # subtract 1 from n
        countdown(n)   # call the same function with the new value of n.

def countdown_while(n):
    while n > 0:
        print(n)
        n = n - 1

def countup(n):
    while n < 0:
        print(n)
        n = n + 1


def countup_recursive(n):
    if n >= 0:
        print("We are done!")
    else:
        print(n)
        n = n + 1
        countup_recursive(n)

#countdown(10)
#countup(-10)




#   n! = n x (n-1)!
#   1! = 1
#   0! = 1
#   factorial(n) = n x factorial(n-1)
#                = n x (n-1) x factorial(n-2)
#                = n x (n-1) x (n-2) x factorial(n-3)
# ...
#                = n x (n-1) x (n-2) x (n-3) x ... x factorial(1)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# for n = 2
# return 2 * factorial(1)
# return 2 * 1


# for n = 3
# return 3 * factorial(2)
# return 3 * (return 2 * factorial(1))
# return 3 * 2 * 1
# 6

#print(factorial(10))


