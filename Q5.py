# 5
a = float(input("Enter Side 1 of Triangle(in cms) : ")) 
b = float(input("Enter Side 2 of Triangle(in cms) : ")) 
c = float(input("Enter Side 3 of Triangle(in cms) : ")) 
s=a+b+c/2
area = ((s*(s-a)*(s-b)*(s-c))**(1/2)) 
print("The area of the triangle is :", area, " cms")