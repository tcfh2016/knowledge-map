import pandas as pd
import glob
import os


path = r'C:\Users\lianbche\Git\knowledge-map\Techs\data-science\pandas\csv\read_multi_csv\23R3'                     # use your path
all_files = glob.glob(os.path.join(path, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent

df_from_each_file = (pd.read_csv(f) for f in all_files)
concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)
print(concatenated_df)
#concatenated_df.to_csv("20230925T1915-16_ddds.csv", index=False)
concatenated_df.to_csv("20230925T1035-40_ddds.csv", index=False)