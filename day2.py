# 1. Print Numbers from 1 to n
# Question: Write a program to print numbers from 1 to n. 
# Explanation: Use a loop starting from 1 to n and 
# print each number. - Input: n = 5 - Output: 1 2 3 4 5
print('1. Print Numbers from 1 to n')
n=5
for i in range(1,n+1):
  print(i,end=' ')
print()
# 2. Print Numbers from m to n
# Question: Write a program to print numbers from m to n. Explanation:
# Loop from m to n and print values. 
# - Input: m = 3, n = 7 - Output: 3 4 5 6 7
print('2. Print Numbers from m to n')
m=3
n=7
for i in range(m,n+1):
  print(i)
print('3. Print Numbers from n to 1 in Reverse')
# 3. Print Numbers from n to 1 in Reverse
# Question: Write a program to print numbers in reverse
# from n to 1. Explanation: Use a loop starting from n and decrement to 1.
# -Input: n = 5 - Output: 5 4 3 2 1
num=5
for i in range(num,0,-1):
  print(i)
# 4. Print Numbers from n to m in Reverse
# Question: Write a program to print numbers from n to m in reverse.
# Explanation: Start from n and go down to m. - Input: n = 10, m = 6 
# - Output: 10 9 8 7 6
print('4. Print Numbers from n to m in Reverse')
n=10
m=6
for i in range(n,m-1,-1):
  print(i)
# 5. Sum of n Natural Numbers
# Question: Write a program to calculate the sum of first n
# natural numbers. Explanation: Use formula or loop to sum from 1 to n.
# - Input: n = 5 - Output: 15
print('5. Sum of n Natural Numbers')
n=5
sum=0
for i in range(n+1):
  sum+=i
print(sum)
# 6. Factorial of a Number
# Question: Write a program to find the factorial of a number. 
# Explanation: Multiply all numbers from 1 to n. 
# - Input: n = 5 - Output: 120
print('6. Factorial of a Number')
n=5
fact=1
for i in range(1,n+1):
  fact*=i
print(fact)
# 7. Sum of m to n Numbers
# Question: Write a program to find the sum of all numbers from m to n.
# Explanation: Loop from m to n and add values. -
# Input: m = 3, n = 6 - Output: 18
print('7. Sum of m to n Numbers')
m=3
n=6
sum=0
for i in range(m,n+1):
  sum+=i
print(sum)
# 8. Product of m to n Numbers
# Question: Write a program to find the product of numbers from m to n.
# Explanation: Loop from m to n and multiply values. 
# - Input: m = 2, n = 4 - Output: 24
print('8. Product of m to n Numbers')
m=2
n=4
product=1
for i in range(m,n+1):
  product*=i
print(product)
# 9. Print Factors of a Number
# Question: Write a program to print all factors of a given number. 
# Explanation: Check divisibility of number from 1 to n.
# - Input: n = 6 - Output: 1 2 3 6
print('9. Print Factors of a Number')
n=6
for i in range(1,n+1):
  if n%i==0:
    print(i)
# 10. Count of Factors
# Question: Write a program to count how many factors a number has.
# Explanation: Increment count when divisible. 
# - Input: n = 6 - Output: 4
print('10. Count of Factors')
n=6
count=0
for i in range(1,n+1):
  if n%i==0:
    count+=1
print(count)
# 11. Prime Number Check
# Question: Check if a number is prime. 
# Explanation: A number is prime if it has exactly 2 factors.
# - Input: n = 7 - Output: Prime
print('11. Prime Number Check')
n=7
is_prime=True
for i in range(2,n):
  if n%i==0:
    is_prime=False
    break
if is_prime:
  print('prime')
else:
  print('not prime')
# 12. Even Numbers from m to n
# Question: Print all even numbers between m and n.
# Explanation: Use loop and check if divisible by 2.
# - Input: m = 3, n = 10 - Output: 4 6 8 10
print('12. Even Numbers from m to n')
m=3
n=10
for i in range(m,n+1):
  if(i&1==0):
    print(i)
# 13. Odd Numbers from m to n
# Question: Print all odd numbers between m and n. 
# Explanation: Check if number % 2 != 0. 
# - Input: m = 3, n = 10 - Output: 3 5 7 9
print('13. Odd Numbers from m to n')
m=3
n=10
for i in range(m,n+1):
  if(i&1==1):
    print(i)
# 14. Count of Even and Odd Numbers
# Question: Count how many even and odd numbers are 
# in the range m to n. Explanation: Use counters for even and odd. 
# - Input: m = 3, n = 7 - Output: Even = 2, Odd = 3
print('14. Count of Even and Odd Numbers')
m=3
n=7
even=0
odd=0
for i in range(m,n+1):
  if(i%2==0):
    even+=1
  else:
    odd+=1
print('EVEN=',even,'ODD=',odd)
# 15. Reverse a String
# Question: Reverse a given string. Explanation:
# Use slicing or loop. - Input: “hello” - Output: “olleh”
print('15. Reverse a String')
word='hello'
rev=''
for i in word:
  rev=i+rev
print(rev)
# 16. Check for Palindrome String
# Question: Check if a string is a palindrome. 
# Explanation: Compare string with its reverse. - Input: “madam” 
# - Output: Palindrome
print('16. Check for Palindrome String')
word='madam'
rev=''
for i in word:
  rev=i+rev
