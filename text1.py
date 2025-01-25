import requests

# 设置你的个人访问令牌和要访问的仓库
token = 'YOUR_ACCESS_TOKEN'
repo_owner = 'pyinstaller'
repo_name = 'pyinstaller'

# 获取提交信息的 API URL
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'

headers = {
    'Authorization': f'token {token}',
}

response = requests.get(url, headers=headers)
commits = response.json()


"""
数据清晰清洗
"""
import pandas as pd

# 将提交数据转换为 DataFrame
commits=[commits]
df = pd.DataFrame(commits)

# 提取关键信息，如提交的 SHA、作者、提交日期等
cleaned_df = df[['sha', 'commit']].copy()
cleaned_df['author'] = cleaned_df['commit'].apply(lambda x: x['author']['name'])
cleaned_df['date'] = cleaned_df['commit'].apply(lambda x: x['author']['date'])
cleaned_df = cleaned_df[['sha', 'author', 'date']]

# 转换日期格式
cleaned_df['date'] = pd.to_datetime(cleaned_df['date'])



"""
数据分析
"""
# 统计每个作者的提交次数
author_commits = cleaned_df['author'].value_counts()
print(author_commits)

# 按日期统计提交次数
daily_commits = cleaned_df.resample('D', on='date').size()
print(daily_commits)

"""
可视化"""
import matplotlib.pyplot as plt
import seaborn as sns

# 绘制每个作者的提交次数柱状图
plt.figure(figsize=(10, 6))
author_commits.plot(kind='bar', color='skyblue')
plt.xlabel('Author')
plt.ylabel('Number of Commits')
plt.title('Commits per Author')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 绘制每日提交次数折线图
plt.figure(figsize=(12, 6))
daily_commits.plot(kind='line', color='orange')
plt.xlabel('Date')
plt.ylabel('Number of Commits')
plt.title('Daily Commits')
plt.grid(True)
plt.show()