# import pandas as pd
#
# test = pd.read_csv('2018_1_SST copy.txt', sep='\t')

# with open('2018_1_SST copy.txt') as f:
#     cNames = f.readlines()
#     print(cNames)


f2 = open('inserted_.txt', 'w')
with open('2018_1_SST copy.txt', 'r') as f:
    for i in range(360):
        line_str = f.readline()
        inserted_str = ','.join(line_str[i:i + 6] for i in range(0, len(line_str), 6))
        f2.writelines(inserted_str)


