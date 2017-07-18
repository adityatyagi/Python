# MANIPULATE DATA WITH SHELVES
# .get(key, stringIfResultNotFound) -> values
# shelves keys must be strings

# METHOD 1 -> USING TEMPORARY LIST

import shelve

#blt = ["bacon", "lettuce", "tomato", "bread"]
#beans_on_toast = ["beans", "bread"]
#scrambled_eggs = ["eggs", "butter", "milk"]
#soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

with shelve.open('recipe', writeback=True) as recipe:
    
    ''' recipe["blt"] = blt
    recipe['beans'] = beans_on_toast
    recipe['eggs'] = scrambled_eggs
    recipe['soup'] = soup

    temp_list = recipe['blt']
    temp_list.append('butter')
    recipe['blt'] = temp_list

    temp_list = recipe['eggs']
    temp_list.append('chutney')
    recipe['eggs'] = temp_list 

    recipe['pasta'] = pasta '''


    for i in recipe:
        print(i, recipe[i])