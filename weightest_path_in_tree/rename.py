import os
direcory_name = '/Users/donsee/Downloads/黑客军团/'
dirs = os.listdir(direcory_name)
for item in dirs:
    if item.startswith('Mr.'):
        old_name = item.split('.')
        new_name = direcory_name + old_name[2]
        os.renames(direcory_name + item,  new_name)
