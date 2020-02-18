import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt


def get_mon_str(SST_file_name):
    # 2018_MM
    return SST_file_name[-11:-4]


year_list = list(range(2004, 2020))

# idx = pd.date_range('2014-1-1', periods=12 * len(year_list), freq='MS')
idx = []
val = []
xloc = 2
yloc = 2


# for fname in os.listdir("./AtSST_SST"):
#     if fname.startswith('AtSST_SST_'):
#         idx.append(get_mon_str(fname))
#         val.append(pd.read_csv('./AtSST_SST/' + fname, index_col=0).iloc[xloc, yloc])
#         print(fname)
#
# ts = pd.Series(val, index=idx)
# ts.index = pd.to_datetime(ts.index, format='%Y_%m')
# ts = ts.sort_index()
# ts.plot()
# plt.title(str(xloc) + str(yloc))
# plt.show()


def get_loc_ts(xloc, yloc):
    year_list = list(range(1901, 2020))
    val = []
    idx = []
    for fname in os.listdir("./AtSST_SST"):
        if fname.startswith('AtSST_SST_'):
            idx.append(get_mon_str(fname))
            print(fname)
            val.append(pd.read_csv('./AtSST_SST/' + fname, index_col=0).iloc[xloc, yloc])
    ts = pd.Series(val, index=idx)
    ts.index = pd.to_datetime(ts.index, format='%Y_%m')
    ts = ts.sort_index()
    ts.plot()
    plt.title(str(xloc) + str(yloc))
    plt.show()

    ts.to_csv('./point_timeseries/'+'ts_point_'+str(xloc).zfill(2)+str(yloc).zfill(2)+'_all.csv')

    return ts


ts = get_loc_ts(2, 2)

#
# ts.to_csv('./point_timeseries/2-2.csv')
# a = pd.read_csv('./point_timeseries/2-2.csv',parse_dates=True,index_col=0)
