import os

def generate_readme(rpk_directory, readme_path, title="动态表盘", main_readme_link="../README.md"):
    # 定义链接地址前缀
    url_prefix = "https://github.akams.cn/https://github.com/tian1326/BlueOS-App-Library/raw/refs/heads/main/"
    
    # 获取指定目录下的所有.rpk文件
    rpk_files = [f for f in os.listdir(rpk_directory) if f.endswith('.rpk')]
    
    # 生成README内容
    with open(readme_path, 'w', encoding='utf-8') as readme_file:
        readme_file.write(f"# {title} [返回主目录]({main_readme_link})\n\n")
        readme_file.write(f"以下是{title}的相关应用：\n\n")
        
        for rpk_file in rpk_files:
            file_name = os.path.splitext(rpk_file)[0]
            file_link = f"{url_prefix}{title}/{rpk_file.replace(' ', '%20')}"
            readme_file.write(f"- [{file_name}.rpk](#{file_name.replace(' ', '-')})\n")
        
        readme_file.write("\n")
        
        for rpk_file in rpk_files:
            file_name = os.path.splitext(rpk_file)[0]
            file_link = f"{url_prefix}{title}/{rpk_file.replace(' ', '%20')}"
            readme_file.write(f"### {file_name}.rpk <a name=\"{file_name}\"></a>\n")
            readme_file.write(f"[下载地址]({file_link})\n\n")

    print("README文件已更新")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))  # 获取脚本所在目录
    
    # 动态表盘
    rpk_directory = os.path.join(script_dir, "表盘", "动态表盘")
    readme_path = os.path.join(script_dir, "docs", "表盘", "动态表盘", "README.md")
    generate_readme(rpk_directory, readme_path, title="表盘/动态表盘", main_readme_link="../../README.md")
    
    # 普通表盘
    rpk_directory = os.path.join(script_dir, "表盘", "普通表盘")
    readme_path = os.path.join(script_dir, "docs", "表盘", "普通表盘", "README.md")
    generate_readme(rpk_directory, readme_path, title="表盘/普通表盘", main_readme_link="../../../README.md")
    
    # 工具类
    rpk_directory = os.path.join(script_dir, "工具类")
    readme_path = os.path.join(script_dir, "docs", "工具类", "README.md")
    generate_readme(rpk_directory, readme_path, title="工具类")
    
    # 娱乐类
    rpk_directory = os.path.join(script_dir, "娱乐类")
    readme_path = os.path.join(script_dir, "docs", "娱乐类", "README.md")
    generate_readme(rpk_directory, readme_path, title="娱乐类")