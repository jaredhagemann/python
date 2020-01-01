import portfolio

# sample usage
testCount = 5
testInvestments = [[5,3,7], [5,9], [9,6,13], [7], [7,11,20,30,13]]
riskThresholds =  [11,      22,    17,       20,  51]
solutions =       [11,      20,    15,       14,  51]
passCount = 0

for i in range(testCount):
    maximumRisk = portfolio.maxReturn(testInvestments[i], riskThresholds[i])
    #print "Max:", maximumRisk
    if maximumRisk == solutions[i]:
        passCount += 1
        print "Test", i+1, ": [PASS]"
    else:
        print "Test", i+1, ": [FAIL]"

print "[", passCount, "/", testCount, "] PASSED"
