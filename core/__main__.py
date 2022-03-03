from time import sleep
from parse_product import parseProduct
import os
import pandas as pd


parse = parseProduct()

result = parse.getData()
exists = False


if os.path.exists('samsung.csv'):
    # We need to create a new file.
    df = pd.DataFrame(result, columns=['Samsung'])
    df.to_csv('new_samsung.csv', index=False)
    exists = True

else:
    df = pd.DataFrame(result, columns=['Samsung'])
    df.to_csv('samsung.csv', index=False)


if exists is True:
    # Now let's compare the files
    oldfile = pd.read_csv('samsung.csv')
    newfile = pd.read_csv('new_samsung.csv')

    # convert to list
    old_list = oldfile.values.tolist()
    new_list = newfile.values.tolist()

    # compare the two lists
    for i in new_list:
        if i not in old_list:
            print("New Samsung Phone:", i)
            sleep(1)
        

    # delete the old file
    os.remove('samsung.csv')
    # rename the new file
    os.rename('new_samsung.csv', 'samsung.csv')