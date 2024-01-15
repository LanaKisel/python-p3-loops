#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    n = 11
    while n>0:
        n -= 1
        print(f"{n}")
    print("Happy New Year!")     
    pass

def square_integers(int_list):
    # code goes here!
    # int_list = list()
    # for number in int_list:
    #     squere_number = number ** 2
    #     int_list.append(squere_number)
    pass
    int_list = [num ** 2 for num in int_list]
    return int_list

def fizzbuzz():
    # code goes here!
    n = 1
    while n < 101:
        if (n % 3 == 0 and n % 5 == 0):
            print("FizzBuzz")
        elif (n % 3 == 0):
            print("Fizz")
        elif (n % 5 == 0):
            print("Buzz")    
        else:
            print(f"{n}")
        n += 1   
    pass
