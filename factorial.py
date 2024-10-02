# factorial.py
"""Factorial.py"""
import time

final_list = []

def factorial(n):
    """Find Factorial"""
    time.sleep(.1)
    factorial_num = 1
    for i in range (1,n+1):
        factorial_num = factorial_num * i
    return factorial_num

def sum_factorial():
    """Sum Factorial"""
    for i in range(50):
        final_list.append(factorial(i))
    result=sum(final_list)
    print(f"FINAL_SUM = {result}")
    return result

if __name__ == "__main__":
    sum_factorial()

FINAL_SUM = 620960027832821612639424806694551108812720525606160920420940314
