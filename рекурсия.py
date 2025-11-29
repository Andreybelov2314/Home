

def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(string) < 1:
        return ""
    rest = remove_vowels(string[1:])
    if string[0].lower() not in vowels:
        return string[0] + rest
    else:
        return rest

print(remove_vowels('apple'))




def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(9))

def rec(n):
    if n == 0:
        return []
    return rec(n-1) + [n]

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
print(factorial(6))
def sum(n):
    if n <= 1:
        return n
    else:
        return n+sum(n-1)
print(sum(5))
def sum_odd(lis):
    if len(lis) < 1:
        return 0
    else:
        if lis[-1] % 2 == 0:
            return lis[-1]
        else:
            return lis[-1] + sum_odd(lis[:-1])
print(sum_odd([1,2,3,4]))
def sum_sub(lis):
    if len(lis) < 1:
        return 0
    else:
        if lis[-1] % 2 == 0:
            return lis[-1] + sum_sub(lis[:-1])
        else:
            return -lis[-1] + sum_sub(lis[:-1])

print(sum_sub([2,4,6]))
print('-==========-')
def palindrome(n):
    if len(n) <= 1:
        return True
    else:
        if n[0] == n[-1]:
            return(n[1:-1])
        else:
            return False
print(palindrome("racecar"))  # True
print(palindrome("hello"))    # False
print(palindrome("a"))        # True
print(palindrome(""))         # True
print(palindrome("madam"))    # True



print('-=======-')
def  is_balanced(string):
    dct={'(':')', '[':']', '{':'}'}
    if len(string) < 1:
        return True
    else:
        if len(string) < 2:
            return False
        if string[0] in dct.keys():
            if dct.get(string[0]) == string[1]:
                return is_balanced(string[2:])
            else:
                return False
        else:
            return is_balanced(string[1:])
def numbers(num):
    if num <= 1:
        return num
    else:
        return str(num)+str(numbers(num-1))
print(numbers(5))
print(numbers(6))
def double(string):
    if len(string) < 1:
        return string
    else:
        result=double(string[1:])
        return string[0]*2+result
print(double('hello'))
print(double('banana'))

































