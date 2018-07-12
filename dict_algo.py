actual = {"tomatoes": 3, "apple": 3, "oranges": {"navel": {"juicy": 4}}, "grapes": 7, "kiwis": 2}

expected = {"apple": 3, "oranges": {"navel": {"juicy": 5}}, "bananas": 6, "kiwis": 3}

# method assumes that both lists have a nested dictionary pair, change expected "oranges" back to "orange": 3, check v2

# sample output

# [['+', 'tomatoes', 3], 
# ['+', 'oranges.navel.juicy', 4], 
# ['-', 'oranges.navel.juicy', 5], 
# ['+', 'grapes', 7], 
# ['+', 'kiwis', 2], 
# ['-', 'bananas', 6], 
# ['-', 'kiwis', 3]]
 
lst = [ ]
def compare(dict1, dict2, parent=""): # feed in optional parameter "parent"
    global lst
    for key, value in dict1.items():
        if key not in dict2:
            a = ["+", key, value]
            lst.append(a)
        if isinstance(dict1[key], dict): # Check if value is dict
            if key in dict2 and dict1[key] != dict2[key]:
                compare(dict1[key], dict2[key], parent + key + ".") # recursion, add in optional parent to print key.
                
             
        elif key in dict2 and dict1[key] != dict2[key]: # If not dict, just add to list
            b = ["+", parent + key, value] #parent is either "" or whatever key of a key:value pair with a dictionary value 
            lst.append(b)
            
            
    for key, value in dict2.items():
        if key not in dict1:
            c = ["-", key, value]
            lst.append(c)
        # if isinstance(dict2[key], dict): ---- Is there a need to run the recursion again in the second loop? -----
        #     if key in dict1 and dict2[key] != dict1[key]:
        #         compare(dict1[key], dict2[key]) # Check if value is dict
                
        if not isinstance(dict2[key], dict) and key in dict1 and dict1[key] != dict2[key]: # If not dict, just add to list
            d = ["-", parent + key, value]
            lst.append(d)
            
    return lst

# call the function
compare(actual, expected)

# append the lst into a master list
print (lst)