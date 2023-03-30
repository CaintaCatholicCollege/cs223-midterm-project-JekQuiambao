import math

repeat = "y"
while repeat.lower() == "y":
    choice = 0
    while choice < 1 or choice > 4:
     
        print("\nChoose a shape to calculate its area:")
        print("1. Triangle")
        print("2. Square")
        print("3. Rectangle")
        print("4. Circle")
        choice = int(input("Enter your choice (1-4): "))

        if choice < 1 or choice > 4:
            print("Invalid choice. Please enter a number between 1 and 4.\n")


    if choice == 1:
        base = float(input("Enter base length of triangle: "))
        height = float(input("Enter height of triangle: "))
        triangle_area = 0.5 * base * height
        print(f"The area of the triangle is {triangle_area}")
    elif choice == 2:
        side = float(input("Enter side length of square: "))
        square_area = side * side
        print(f"The area of the square is {square_area}")
    elif choice == 3:
        length = float(input("Enter length of rectangle: "))
        width = float(input("Enter width of rectangle: "))
        rectangle_area = length * width
        print(f"The area of the rectangle is {rectangle_area}")
    elif choice == 4:
        radius = float(input("Enter radius of circle: "))
        circle_area = math.pi * radius * radius
        print(f"The area of the circle is {circle_area}")
    else:
        print("Invalid choice.")

    repeat = input("\nDo you want to calculate another shape? (y/n): ")

print("\nMidterm Project: Quiambao, John King Eduard B.")
