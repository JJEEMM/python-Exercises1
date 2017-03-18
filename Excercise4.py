__author__ = 'Justin'

"""
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which
contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""

str_in = input("Enter a list of , numbers: ")
list_in = str_in.split(",")
tup_in = tuple(list_in)
print(list_in)
print(tup_in)

"""
values=raw_input()
l=values.split(",")
t=tuple(l)
print l
print t
"""