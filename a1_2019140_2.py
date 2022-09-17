# -*- coding: utf-8 -*-
"""A1_2019140_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pYmPUK0SuzDbrGEWIYy1NvelLEmH09tJ

Q2

1.
"""

# pip install english-words

from english_words import english_words_set
'hello' in english_words_set

xyz = ["AlAo%12%%","AbcA#d123%","123hello%Xyz678","123"]
dig = '0123456789'
sp = '#$%&!'
alph = 'abcdefghijklmnopqrstuvwxyz'
calpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(xyz)):                                       # checks validity 
  if len(xyz[i]) >= 8:
    #print(True)
    z=xyz[i]
    dc=z[1:len(z)-1]
    r_1 = set(list(xyz[i])).intersection(list(alph))
    r_2 = set(list(dc)).intersection(list(calpha))
    r_3 = set(list(dc)).intersection(list(sp))
    r_4 = set(list(xyz[i])).intersection(list(dig))
    if len(r_1) > 0 and len(r_2) > 0 and len(r_3) > 0 and len(r_4) > 0 :
      #print(True)
      b = 0
      for j in english_words_set:
        if j in xyz[i] and len(j) >=3:
          b = 1
      if b ==1: print("Invalid")
      else: print("Valid")
    else:
      print("Invalid")
  else:
    print("Invalid")

"""2.

"""

import random

def cpx(xy):
  for i in range(len(xy)):
    if len(xy[i]) >= 8:
      #print(True)
      z=xy[i]
      dc=z[1:len(z)-1]
      r_1 = set(list(xy[i])).intersection(list(alph))
      r_2 = set(list(dc)).intersection(list(calpha))
      r_3 = set(list(dc)).intersection(list(sp))
      r_4 = set(list(xy[i])).intersection(list(dig))
      if len(r_1) > 0 and len(r_2) > 0 and len(r_3) > 0 and len(r_4) > 0 :
        #print(True)
        b = 0
        for j in english_words_set:
          if j in xy[i] and len(j) >=3:
            b = 1
        if b ==1: return False
        else: return True
      else:
        return False
    else:
      return False

def generatep():
  le = random.randrange(8,30)
  out = [0]*le
  x = [n for n in range(le)] 
  for i,j in enumerate(x):
    r = random.choice(x)
    x = [a for a in x if a != r]
    uc = random.randrange(1,5)
    if (uc==1):
        out[r] = random.choice(list(alph))  
    elif(uc==2):
        out[r] = random.choice(list(calpha))            #basically these 4 conditions should be there if its not I get fked .. so I randomized everything . if by any chance the pass generated is not valid .. it reruns
    elif(uc==3):
        out[r] = random.choice(list(sp))
    elif(uc==4):
        out[r] = random.choice(list(dig))
  outt= ''
  for i in range(len(out)):
    outt=outt+str(out[i])
  lin = list()
  lin.append(outt)
  if cpx(lin) == True:
    print(outt)
  else: 
    generatep()

generatep()