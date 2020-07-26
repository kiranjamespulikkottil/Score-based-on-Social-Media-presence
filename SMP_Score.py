# *****Please keep the script in the same folder as the 'Social Score Assignment.xlsx' file******

import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
# import matplotlib.pyplot as plt

pd.set_option('mode.chained_assignment', None)


# Reading the xlsx scrapped files and storing them into a dataframe for each week
df_Dec_week1 = pd.read_excel(
    'Social Score Assignment.xlsx', sheet_name='Dec_week1')
df_Dec_week2 = pd.read_excel(
    'Social Score Assignment.xlsx', sheet_name='Dec_week2')
df_Dec_week3 = pd.read_excel(
    'Social Score Assignment.xlsx', sheet_name='Dec_week3')
df_Dec_week4 = pd.read_excel(
    'Social Score Assignment.xlsx', sheet_name='Dec_week4')

# appending all the data to a single dataframe
data_frames = [df_Dec_week1, df_Dec_week2, df_Dec_week3, df_Dec_week4]
final_df = pd.DataFrame()
for data in data_frames:
    final_df = final_df.append(data)

# Creating dataframes for each social platform to perform analysis
final_df = final_df[['brand', 'dislike', 'likes', 'retweet',
                     'shareCount', 'videoDuration', 'views', 'Channel']]

df_youtube = final_df[final_df['Channel'] == 'youtube'][[
    'brand', 'dislike', 'likes', 'views', 'Channel']]
df_facebook = final_df[final_df['Channel'] == 'facebook']
df_twitter = final_df[final_df['Channel'] == 'twitter']
df_instagram = final_df[final_df['Channel'] == 'instagram']


# Computing Youtube Popularity Scores
df_youtube['views'] = df_youtube['views'].astype(
    str).str.replace(',', '').astype(int)
df_you = df_youtube.groupby('brand').sum().reset_index()
df_you['total'] = df_you['views'] + df_you['likes'] - df_you['dislike']
df_you['popularity percentage'] = (df_you['total']/(df_you['total'].sum()))*100
df_you['Channel'] = 'youtube'

print('\n\nYoutube popularity score for the month of December for three differnet brands \n')
print(df_you)


# Computing Facebook Popularity Scores
df_facebook = df_facebook[['brand', 'likes', 'shareCount']]
df_fb = df_facebook.groupby('brand').sum().reset_index()
df_fb['total'] = df_fb['likes'] + df_fb['shareCount']
df_fb['popularity percentage'] = (
    (df_fb['total']/(df_fb['total'].sum()))*100).round(decimals=2)
df_fb['Channel'] = 'Facebook'

print('\n\nFacebook popularity score for the month of December for three differnet brands \n')
print(df_fb)


# Computing Twitter Popularity Scores
df_twit = df_twitter[['brand', 'likes', 'retweet']]
df_twit = df_twit.groupby('brand').sum().reset_index()
df_twit['total'] = df_twit['likes'] + df_twit['retweet']
df_twit['popularity percentage'] = (
    (df_twit['total']/(df_twit['total'].sum()))*100).round(decimals=2)
df_twit['Channel'] = 'Twitter'

print('\n\nTwitter popularity score for the month of December for three differnet brands \n')
print(df_twit)


# Computing Instagram Popularity Scores
df_insta = df_instagram[['brand', 'views', 'likes']]
df_insta['likes'] = df_insta['likes'].astype(int).astype(object)
df_insta = df_insta.groupby('brand').sum().reset_index()
df_insta['total'] = df_insta['likes'] + df_insta['views']
df_insta['popularity percentage'] = (
    (df_insta['total']/(df_insta['total'].sum()))*100).round(decimals=2)
df_insta['Channel'] = 'Instagram'

print('\n\nInstagram popularity score for the month of December for three differnet brands \n')
print(df_insta)


# Computing the Final popularity score
popularity_list = [df_you, df_fb, df_twit, df_insta]
df_popularity = pd.DataFrame()
for items in popularity_list:
    df_popularity = df_popularity.append(
        items[['brand', 'popularity percentage']])
df_popularity = df_popularity.groupby('brand').mean().reset_index()

print('\n\nBrand Popularity in Social Media Platforms \n')
print(df_popularity)

# Visualizing the Final dataframe
#df_popularity.plot(x='brand', y='popularity percentage', title='Brand Popularity in Social Media Platforms', fontsize=25, kind='pie', figsize=(10,15), labels=df_popularity.brand)
#plt.legend(prop={'size': 15})
#plt.title('Brand Popularity in Social Media Platforms', fontsize=20)
