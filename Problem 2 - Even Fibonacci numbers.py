#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#Solution 1
i = 0
a = 1
b = 2
c = 3
d = 0
answerlist = []
numbersequence = [a, b, c, d]

while d < 4000000:
    if a % 2 == 0:
        answerlist.append(a)
    if b % 2 == 0:
        answerlist.append(b)
    if c % 2 == 0:
        answerlist.append(c)
    d = c + b
    a = d
    b = d + c
    c = d + b
    i = i + 1

print(sum(answerlist))

#Answer: 4613732