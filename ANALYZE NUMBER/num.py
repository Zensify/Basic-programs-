def analyzeNumber(aNumber):
    if aNumber < 0:
        return "Negative"
    if aNumber > 0:
        return "Positive"
    if aNumber == 0:
        return "Zero"

print (analyzeNumber(23))
print (analyzeNumber(-300))
print (analyzeNumber(0))