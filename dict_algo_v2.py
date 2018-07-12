actual = {"tomatoes": 3, "apple": 3, "oranges": {"Navel": {"juicy": 4}}, "grapes": 7, "kiwis": 2}

expected = {"apple": 3, "oranges": 3, "bananas": 6, "kiwis": 3}


# sample output
# [['+', 'tomatoes', 3], 
# ['+', 'oranges.navel.juicy', 4], 
# ['-', 'oranges', 3], 
# ['+', 'grapes', 7], 
# ['+', 'kiwis', 2], 
# ['-', 'bananas', 6], 
# ['-', 'kiwis', 3]]

