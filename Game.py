user_input = input("Of what shape do you want to find the area? triangle or rectangle?: ")
if user_input == "triangle":
    user_input_triangle_base = int(input("First type the base of the triangle: "))
    user_input_triangle_height = int(input("Second type the height of the triangle: "))
    triangle_almost = user_input_triangle_base * user_input_triangle_height
    triangle_answer = triangle_almost / 2
    print(f"The area of that triangle is {triangle_answer}!")
elif user_input == "rectangle":
    user_input_rectangle_length = int(input("First type the lenght of the rectangle: "))
    user_input_rectangle_width = int(input("Second type the width of the rectangle: "))
    rectangle_answer = user_input_rectangle_length * user_input_rectangle_width
    print(f"The area of that rectangle is {rectangle_answer}!")

