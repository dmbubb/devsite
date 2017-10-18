# solution for factors.py

# Step 0 Finish this function
def isFactor(n, m):
    '''True or False -- is n divisible by m?'''
    return n % m == 0

# Step 1 Finish this function
def factors(n):
    '''Assuming n is a positive integer, print its factors.'''
    print("The factors of ", n, "are")
    for i in range(1,n+1):
        if isFactor(n, i):
            print(i)

# Step 2 Try your functions by running this one.
def test():
    x = input("Enter a number, or q to quit. ")
    while x != 'q':
        factors(int(x))
        x = input("Enter a number, or q to quit. ")
        
