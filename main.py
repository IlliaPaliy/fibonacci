inputArg = int(input("Choose number of numbers to sum:"))
startNum1 = 0
startNum2 = 1
for i in range (0, inputArg):
    summary = startNum1 + startNum2
    print(summary)
    startNum1 = startNum2
    startNum2 = summary
