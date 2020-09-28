def name_triangle():
    user_name = input("Please enter your name: ")
    for i in range(1, len(user_name) + 1):
        print(user_name[:i])


name_triangle()
