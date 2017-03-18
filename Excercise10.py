__author__ = 'Justin'

"""
Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all
duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""

sen_in = input("Enter a sentence: ").split(" ")
sen_in.sort()
for i in range(len(sen_in) - 1, 0, -1):
    if sen_in[i] == sen_in[i - 1]:
        sen_in.remove(sen_in[i - 1])

print(" ".join(sen_in))

"""
s = raw_input()
words = [word for word in s.split(" ")]
print " ".join(sorted(list(set(words))))
"""