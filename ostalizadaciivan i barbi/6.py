# # import math
s = "ababaa"
# # brojac = 0
# # brojac2 = 0
# # permutacije = 0
# # duljina_gapa = math.ceil(len(S) / 3) #gapa

# # for slovo in S:
# #     if slovo == "a":
# #         brojac += 1
# #     else:
# #         brojac2 += 1

# # if brojac % 3 == 0:
# #     print("imamo broja * a za tocno 3 gapa")


# # elif brojac % 3 == 1 or brojac % 3 == 2:
# #     permutacije += 0
# #     print("ne postoji gap")

# # broj_a_po_gapu = brojac / 3
# # po_gapu = duljina_gapa / broj_a_po_gapu


# # print("broj:", permutacije)


 
def distinctChars(s) :  
  
    # Frequency of each character  
    freq = [0]*26;  
    count = 0;  
      
    # Loop to count the frequency  
    # of each character of the string  
    for i in range(len(s)) :  
        freq[ord(s[i]) - ord('a')] += 1;  
  
    # If frequency is greater than 0  
    # then the character occured  
    for i in range(26) : 
        if (freq[i] > 0) : 
            count += 1;  
  
    return count;  
  
# Function to count the number  
# of ways to partition the string  
# such that each partition have  
# same number of distinct character  
def waysToSplit(s) :  
    n = len(s);  
    answer = 0;  
      
    # Loop to choose the partition  
    # index for the string  
    for i in range(1, n) : 
          
        # Divide in two parts  
        left = s[0 : i];  
        right = s[i : n ];  
  
        # Check whether number of distinct  
        # characters are equal  
        if (distinctChars(left) == distinctChars(right)) : 
            answer += 1;  
      
    return answer;  
distinctChars(s)
# Driver Code  
if __name__ == "__main__" :  
  
    s = "ababa";  
  
    print(waysToSplit(s));  