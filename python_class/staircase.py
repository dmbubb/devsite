def count_sways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return count_sways(n-1) + count_sways(n-2) + count_sways(n-3)

s = 10

for i in range(s):
    print("stair len",i)
    print(count_sways(i))
