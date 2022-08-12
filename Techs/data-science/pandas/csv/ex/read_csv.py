import pandas as pd
df = pd.read_csv("csv.txt", index_col = 0)

print(df)
print(df.index)
print(df.index.values)
print(df.columns)
print(df.columns.values)

print(df.loc['cb8386_MultiUEMultiBearerDL300UL100_8CC_1UE_TDD125_ABIO_CFG_NSA_DLUL']['First Fail Build'])
print(type(df.loc['cb8386_MultiUEMultiBearerDL300UL100_8CC_1UE_TDD125_ABIO_CFG_NSA_DLUL']['First Fail Build']))
print(df.loc['cb8386_MultiUEMultiBearerDL300UL100_8CC_40UE_TDD125_ABIO_CFG_NSA_DLUL']['First Fail Build'])
print(type(df.loc['cb8386_MultiUEMultiBearerDL300UL100_8CC_40UE_TDD125_ABIO_CFG_NSA_DLUL']['First Fail Build']))

def if_cell_exist(row, col):
    if row in df.index.values and col in df.columns.values:
        print('exist')
    else:
        print('NOT exist')

if_cell_exist('cb8386_MultiUEMultiBearerDL300UL100_8CC_1UE_TDD125_ABIO_CFG_NSA_DLUL', 'First Fail Build')
if_cell_exist('cb8386_MultiUEMultiBearerDL300UL100_8CC_1UE_TDD125_ABIO_CFG_NSA_DLUL2', 'First Fail Build')
