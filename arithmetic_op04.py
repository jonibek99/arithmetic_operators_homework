#Create a variable called 'number' and assign it the three-digit number.

#Find the 'number' first digit and assign to x1.

#Find the 'number' second digit and assign to x2.

#Find the 'number' third digit and assign to x3.

#Create a variable called 'answer' and assign it the sum of the three digits x1, x2, x3.

#Print the value of the 'answer.
number=432
x1=int(str(number)[1])
x2=int(str(number)[2])
x3=int(str(number)[-1])
answer=x1+x2+x3
print(answer)