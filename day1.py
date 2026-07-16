#1 Area of Square
#Question: Calculate the area of a square.
#  - Formula: Area = side × side - Input: - Side = 5 - Output: - Area of square is: 25
side=5
area=side*side
print(area)
# 2. Area of Rectangle
# Question: Calculate the area of a rectangle. - Formula: Area = length × breadth - Input: - Length = 6 -
# Breadth = 4 - Output: - Area of rectangle is: 24
length=6
breadth=4
area=length*breadth
print(area)
# 3. Area of Triangle
# Question: Calculate the area of a triangle using base and height. 
# - Formula: Area = (1/2) × base × height - Input: - Base = 8 - Height = 5 -
# Output: - Area of triangle is: 20.0
base=8
height=5
area=1/2*(base*height)
print(area)
# 4. Perimeter of Square
# Question: Calculate the perimeter of a square. - Formula: Perimeter = 4 × side - Input: - 
# Side = 6 - Output: - Perimeter of square is: 24
side=6
perimeter=4*side
print(perimeter)
# 5. Perimeter of Rectangle
# Question: Calculate the perimeter of a rectangle. - Formula: Perimeter = 2 × (length + breadth) - 
# Input: - Length = 5 - Breadth = 3 - Output: - Perimeter of rectangle is: 16
l=5
b=3
perimeter=2*(l+b)
print(perimeter)
# 6. Perimeter of Triangle
# Question: Calculate the perimeter of a triangle. - Formula: Perimeter = side1 + side2 + side3 -
# Input: - Side1 = 5, Side2 = 6, Side3 = 7 - Output: - Perimeter of triangle is: 18
side1=5
side2=6
side3=7
perimeter=side1+side2+side3
print(perimeter)
# 7. Break Amount into 1000s, 500s, and Remaining Change
# Question: Break the total amount into denominations. - 
# Input: - Amount = 3700 - Output: - 1000s: 3 - 500s: 1 - Remaining: 200
amount=3700
thousands=amount//1000
remainder=amount%1000
five_hunderds=remainder//500
last=remainder%500
print('1000s:',thousands,'- 500s:',five_hunderds,'-Remaining:',last)
# 8. Convert Seconds into Hours, Minutes, and Seconds
# Question: Convert total seconds into hours, minutes, and seconds. - 
# Input: - Total seconds = 3672 - Output: - Hours: 1 - Minutes: 1 - Seconds: 12
seconds=3672
hours=seconds//3600
r1=seconds%3600
minutes=r1//60
remaining=r1%60
print('Hours:',hours,'Minutes:',minutes,'seconds:',remaining)
# 9. Sum of Marks (Maths, Physics, Chemistry)
# Question: Calculate the sum of marks in 3 subjects. -
# Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Total marks: 263
maths=85
physics=90
chemistry=88
total_marks=maths+chemistry+physics
print(total_marks)
# 10. Average of Marks (Maths, Physics, Chemistry)
# Question: Calculate the average of marks in 3 subjects. - 
# Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Average marks: 87.67
Maths = 85 
Physics = 90 
Chemistry = 88 
Average_marks=(Maths+Physics+Chemistry)/3
print(Average_marks)