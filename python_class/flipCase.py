S = str(input())
SO = ""

for ch in S:
    if ch == ch.lower():
        SO = SO + ch.upper()
    elif ch == ch.upper():
        SO = SO + ch.lower()
    else:
        SO = SO + ch

S = SO    
print(S)
