import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['BMI'] = df['weight']/((df['height']/100)**2)
df['overweight'] = df['BMI']>25

# 3
df.rename(columns={'cholesterol':'old_chol','gluc':'old_gluc'}, inplace=True)
df['cholesterol'] = df['old_chol'] != True
df['gluc'] = df['old_gluc'] != True

# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars=['cardio'], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])

    # 6
    df_cat = df_cat.value_counts().reset_index(name="total")
    

    # 7
    df_cat = df_cat.sort_values('variable')


    # 8
    fig, ax = plt.subplots(1,2)
    ax = sns.catplot(data=df_cat, x="variable", y="total", hue="value", kind="bar", col="cardio")

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
df = df.drop(columns=['old_chol','old_gluc','BMI'])
new_cols = ['id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke',
       'alco', 'active', 'cardio', 'overweight']
df = df.reindex(new_cols, axis='columns')

def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = round(df_heat.corr(), 1 )

    # 13
    mask = np.triu(np.ones_like(corr)).astype(bool)



    # 14
    fig, ax = plt.subplots(1,1, figsize=(8, 8))

    # 15
    ax = sns.heatmap(corr, annot=True, fmt='.1f', linewidth=.5, mask=mask)


    # 16
    fig.savefig('heatmap.png')
    return fig
