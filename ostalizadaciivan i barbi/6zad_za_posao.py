# You are given a string S consisting of letters 'a' and 'b'. 
# You want to split it into three separate non-empty parts. 
# The lengths of the parts can differ from one another. 
# In how many ways can you split S into three parts???, such that each part contains the same!!! number of letters 'a'?
#  
# Write a function: 
# class Solution { public int solution(string S); } 
# that, given a string S of length N, returns the number of possible ways of splitting S as described above. 
# Examples: 

# 1. Given S = "babaa", the function should return 2. The possible splits are: "ba ba I a" and "bab I a I a". 
# 2. Given S = "ababa", the function should return 4. The possible splits are: "a I ba ba", "a I bab I a", "ab I a I ba" and "ab ab a". 
# 3. Given S = "aba", the function should return 0. It is impossible to split S as required. 
# 4. Given S = "bbbbb", the function should return 6. The possible splits are: "b b bbb", "b bb bb", "b bbb b", "bb b bb", "bb bb b" and "bbb b b". Each part contains the same number of letters 'a', i.e. 0. 
# Write an efficient algorithm for the following assumptions: 
# - N is int in range [1...40000]
# - string S contains only letters a and b

import math
#S = "babaa"
#S = "ababa"
#S = "abbaba"
#S = "aba"
S = "bbbbb"

#ceslja slova i nalazi a kad ga nade onda dodaje jedan
def brojac():
    brojac_a = 0
    #brojac slova a
    for slovo in S:
        if slovo == "a":                   
            brojac_a += 1
    return brojac_a

    
#uvjet za dijeljenje "a "u 3 cjeline
def particije():
    brojac_a = 0
    brojac_1b = 0
    brojac_2b = 0
    a1 = a_po_cjelini
    a2 = a_po_cjelini * 2
    a3 = a_po_cjelini * 3
    index = 0
    for slovo in S:
        if slovo == "a":
            brojac_a += 1
            if brojac_a == a1:
                granica_1 = index
                #print(granica_1,"granica1")
            if brojac_a == a2:
                granica_2 = index
                #print(granica_2, "granica2")
            if brojac_a == a3:
                granica_3 = index
                #print(granica_3, "granica3")
        index = index + 1
    index = 0  

    for index in range (granica_1, granica_2):
        if S[index] == "b":
            brojac_1b += 1
        index += 1
    for index in range (granica_2, granica_3):
        if S[index] == "b":
            brojac_2b += 1
        index += 1
    broj_permutacija = (brojac_1b +1)  * (brojac_2b + 1)
    print("broja mogucih permutacija u stringu S je:", broj_permutacija)


ukupno = brojac()
if ukupno % 3 == 0:
        a_po_cjelini = math.floor(ukupno/ 3) #ukpno "a" po cjelini  
        print("ukupan broj a-ova djeljiv je pravilno na tri djela i iznosi", a_po_cjelini, "po cjelini") 
        particije()      
else:
    print("nepravilno zadan string") 
    print("broja mogucih permutacija u stringu S je: 0" )
        #DJELI UKUPAN BROJAC SA 3 CELJIJE DA DOBIJEBMO BROJ A PO CELIJI
        
        
