'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    #variable to hold the count 
    count = 0
    # if word is 1 letter or empty, return 0, the base case
    if len(word) == 1 or len(word) == 0:
        return 0

    #increase count if 'th' is found in first 2 positions
    if word[0] == 't' and word[1] == 'h':
        count = count + 1
    
    #recursion
    #it's going to split the array and keep checking until it reaches the base case
    return count + count_th(word[1:])
    
