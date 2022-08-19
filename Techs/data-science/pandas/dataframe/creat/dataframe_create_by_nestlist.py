import pandas as pd

nest_list = [['cb8386_MultiUEMultiBearerDL300UL100_8CC_1UE_TDD125_ABIO_CFG_NSA_DLUL', 24492],
             ['cb8386_MultiUEMultiBearerDL300UL100_8CC_40UE_TDD125_ABIO_CFG_NSA_DLUL', 24492]]
print("nest list:")
print(nest_list)

df=pd.DataFrame(nest_list, columns=['Case', 'First Fail Build'])
print("dataframe created by nest list:")
print(df)

l = [['a', 'b', 'c', 'd'],
     [1, 2, 3, 4],
     ['i', 'j', 'k', 'l']]
df = pd.DataFrame(l)
print(df)

df2 = pd.DataFrame(l, index=['i1', 'i2', 'i3'], columns=['c1', 'c2', 'c3', 'c4'])
print(df2)
