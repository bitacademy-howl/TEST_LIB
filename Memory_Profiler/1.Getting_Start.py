# -*- coding  :  utf-8 -*-
# # install   :  pip install -U memory_profiler
# # usage     :  python -m memory_profiler Memory_Profiler/1.Getting_Start.py


@profile
def Fibonacci_Recursion(val):
    if (val == 1):
        return 0
    elif (val == 2):
        return 1
    else:
        return Fibonacci_Recursion(val - 1) + Fibonacci_Recursion(val - 2)


@profile
def Fibonacci_Repeat(val):
    val_1 = 0
    val_2 = 1
    val_3 = 0
    temp = 0

    if (val == 0):
        return 0
    elif (val == 1):
        return 1
    else:
        for i in range(0, val):
            temp = val_2
            val_2 = val_1 + val_2
            val_1 = temp

        return val_2


@profile
def TEST():
    recursion = 0
    repeat = 0

    recursion = Fibonacci_Recursion(20)
    repeat = Fibonacci_Repeat(20)

    print(recursion, repeat)


if __name__ == "__main__":
    TEST()