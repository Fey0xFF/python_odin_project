#init stock price
stockprices = [17,3,6,9,15,8,6,1,10]

#functions for max and min checkers, one for single and one for multiple inputs
def maxmin_num(*stocklist):
  print ("Buy when the stock is $" + str(min(stocklist[0:])))
  print ("Sell when the stock is $" + str(max(stocklist[0:])))

def maxmin_list(stocklist):
  print ("Buy when the stock is $" + str(min(stocklist)))
  print ("Sell when the stock is $" + str(max(stocklist)))


#call functions
maxmin_num(17,3,6,9,15,8,6,1,10)
maxmin_list(stockprices)
