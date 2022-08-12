import pandas as pd

dict = {'cb8386_MultiUEMultiBearerDL300UL100_8CC_1UE_TDD125_ABIO_CFG_NSA_DLUL':24492,
        'cb8386_MultiUEMultiBearerDL300UL100_8CC_40UE_TDD125_ABIO_CFG_NSA_DLUL':24492}

df=pd.DataFrame(dict.items(), columns=['Case', 'First Fail Build'])
df.set_index('Case', inplace=True)
print(df)
#df.set_index(0, inplace=True)
