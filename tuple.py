n = int(input())
numtup = tuple(int(x.strip()) for x in raw_input().split(' '))

print(hash(numtup))
