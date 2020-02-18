import os
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def txt_to_csv(file_name):
    new_f = open(file_name + '.csv', 'w')
    with open(file_name + '.txt', 'r') as f:
        for i in range(360):
            line_str = f.readline()
            inserted_str = ','.join(line_str[i:i + 6] for i in range(0, len(line_str), 6))
            new_f.writelines(inserted_str)


def gen_mon_csv_from_year(year_file_name):
    year_file_name_drop_type = year_file_name[:-4] + "_"
    with open(year_file_name) as f1:
        all_list = f1.readlines()
        num = 0
        month_list = list(range(0, 2173, 181))
        for i in range(0, 12):
            from_nub = month_list[i]
            to_nub = month_list[i + 1]
            month_file_name = year_file_name_drop_type + str(int(from_nub / 181 + 1)).zfill(2)
            file_obj = open(month_file_name + '.txt', 'w')
            for j in all_list[from_nub:to_nub]:
                file_obj.write(j)
            file_obj.close()
            txt_to_csv(month_file_name)
            os.remove(month_file_name + '.txt')


def data_clean(year):
    gen_mon_csv_from_year('HadISST1_SST_' + str(year) + '.txt')


def get_AtSST_df(SST_file_name):#TODO, path changed
    data = pd.read_csv(SST_file_name, skiprows=1, header=None).iloc[:, :-1]
    Atlantic_data = data.iloc[24:38, 161:190]  # (24,161)to(38,190)=(66N, 19W)to(52N, 10E)
    Atlantic_SST = Atlantic_data / 100  # data to temperature
    Atlantic_SST[Atlantic_SST < -300] = np.nan  # clean land data
    return Atlantic_SST


def read_AtSST_df(year, month):
    pd.read_csv('./AtSST_SST/AtSST_SST_' + year + month + '.csv', index_col=0)


def read_AtSST_df(AtSST_file_name):
    pd.read_csv('AtSST_SST_2004_06.csv')
    pass


def new_folder(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)


def gen_AtSST_file(SST_file_name, delete_=False):
    AtSST_file_name = 'AtSST' + SST_file_name[8:]
    sub_folder_path = './AtSST_SST/'
    new_folder(sub_folder_path)
    get_AtSST_df(SST_file_name).to_csv(sub_folder_path + AtSST_file_name)
    if delete_: os.remove(SST_file_name)


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


# def draw_opt_heatmap(fish_name, opt_temp, SST_file_name):
#     sub_path = './' + fish_name + '/'
#     new_folder(sub_path)
#     Atlantic_SST = get_AtSST_df(SST_file_name)
#     opt_temp_df = (Atlantic_SST - opt_temp).abs()
#     sns.heatmap(opt_temp_df, vmax=10, vmin=0)
#     title = fish_name + get_mon_str(SST_file_name)
#     plt.title(title)
#     plt.savefig(sub_path + title + '.png')
#     plt.close()

def draw_opt_heatmap(fish_name, opt_temp, SST_file_name):
    sub_path = './' + fish_name + '/'
    new_folder(sub_path)
    Atlantic_SST = get_AtSST_df(SST_file_name)
    opt_temp_df = (Atlantic_SST - opt_temp).abs()
    sns.heatmap(opt_temp_df, vmax=10, vmin=0)
    title = fish_name + get_mon_str(SST_file_name)
    plt.title(title)
    plt.savefig(sub_path + title + '.png')
    plt.close()


def gen_AtSST_csv_from_specific_year(year):  # 名称改到这里
    for fname in os.listdir("./"):
        if fname.startswith('HadISST1_SST_' + str(year)):
            if fname.endswith('csv'):
                gen_AtSST_file(fname)


def loof_year_opt_T(year, fish_name, opt_temp):
    for fname in os.listdir("./"):
        if fname.startswith('HadISST1_SST_' + str(year)):
            if fname.endswith('csv'):
                draw_opt_heatmap(fish_name, opt_temp, fname)


def loof_opt_T(fish_name, opt_temp):
    for fname in os.listdir("./AtSST_SST/"):
        draw_opt_heatmap(fish_name, opt_temp, fname)


def loof_year_(func, year):
    for fname in os.listdir("./"):
        if fname.startswith('HadISST1_SST_' + str(year)):
            if fname.endswith('csv'):
                func(fname)


def delete_mon_SST_of_year(year):
    for fname in os.listdir("./"):
        if fname.startswith('HadISST1_SST_' + str(year)):
            if fname.endswith('csv'):
                os.remove(fname)


def get_mon_str(file_name):
    # _2018_MM
    return file_name[-11:-4]


def gen_mon_csv_from_specific_year(year):
    raw_file_name = 'HadISST1_SST_' + str(year) + '.txt'
    gen_mon_csv_from_year(raw_file_name)


def from_raw_to_opt_pic(fish_type):
    for year in YEAR_LIST:
        raw_file_name = 'HadISST1_SST_' + str(year) + '.txt'
        gen_mon_csv_from_year(raw_file_name)
        loof_year_opt_T(year, fish_type[0], fish_type[1])


YEAR_LIST = list(range(2004, 2020))
FISH_H = ['Herring', 4.62]
FISH_M = ['Mackerel', 12.94]

# if __name__ == "__main__":
#     from_raw_to_opt_pic(FISH_H)
#     from_raw_to_opt_pic(FISH_M)

# for i in range(2004, 2020):
#     gen_mon_csv_from_specific_year(i)

# if __name__ == "__main__":
#     loof_year_opt_T(2018, 'Herring', 4.62)
#     loof_year_opt_T(2018, 'Mackerel', 12.94)
