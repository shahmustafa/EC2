# def sumList(lst):
#     if len(lst) == 1:
#         return lst[0]
#     return lst[0] + sumList(lst[1:])
#
# print(sumList([1,2,3,4]))

# def power(base, n):
#     if n == 1:
#         return n
#     return base * pow(base, n-1)
#
#
# print(power(8, 3))


def feebonic(integer, nth):
    if nth == 0:
        return
    return integer + feebonic(integer, nth-1)


print(feebonic(3, 4))