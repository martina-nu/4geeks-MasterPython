#Complete the function to return the area of the triangle.
b = input("Size of B")
h = input("Size of H")

def area_of_triangle(arg1, arg2):
    #your code here, please remove the "None" 
    b = int(arg1)
    h = int(arg2)
    return (b*h)/2

# Testing your function
print(area_of_triangle(b, h))