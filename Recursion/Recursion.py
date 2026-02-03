# print 1 to n number using recursion


def print_numbers(n):
    if n <= 0:
        return
    print_numbers(n - 1)
    print(n)