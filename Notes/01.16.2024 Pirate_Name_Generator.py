# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 18:56:21 2024

@author: dev46
"""

import random
Name_1=["Jolly","Old","One-eyed","Stinky","Pegleg","Phlegmatic"]
Name_2=["Bud","Sally","Davie","Sam"]
Name_3=["Red","Blue","Green","Yellow"]

# first=random.sample(Name_1,1)
# middle=random.sample(Name_3,1)
# last=random.sample(Name_2,1)

def get_a_pirate_name():
    """ 
    Doc String for get a pirates name 
    """
    first=random.sample(Name_1,1)
    last=random.sample(Name_2,1)
    middle=random.sample(Name_3,1)
    outname= first[0]+" "+ middle[0] +" "+last[0]
    return outname
PIRATE_NAME = get_a_pirate_name()
print(PIRATE_NAME)
