

def add_students():
    ans = ''
    class_list = []
    while ans != 'n':
        ans = input("add student? 'y' or 'n': ")
        if ans == 'y':
            class_list.append(input(" student name "))
        else:
            print("Please enter 'y' or 'n'")

    return class_list

print(add_students())


'''
* What is a while loop? How is it different from a for loop?
* How do you accept 'N' or 'Y' as well? (string functions)
* Break this up into 2 functions
  - one which handles correct input; the other which adds to the list
