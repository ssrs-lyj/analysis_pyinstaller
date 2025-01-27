import requests
import pandas as pd
import matplotlib.pyplot as plt
import random
import string
# 定义模糊测试的输入
def generate_fuzzy_data():
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=40))
    repo_owner = ''.join(random.choices(string.ascii_letters, k=10))
    repo_name = ''.join(random.choices(string.ascii_letters, k=10))
    return token, repo_owner, repo_name

# 模糊测试函数
def fuzzy_test():
    for _ in range(1000):  # 进行1000次模糊测试
        token, repo_owner, repo_name = generate_fuzzy_data()
        url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'
        headers = {
            'Authorization': f'token {token}',
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            commits = response.json()
            print("Commits data structure:", commits)
        else:
            print("Failed to fetch commits. Status code:", response.status_code)
            print("Response:", response.json())
# 执行模糊测试
fuzzy_test()
