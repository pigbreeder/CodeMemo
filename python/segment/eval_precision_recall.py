# 评测各个类别质量
import pandas as pd
pd.set_option('display.width', 1000)
baseline_label = 'baseline'
predict_label = 'predict'

a=df[predict_label].value_counts()
b=df[baseline_label].value_counts()
c=df[(df[predict_label].str.strip() == df[baseline_label].str.strip())][baseline_label].value_counts()
c.name='true'
all_df=pd.concat([a,b,c],axis=1).reset_index()
all_df['precision']=all_df['true']/all_df[predict_label]
all_df['recall']=all_df['true']/all_df[baseline_label]
# add tot
data={'index':'总计',baseline_label:all_df[baseline_label].sum(),predict_label:all_df[predict_label].sum(),'true':all_df['true'].sum(),\
              'precision':all_df['true'].sum()/all_df[predict_label].sum(),'recall':all_df['true'].sum()/all_df[baseline_label].sum()}
tmp_df = pd.DataFrame(data,index=[100])
all_df.append(tmp_df)
