#Write a program that classifies a triangle based on its side lengths.

first_side = int(input("Enter first side of triangle\n"))
second_side = int(input("Enter second side of triangle\n"))
third_side = int(input("Enter third side of triangle\n"))

if (first_side==second_side) and (first_side==third_side) and (second_side==third_side):
    print("Triangle is equilateral")
elif (first_side==second_side) or (first_side==third_side) or (second_side==third_side):
    print("Triange is isosceles")
elif (first_side!=second_side) and (first_side!=third_side) and (second_side!=third_side):
    print("Triangle is scalene")
else:
    print("Please enter valid sides")