if rev==word:
  print('palindrome')
else:
  print('not palindrome')
# 17. Sum of Digits
# Question: Calculate the sum of digits of a number.
# Explanation: Use loop and % 10 to extract digits.
# - Input: 123 - Output: 6
print('17. Sum of Digits')
num=123
total=0
while num>0:
  dig=num%10
  total+=dig
  num//=10
print(total)
# 18. Product of Digits
# Question: Calculate the product of digits.
#  Explanation: Multiply digits extracted from number.
# - Input: 123 - Output: 6
print('18. Product of Digits')
num=123
product=1
while num>0:
  dig=num%10
  product*=dig
  num//=10
print(product)
# 19. Armstrong Number Check
# Question: Check if a number is an Armstrong number. 
# Explanation: Sum of cube of digits equals the number.
# - Input: 153 - Output: Armstrong number
print('19. Armstrong Number Check')
number=153
temp=number
l=len(str(number))
total=0
while number>0:
  dig=number%10
  total+=dig**l
  number//=10
if total==temp:
  print('Armstrong number')
else:
  print('Not Armstrong number')
# 20. Reverse a Number
# Question: Reverse the digits of a number.
# Explanation: Use loop with % and // to reverse.
#  - Input: 123 - Output: 321
print('20. Reverse a Number')
n=123
rev=0
while n>0:
  dig=n%10
  rev=rev*10+dig
  n//=10
print(rev)
# 21. Palindrome Number Check
# Question: Check if a number is a palindrome.
# Explanation: Compare number with its reverse.
# - Input: 121 - Output: Palindrome
print('21. Palindrome Number Check')
n=121
temp=n
rev=0
while n>0:
  dig=n%10
  rev=rev*10+dig
  n//=10
if temp==rev:
  print('Palindrome')
else:
  print('Not Palindrome')
# 22. Count Vowels in String
# Question: Count number of vowels in a string.
# Explanation: Loop and check for a, e, i, o, u. 
# - Input: “apple” - Output: 2
print('22. Count Vowels in String')
word='apple'
count=0
for ch in word:
  if ch in 'aeiouAEIOU':
    count+=1
print(count)
# 23. Count Consonants in String
# Question: Count consonants in a string. 
# Explanation: Check for alphabetic characters not vowels.
#  - Input: “apple” - Output: 3
print('23. Count Consonants in String')
word='apple'
count=0
for ch in word:
  if ch not in 'aeiouAEIOU':
    count+=1
print(count)
# 24. Count Vowels and Consonants
# Question: Count vowels and consonants in input string. 
# Explanation: Maintain two counters.
# - Input: “apple” - Output: Vowels = 2, Consonants = 3
print('24. Count Vowels and Consonants')
word='apple'
Consonants=0
Vowels=0
for ch in word:
  if ch not in 'aeiouAEIOU':
    Consonants+=1
  else:
    Vowels+=1
print('Vowels',Vowels,'Consonants',Consonants)
# 25. Perfect Number Check
# Question: Check if a number is perfect. 
# Explanation: Sum of proper divisors equals the number. 
# - Input: 28 - Output: Perfect number
print(' 25. Perfect Number Check')
n=28
sum=0
for i in range(1,n):
  if n%i==0:
    sum+=i
if sum==n:
  print('Perfect number')
else:
  print('not perfect number')
# 26. Neon Number Check
# Question: Check if a number is a neon number. 
# Explanation: Square the number, sum digits, match original.
# - Input: 9 - Output: Neon number
print('26. Neon Number Check')
n=9
total=0
square=n*n
while square>0:
  dig=square%10
  total+=dig
  square//=10
if(n==total):
  print('Neon')
else:
  print('not Neon')
# 27. Strong Number Check
# Question: Check if a number is a strong number.
# Explanation: Sum of factorial of digits equals the number. 
# - Input: 145 - Output: Strong number
print('27. Strong Number Check')
import math
n=145
temp=n
fact=1
sum=0
while n>0:
  dig=n%10
  sum+=math.factorial(dig)
  n//=10
if sum==temp:
  print('Strong Number')
else:
  print('Not Strong Number')
# 28. Harshad Number Check
# Question: Check if a number is divisible by the sum of its digits.
# Explanation: Calculate digit sum and check divisibility. 
# - Input: 18 - Output: Harshad number
print('28. Harshad Number Check')
n=18
Sum=0
while n>0:
  Sum+=n%10
  n//=10
if n%Sum==0:
  print('Harshad Number')
else:
  print('Not Harshad Number')
# 29. Fibonacci Series
# Question: Print the Fibonacci series up to n terms.
# Explanation: Start with 0, 1 and continue with sum of last two.
#  - Input: n = 5 - Output: 0 1 1 2 3
print('29. Fibonacci Series')
n=5
a=0
b=1
for i in range(n):
  print(a,end=' ')
  a,b=b,a+b
# 30. Check for Neon Number (Repeated)
# Question: Again, check for a neon number (example). 
# Explanation: Square number and sum digits. 
# - Input: 9 - Output: Neon number
print(' 30. Check for Neon Number (Repeated)')


