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

print(type(commits))
print(commits)
