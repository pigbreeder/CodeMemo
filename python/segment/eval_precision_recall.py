# 评测各个类别质量
def func_report(df, baseline_label='标注二级知识点', predict_label='label'):
    #baseline_label = '标注二级知识点'
    #predict_label = 'label'
    
    a=df[predict_label].value_counts()
    b=df[baseline_label].value_counts()
    c=df[(df[predict_label].str.strip() == df[baseline_label].str.strip())][baseline_label].value_counts()
    c.name='true'
    
    all_df=pd.concat([a,b,c],axis=1).reset_index()
    
    all_df['precision']=all_df['true']/all_df[predict_label]
    all_df['recall']=all_df['true']/all_df[baseline_label]
    all_df['F1']= 2/(1/all_df['precision'] + 1/all_df['recall'])
    # add tot
    data={'index':'总计',baseline_label:all_df[baseline_label].sum(),predict_label:all_df[predict_label].sum(),'true':all_df['true'].sum(),\
                  'precision':all_df['true'].sum()/all_df[predict_label].sum(),'recall':all_df['true'].sum()/all_df[baseline_label].sum()}
                  
    tmp_df = pd.DataFrame(data,index=[100])
    return all_df.append(tmp_df)