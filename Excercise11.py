__author__ = 'Justin'

"""
Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether
they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
"""

in_ = input("Enter 4 bit binary by ,: ").split(",")
in_dec = []

for group in in_:
    num = 0
    for bit in range(len(group) - 1, -1, -1):
        if group[bit] == '1':
            num += 2**bit
    if num % 5 == 0:
        in_dec.append(group)

print(",".join(in_dec))

"""
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print ','.join(value)
"""