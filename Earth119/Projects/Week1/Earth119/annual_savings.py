# -*- coding: utf-8 -*-
#Interpreter: Anaconda2 Python 2.7
"""
-Write script that computes annual returns on $10k 
at 10% interest over 30 years

Variables: 
    f_iniInvest = amount invested
    f_interest = interest rate
    i_Year = duration of investment

"""
#===============================================
#           Define Variables
#===============================================
f_iniInvest = 1e4 
f_interest = 0.1 
i_Years = 30 


#===============================================
#               do compuation - savings
#===============================================
def annual_return( f_iniInvest, f_interest, i_Years ):
    """
    - computing annual savings
    :input
        Variables: 
            f_iniInvest = amount invested
            f_interest = interest rate
            i_Year = duration of investment
    :output
        savings in last year (i_Years)
    
    """
    currInvest = f_iniInvest
    for i in range (i_Years-1):
        fGrowth = currInvest*f_interest
        #print ('Year', i+1, 'Savings', currInvest, 'Interest per Year', fGrowth)
        currInvest += fGrowth
    return currInvest
# add a function call
print (annual_return( f_iniInvest, f_interest, i_Years))
        
        
        
        