# Pattern-Based Programming Questions (All 34 Questions - Interview Style)

# 🔷 Square, Rectangle, and Triangle Patterns (1–15)
# 1.Solid Square Pattern
# Problem: Print a solid square of stars of size n.
# Input: n = 4
# Output:
# * * * *
# * * * *
# * * * *
# * * * *
print(' 1.Solid Square PatternProblem: Print a solid square of stars of size n. Input: n = 4 Output:')
n=4
for i in range(n):
  stars=''
  for j in range(n):
    stars+=' *'
  print(stars)
# 2.Solid Rectangle Pattern
# Problem: Print a solid rectangle of m rows and n columns.
# Input: m = 3, n = 5
# Output:
# * * * * *
# * * * * *
print(" 2.Solid Rectangle Pattern Problem: Print a solid rectangle of m rows and n columns. Input: m = 3, n = 5")
m=3
n=5
for i in range(m):
  stars=''
  for j in range(n):
    stars+=' *'
  print(stars) 
# 3.Right-Angled Triangle (Left-Aligned)
# Problem: Print a left-aligned right-angled triangle.
# Input: n = 5
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
print("3.Right-Angled Triangle (Left-Aligned) Problem: Print a left-aligned right-angled triangle. Input: n = 5")
n=5
for i in range(n):
  stars=''
  for j in range(i+1):
    stars+=' *'
  print(stars)
# 4.Right-Angled Triangle (Right-Aligned)
# Input: n = 5
# Output:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
print('4.Right-Angled Triangle (Right-Aligned) Input: n = 5')
n=5
for i in range(n):
  stars=''
  for k in range(n-i):
    stars+='  '
  for j in range(i+1):
    stars+=' *'
  print(stars)
# 5.Inverted Triangle (Left-Aligned)
# Input: n = 5
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *
print("5.Inverted Triangle (Left-Aligned)Input: n = 5")
n=5
for i in range(n):
  stars=''
  for j in range(n-i):
    stars+=' *'
  print(stars)
# 6.Inverted Triangle (Right-Aligned)
# Input: n = 5
# Output:
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
print('6.Inverted Triangle (Right-Aligned) Input: n = 5')
n=5
for i in range(n):
  stars=''
  for k in range(i+1):
    stars+='  '
  for j in range(n-i):
    stars+=' *'
  print(stars)
# 7.Centered Pyramid Pattern
# Input: n = 4
# Output:
#       *
#     * * *
#   * * * * *
# * * * * * * *
print("7.Centered Pyramid Pattern Input: n = 4")
n=4
for i in range(n):
  stars=''
  for k in range(n-i):
    stars+='  '
  for j in range(i*2+1):
    stars+=' *'
  print(stars)
# 8.Diamond Pattern
# Input: n = 3
# Output:
#     *
#   * * *
# * * * * *
#   * * *
#     *
print("8.Diamond Pattern Input: n = 3 ")
n = 3
for i in range(n):
  stars=''
  for k in range(n-i-1):
    stars+='  '
  for j in range(2*i+1):
    stars+='* '
  print(stars)
for i in range(n-2,-1,-1):
  stars=''
  for k in range(n-i-1):
    stars+='  '
  for j in range(2*i+1):
    stars+='* '
  print(stars)
# 9.Butterfly Pattern
# Input: n = 4
# Output:
# *       *
# * *   * *
# * * * * *
# * *   * *
# *       *
print("9.Butterfly Pattern Input: n = 4")
n=4
for i in range(n-1):
  stars=''
  for j in range(i+1):
    stars+='* '
  for k in range(2*(n-i-2)):
    stars+='  '
  for j in range(i+1):
    stars+='* '
  print(stars.rstrip())
for i in range(n-2):
  stars=''
  for j in range(n-2-i):
    stars+='* '
  for k in range(2*(i+1)):
    stars+='  '
  for j in range(n-2-i):
    stars+='* '
  print(stars.rstrip())




# 10.Left-Aligned Half Diamond
# Input: n = 4
# Output:
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
print("10.Left-Aligned Half Diamond Input: n = 4")
n=4
for i in range(n):
  stars=''
  for j in range(i+1):
    stars+=' *'
  print(stars)
for i in range(n-1):
  stars=''
  for j in range(n-1-i):
    stars+=' *'
  print(stars)
# 11.Right-Aligned Half Diamond
# Input: n = 4
# Output:
#       *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *
print("11.Right-Aligned Half Diamond Input: n = 4")
n=4
for i in range(n):
  stars=''
  for k in range(2*(n-i-1)):
    stars+=' '
  for j in range(i+1):
    stars+=' *'
  print(stars)
for i in range(n-1):
  stars=''
  for k in range(2*(i+1)):
    stars+=' '
  for j in range(n-1-i):
    stars+=' *'
  print(stars)
# 12.Sandglass Pattern
# Input: n = 4
# Output:
# * * * *
#   * * *
#     * *
#       *
#     * *
#   * * *
# * * * *
print("12.Sandglass Pattern Input: n = 4")
n=4
for i in range(n):
  stars=''
  for k in range(2*(i)):
    stars+=' ' 
  for j in range(n-i):
    stars+='* '
  print(stars)
for i in range(n):
  stars=''
  for k in range(2*(n-i-1)):
    stars+=' '
  for j in range(i+1):
    stars+='* '
  print(stars)
# 13.Increasing Width Triangle
# Input: n = 5
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
print("13.Increasing Width Triangle Input: n = 5")
n=5
for i in range(n):
  stars=''
  for j in range(i+1):
    stars+='* '
  print(stars)
# 14.Decreasing Width Triangle
# Input: n = 5
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *
print('14.Decreasing Width Triangle Input: n = 5')
n=5
for i in range(n):
  stars=''
  for j in range(n-i):
    stars+='* '
  print(stars)
# 15.Right-Aligned Hill Pattern
# Input: n = 4
# Output:
#       *
#     * *
#   * * *
# * * * *
print("15.Right-Aligned Hill Pattern Input: n = 4")
n=4
for i in range(n):
  stars=''
  for k in range(n-i):
    stars+='  '

  for j in range(i+1):
    stars+='* '
  print(stars)