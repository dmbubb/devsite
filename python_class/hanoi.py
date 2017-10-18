num_disks = int(input("How many disks? ").strip())

def load_source(num_disks):
    src = []
    while num_disks > 0:
        src.append(num_disks)
        num_disks -= 1
    return src

def hanoi(n, source, helper, target):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)
        print(source, helper, target)
#    print("Moves ", moves)



source = load_source(num_disks) 
target = []
helper = []

print(source, helper, target)
hanoi(len(source),source,helper,target)


