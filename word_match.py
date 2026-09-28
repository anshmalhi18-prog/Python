def match_word(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr=ctr+1
            lst.append(word)
    print("List of words with the first and last character same: ",lst)
    return ctr

count=match_word(["abc","123","1331","224","aba"])
print("Number of words having the first and last character same: ",count)
