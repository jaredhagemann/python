# Task: Given a list of investment risks (integers) and a maximum allowable risk threshold,
#       compute the largest possible risk which could be achieved via a combination of all
#       possible investments. There is no limit to the number of times each investment can
#       be used.
# This is an unoptimized, brute force solution

def maxReturn(investmentList, riskThreshold, currentRisk=0):
  maxRisk = currentRisk
  for i in investmentList:
    if (currentRisk+i == riskThreshold):
      # Risk threshold matched exactly, we can return
      #print "*** exact (", currentRisk, "+", i, "=", riskThreshold, ")"
      return currentRisk+i
    elif (currentRisk+i < riskThreshold):
      # The addition of this investment to the current subset of investments
      # does not exceed the risk threshold. Add its value to the current total
      # and recursively call this function, setting maxRisk to the higher of
      # the current value or the returned value
      #print "maxRisk(", currentRisk, "+", i, "=", currentRisk+i, ")"
      newMax = maxReturn(investmentList, riskThreshold, currentRisk+i)
      maxRisk = max(maxRisk, newMax)
    else: # sum+i > R
      # The addition of this investment to the current subset of investments
      # would exceed the risk threshold. Moving on.
      #print "bust (", currentRisk, "+", i, "=", currentRisk+i, ")"
      pass
  return maxRisk
