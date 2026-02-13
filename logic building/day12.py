#08/01/26
# Datatype Counter (Logic + Datatype)
# data = [10, "hi", 2.5, "7", False, "python", 3]
# count_int = 0
# count_str = 0
# count_others = 0
# for i in data:
#     if type(i) == int and i is not False:
#         count_int += 1
#     elif type(i) == str:
#         count_str += 1
#     else:
#         count_others += 1
# print(count_int)
# print(count_str)
# print(count_others)
from subprocess import check_output


# Function: Count Digits
# def count_digit(x):
#     count = 0
#     for i in x:
#         if i.isdigit():
#             count += 1
#     return count
# print(count_digit("a1b2c3v7"))


# def is_upper(ch):
#     if ch.isupper():
#         return True
#     else:
#         return False
# def count_upper(s):
#     count = 0
#     for i in s:
#         if is_upper(i):
#             count += 1
#     return count
# print(count_upper("AbcDEfghI"))


# def is_multiple_of_5(n):
#     if n % 5 == 0:
#         return True
#     else:
#         return False
#
# def print_multiples(x):
#     for i in x:
#         if is_multiple_of_5(i):
#             print(i)
# print(print_multiples([1,2,3,4,5,10,15]))


# def is_digit(ch):
#     if ch.isdigit():
#         return True
#     else:
#         return False
# def count_digit_until_letters(s):
#     count = 0
#     for i in s:
#         if is_digit(i):
#             count += 1
#         else:
#             break
#     return count
# print(count_digit_until_letters("129abcd"))

# def is_even(s):
#     if s % 2 == 0:
#         return True
#     else:
#         return False
# def count_is_even(x):
#     count = 0
#     for i in x:
#         if is_even(i):
#             count += 1
#     return count
# print(count_is_even(range(1,21)))


def is_vowel(ch):
    vowels = "aeiouAEIOU"
    if ch in vowels:
        return True
    else:
        return False

def print_until_vowels(s):
    for i in s:
        if is_vowel(i):
            break
        print(i)
print(print_until_vowels("shshdamar"))







