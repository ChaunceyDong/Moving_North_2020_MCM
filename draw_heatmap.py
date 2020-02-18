import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
#from clean_test import *


# HadISST1_SST_2019_4.csv
# 12345678901234567890

def get_AtSST_df(SST_file_name):
    data = pd.read_csv(SST_file_name, skiprows=1, header=None).iloc[:, :-1]
    Atlantic_data = data.iloc[24:38, 161:190]  # (24,161)to(38,190)=(66N, 19W)to(52N, 10E)
    Atlantic_SST = Atlantic_data / 100  # data to temperature
    Atlantic_SST[Atlantic_SST < -300] = np.nan  # clean land data
    return Atlantic_SST

y_list = []
for i in list(range(52,67))[::-1]:
    y_list.append(str(i)+'N')

x_list = []
for i in list(range(1,20))[::-1]:
    x_list.append(str(i)+'W')
x_list.append('0')
for i in range(0,11):
    x_list.append(str(i)+'E')




def draw_SST_heatmap(SST_file_name):
    Atlantic_SST = get_AtSST_df(SST_file_name)
    sns.heatmap(Atlantic_SST, vmax=18, vmin=4)
    plt.title(SST_file_name[:-4])
    # plt.show()
    print(SST_file_name)
    plt.savefig('./' + SST_file_name[:-4] + '.png')
    plt.close()


def loof_year(year):
    for fname in os.listdir("./"):
        if fname.startswith('HadISST1_SST_' + str(year)):
            if fname.endswith('csv'):
                draw_SST_heatmap(SST_file_name=fname)
        # print(fname)


def draw_opt_heatmap(fish_name, opt_temp, SST_file_name):
    sub_path = './' + fish_name + '/'
    Atlantic_SST = get_AtSST_df(SST_file_name)
    opt_temp_df = (Atlantic_SST - opt_temp).abs()
    sns.heatmap(opt_temp_df, vmax=10, vmin=0, xticklabels=x_list, yticklabels=y_list)
    plt.title('Tolerance_value_'+fish_name + SST_file_name[12:20])
    plt.savefig(fish_name + SST_file_name[12:20] + '.png')
    plt.close()


def loof_year_opt_T(year, fish_name, opt_temp):
    for fname in os.listdir("./SST_month/"):
        if fname.startswith('HadISST1_SST_' + str(year)):
            if fname.endswith('csv'):
                draw_opt_heatmap(fish_name, opt_temp, fname)


def draw_overlap_opt_heatmap(fish_1, fish_2, SST_file_name):
    # fish_1=['name',10]
    Atlantic_SST = get_AtSST_df(SST_file_name)
    opt_temp_df_1 = (Atlantic_SST - fish_1[1]).abs()
    opt_temp_df_2 = (Atlantic_SST - fish_2[1]).abs()
    opt_temp_df = opt_temp_df_1 + opt_temp_df_2
    sns.heatmap(opt_temp_df)
    plt.savefig('./Overlap_opt_heatmap/overlap_' + SST_file_name[12:19] + '.png')
    plt.close()


def loof_year_overlap_opt_T(year, fish_1, fish_2, ):
    for fname in os.listdir("./SST_month"):
        draw_overlap_opt_heatmap(fish_1, fish_2, fname)


loof_year_opt_T(2014, 'Herring', 4.62)
loof_year_opt_T(2015, 'Herring', 4.62)

# loof_year_opt_T(2018, 'Mackerel', 12.94)
# for year in range(2004, 2005):
#     loof_year_overlap_opt_T(year, FISH_H, FISH_M)

# i = 0
# for fname in os.listdir("./AtSST_SST/"):
#     date_str = fname[-11:-4]
#     print(fname)
#     if fname.startswith('.'):continue
#     year = int(date_str[:4])
#     if year < 2009: continue
#     Atlantic_SST = pd.read_csv('./AtSST_SST/' + fname, index_col=0)
#     opt_temp_df_1 = (Atlantic_SST - FISH_M[1]).abs()
#     opt_temp_df_2 = (Atlantic_SST - FISH_H[1]).abs()
#     opt_temp_df = opt_temp_df_1 + opt_temp_df_2
#     cmap = sns.cubehelix_palette(start=1.5, rot=3, gamma=0.8, as_cmap=True)
#     sns.heatmap(opt_temp_df, vmax=15, vmin=8, cmap='rainbow')
#     plt.title('Overlap_opt_heatmap_'+date_str)
#     plt.savefig('./Overlap_opt_heatmap/overlap_' + date_str + '.png')
#     plt.close()
