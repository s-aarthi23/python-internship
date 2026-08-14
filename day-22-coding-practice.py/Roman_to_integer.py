values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
total = 0
roman = input("Enter a Roman numeral: ")
for symbol in range(len(roman)):
    if symbol + 1 < len(roman) and values[roman[symbol]] < values[roman[symbol + 1]]:
        total -= values[roman[symbol]]
    else:
        total += values[roman[symbol]]
print("The integer value of the Roman numeral is:", total)    
    