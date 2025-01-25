import requests
import pandas as pd
import matplotlib.pyplot as plt

# 设置你的个人访问令牌和要访问的仓库
token = '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'  # token!!!
repo_owner = 'pyinstaller'
repo_name = 'pyinstaller'

# 获取提交信息的 API URL
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'

headers = {
    'Authorization': f'token {token}',
}

# 发送请求
response = requests.get(url, headers=headers)

# 检查响应状态码
if response.status_code == 200:
    commits = response.json()
    print("Commits data structure:", commits)

    # 提取关键信息
    commit_data = []
    for commit in commits:
        # 确保 commit 是一个字典
        if isinstance(commit, dict):
            sha = commit.get('sha')
            author_name = commit.get('commit', {}).get('author', {}).get('name')
            author_date = commit.get('commit', {}).get('author', {}).get('date')
            commit_data.append({
                'sha': sha,
                'author': author_name,
                'date': author_date
            })

    # 将提取的数据转换为 DataFrame
    df = pd.DataFrame(commit_data)

    # 转换日期格式
    df['date'] = pd.to_datetime(df['date'])

    # 数据分析
    # 统计每个作者的提交次数
    author_commits = df['author'].value_counts()
    print("Commits per author:")
    print(author_commits)

    # 按日期统计提交次数
    daily_commits = df.resample('D', on='date').size()
    print("Daily commits:")
    print(daily_commits)

    # 可视化
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
else:
    print("Failed to fetch commits. Status code:", response.status_code)
    print("Response:", response.json())




"""
关键点解释
URL 格式：
确保 url 是一个有效的字符串，而不是带有 HTML 标签或转义字符的格式。
访问令牌：
确保你的 GitHub 个人访问令牌是有效的，并且具有足够的权限（例如 repo 或 read:org）。
错误处理：
检查响应状态码，确保请求成功。如果状态码不是 200，打印错误信息。
数据提取：
使用嵌套的 get 方法安全地提取嵌套字典中的数据。
数据分析和可视化：
使用 Pandas 进行数据分析，使用 Matplotlib 进行可视化。
"""