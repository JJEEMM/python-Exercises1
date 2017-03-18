__author__ = 'Justin'

"""
Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""

in_list = input("Enter , words: ").split(",")

num_iter = len(in_list)
out_list = []

for i in range(num_iter):
    out_list.append(min(in_list))
    in_list.remove(min(in_list))

print(",".join(out_list))

"""
items=[x for x in raw_input().split(',')]
items.sort()
print ','.join(items)
"""