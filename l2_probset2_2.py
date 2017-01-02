# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 15:05:59 2017

@author: MAHE
"""

def fix_machine(debris, product):
    ### WRITE YOUR CODE HERE ###
    len_p=len(product)
    len_d=len(debris)
    count=0
    i=0
    j=0
    while i<len_d:
        while j<len_p:
            if product[j]==debris[i]:
                count=count+1
                break
            j=j+1
        j=0
        i=i+1
    if count==len_p:        
         return product
    else:
        return "Give me something that's not useless next time."
        
print fix_machine('UdaciousUdacitee', 'Udacity')
print fix_machine('wsx0-=mttrhix', 't-shirt')