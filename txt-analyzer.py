####################################################################
###############################::INFO::#############################
# 
# All rights reserved to Yashwanth Maheshwaram at Braceat, Inc.
# This is a code to analyze as small piece of text that is written
# onto sample.txt. This script can analyze
# No. of words, 
# No. of word repetetions
# No. of Adjectives, Adverbs, Nouns and Verbs Syllable wise
# 

import sys, re, os

"""
def adjects():
  
  return 
"""

def main():
  
  adjs = []
  vrbs = []
  advrbs = [] 
  nouns =  [] 
  f = open ('sample.txt', 'r')
  samlines = f.readlines()
 
  #scan logic starts here
    
  for sameachline in samlines:
    sameachlinelist = sameachline.strip()
    sameachlinelist = sameachline.split() #yet to delete punctuation from the strings.
    adjects(sameachlinelist,adjs)
    adverbs(sameachlinelist,advrbs)
    noun(sameachlinelist,nouns)
    verbs(sameachlinelist,vrbs)
  
  print '\nAdjectives:'
  print adjs

  print '\nAdverbs:'
  print advrbs

  print '\nNouns:'
  print nouns

  print '\nVerbs:'
  print vrbs


#adjectives fun
def adjects(sameachlinelist,adjs):
  
  f1 = open ('adjectives/28Kadjectives.txt', 'r')
  chklines = f1.readlines()
 
  for chkwrd in chklines:
    chkwrd = str(chkwrd)
    chkwrd = chkwrd.strip()
    if chkwrd in sameachlinelist:
      adjs.append(chkwrd)   
        
  return adjs
  
#adverbs fun
def adverbs(sameachlinelist,advrbs):
  
  f2 = open ('adverbs/6Kadverbs.txt', 'r')
  chklines = f2.readlines()
 
  for chkwrd in chklines:
    chkwrd = str(chkwrd)
    chkwrd = chkwrd.strip()
    if chkwrd in sameachlinelist:
      advrbs.append(chkwrd)   
        
  return advrbs

#nouns fun
def noun(sameachlinelist, nouns):
  
  f3 = open ('nouns/91Knouns.txt', 'r')
  chklines = f3.readlines()
 
  for chkwrd in chklines:
    chkwrd = str(chkwrd)
    chkwrd = chkwrd.strip()
    if chkwrd in sameachlinelist:
      nouns.append(chkwrd)   
        
  return nouns

#verbs fun
def verbs(sameachlinelist, vrbs):
  
  f3 = open ('verbs/31Kverbs.txt', 'r')
  chklines = f3.readlines()
 
  for chkwrd in chklines:
    chkwrd = str(chkwrd)
    chkwrd = chkwrd.strip()
    if chkwrd in sameachlinelist:
      vrbs.append(chkwrd)   
        
  return vrbs

#boilerplating
if __name__ == '__main__':
    main()  


