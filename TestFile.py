import pandas as pd

df = pd.read_csv('/Users/daveweimer/Desktop/WFH/BlackBoston/2020-08-18-Test2.csv',encoding='utf-8-sig')
template_columns = ['NAME','TAB_NAME','SHORT_DESC','DESC1','DESC2','DESC3','DESC4','DESC5','WEBSITE','PIC_URL','THUMB_URL','LAT','LONG']

new_df = pd.DataFrame(columns=template_columns)
new_df['TAB_NAME'] = df['Type']

print(new_df['TAB_NAME'])