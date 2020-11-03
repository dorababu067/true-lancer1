import pandas as pd

def convert_df_to_html(field='f1'):
    excel_file = pd.ExcelFile('C:/Users/Alapakam Dorababu/Documents/static_data.xlsx') 
    
    # Load the excel_file's back-end as a dataframe 
    df = excel_file.parse('back-end') 
    # print(df)
    filter_df = df[['category','asset',field]]
    # print(filter_df)
    data = []
    assets = [asset for asset in df['asset'].iloc[0:20]]
    cat1  = filter_df.loc[df['category'].isin(['CAT1'])]
    cat2  = filter_df.loc[df['category'].isin(['CAT2'])]
    cat3  = filter_df.loc[df['category'].isin(['CAT3'])]
    cat4  = filter_df.loc[df['category'].isin(['CAT4'])]
   
    for a, c1, c2, c3, c4 in zip(assets, cat1[field].to_list(), cat2[field].to_list(), cat3[field].to_list(), cat4[field].to_list()):
        data.append({"Asset":a, "CAT1":c1, "CAT2":c2, "CAT3":c3, "CAT4":c4})

    final_df = pd.DataFrame(data)
    # print(final_df)
    output = final_df.to_html(classes="table table-bordered table-hover")
    return final_df, output



















# print(data)
# print(df)
# data = []
# cat1  = df.loc[df['category'].isin(['CAT1'])]
# data.append(cat1.iloc[0].to_list())
# print(cat1.iloc[0].to_list())
# cat2  = df.loc[df['category'].isin(['CAT2'])]
# data.append(cat2.iloc[0].to_list())
# cat3  = df.loc[df['category'].isin(['CAT3'])]
# data.append(cat3.iloc[0].to_list())
# cat4  = df.loc[df['category'].isin(['CAT4'])]
# # data.append(cat4.iloc[0].to_list())

# newdf = pd.DataFrame(data)
# print(newdf)