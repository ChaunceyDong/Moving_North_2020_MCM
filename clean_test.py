
from data_clean import *

def from_multi_year_to_single_year(from_year, to_year):
    #year_list = range(from_year, to_year+1)
    f = open('HadISST1_SST_'+str(from_year)+'-'+str(to_year)+'.txt', 'r')

    for year in range(from_year, to_year+1):
        f2 = open('HadISST1_SST_' + str(year) + '.txt', 'w')
        for i in range(0, 2172):
            line_str = f.readline()
            f2.write(line_str)
        f2.close()



def from_year_to_AtSS(year):
    gen_mon_csv_from_specific_year(year)
    gen_AtSST_csv_from_specific_year(year)
    delete_mon_SST_of_year(year)

from_multi_year_to_single_year(1961,1990)
from_multi_year_to_single_year(1931,1960)
from_multi_year_to_single_year(1901,1930)




# f = open('HadISST1_SST_1991-2003.txt','r')
#
#
# for year in range(1991,2004):
#     f2 = open('HadISST1_SST_'+str(year)+'.txt','w')
#     for i in range(0,2172):
#         line_str = f.readline()
#         f2.write(line_str)
#     f2.close()