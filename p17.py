firsts = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def nbLetters(i):
    if i <20:
        return len(firsts[i])
    elif i < 100:
        return len(tens[i//10]) + (len(firsts[i%10]) if i%10 != 0 else 0)
    else:
        return len(firsts[i//100]) + 7 + (3 + nbLetters(i%100) if i%100 != 0 else 0)


s = 11
for i in range(1, 1000):
    s += nbLetters(i)    
print(s)

print(nbLetters(342))