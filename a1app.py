"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting the first currency to
the second.

Author: Julia Ludwig (jal545) and Jackson Stone (jls596)
Date:   9/30/20
"""
import a1

old=input('Enter source currency: ')
new=input('Enter target currency: ')
amt=input('Enter original amount: ')
print('You can exchange '+amt+' '+old+' for '+str(a1.exchange(old,new,float(amt)))+' '+new+'.')
