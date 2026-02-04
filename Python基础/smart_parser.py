import pandas as pd
# text = open('projects_requirements.md',encoding='utf-8').read()
# # print(text)
# projects = ['项目' + p for p in text.split('项目')[1:]]
# pd.DataFrame({'项目需求': projects}).to_excel('projects.xlsx')
# # print(projects)

# df = pd.read_excel('projects.xlsx')
# for i, row in df.iterrows():
#     with open(f'{i:03d}_project.py', 'w',encoding='utf-8') as f:
#         f.write(f'"""\n{row["项目需求"]}\n"""')

# df = pd.read_excel('projects.xlsx')
# for i, row in df.iterrows():
#     # 取第一行的"项目1："后面的部分作为项目名
#     first_line = str(row["项目需求"]).split('\n')[0]
#     project_name = first_line.split('：')[1].strip().replace(' ', '-')
#
#     with open(f'{i + 1:03d}-{project_name}.py', 'w', encoding='utf-8') as f:
#         f.write(f'"""\n{row["项目需求"]}\n"""')

import pandas as pd

df = pd.read_excel('projects.xlsx')

for i, row in df.iterrows():
    content = str(row["项目需求"])

    # 安全的提取项目名
    project_name = "project"  # 默认值

    # 方法1：按冒号分割
    if '：' in content:
        first_line = content.split('\n')[0]
        parts = first_line.split('：')
        if len(parts) > 1:
            project_name = parts[1].strip().replace(' ', '-')

    # 方法2：如果冒号分割失败，尝试其他分隔符
    elif ':' in content:
        first_line = content.split('\n')[0]
        parts = first_line.split(':')
        if len(parts) > 1:
            project_name = parts[1].strip().replace(' ', '-')

    # 清理文件名（移除非法字符）
    illegal_chars = '<>:"/\\|?*'
    for char in illegal_chars:
        project_name = project_name.replace(char, '')

    # 生成文件名
    filename = f'{i + 1:03d}-{project_name}.py'

    # 写入文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f'"""\n{content}\n"""')

    print(f"生成: {filename}")