import os
import re
import json
import shutil

def generate_readme(rpk_directory, readme_path, title, main_readme_link):
    # 定义链接地址前缀
    url_prefix = "https://github.akams.cn/https://github.com/tian1326/BlueOS-App-Library/raw/refs/heads/main/"
    
    # 获取指定目录下的所有.rpk文件
    rpk_files = [f for f in os.listdir(rpk_directory) if f.endswith('.rpk')]
    
        # 生成README内容
    try:
        with open(readme_path, 'w', encoding='utf-8') as readme_file:
            readme_file.write(f"# {title} [返回主目录]({main_readme_link})\n\n")
            readme_file.write(f"以下是{title}的相关应用：\n\n")
            
            for rpk_file in rpk_files:
                file_name = os.path.splitext(rpk_file)[0]
                json_path = os.path.join(script_dir, "docs", os.path.relpath(rpk_directory, script_dir), f"{file_name}.json")
                
                if os.path.exists(json_path):
                    with open(json_path, 'r', encoding='utf-8') as json_file:
                        json_data = json.load(json_file)
                        software_name = json_data.get("software_name", file_name)
                        screen_type = json_data.get("screen_type", "未知")
                        verified_devices = ", ".join(json_data.get("verified_devices", ["未知"]))
                        author = json_data.get("author", "未知")
                        sponsor_image_url = json_data.get("sponsor_image_url", "无")
                        screenshot_url = json_data.get("screenshot_url", "无")
                else:
                    software_name = file_name
                    screen_type = "未知"
                    verified_devices = "未知"
                    author = "未知"
                    sponsor_image_url = "无"
                    screenshot_url = "无"
                
                file_link = f"{url_prefix}{title}/{rpk_file.replace(' ', '%20')}"
                readme_file.write(f"- [{software_name}.rpk](#{software_name.replace(' ', '-')})\n")
            
            readme_file.write("\n")
            
            for rpk_file in rpk_files:
                file_name = os.path.splitext(rpk_file)[0]
                json_path = os.path.join(script_dir, "docs", os.path.relpath(rpk_directory, script_dir), f"{file_name}.json")
                
                if os.path.exists(json_path):
                    with open(json_path, 'r', encoding='utf-8') as json_file:
                        json_data = json.load(json_file)
                        software_name = json_data.get("software_name", file_name)
                        screen_type = json_data.get("screen_type", "未知")
                        verified_devices = ", ".join(json_data.get("verified_devices", ["未知"]))
                        author = json_data.get("author", "未知")
                        sponsor_image_url = json_data.get("sponsor_image_url", "无")
                        screenshot_url = json_data.get("screenshot_url", "无")
                else:
                    software_name = file_name
                    screen_type = "未知"
                    verified_devices = "未知"
                    author = "未知"
                    sponsor_image_url = "无"
                    screenshot_url = "无"
                
                file_link = f"{url_prefix}{title}/{rpk_file.replace(' ', '%20')}"
                readme_file.write(f"### {software_name}.rpk <a name=\"{software_name}\"></a>\n")
                readme_file.write(f"[下载地址]({file_link})\n\n")
                readme_file.write(f"**屏幕类型**: {screen_type}\n\n")
                readme_file.write(f"**已验证设备**: {verified_devices}\n\n")
                readme_file.write(f"**作者**: {author}\n\n")
                readme_file.write(f"**赞助图片地址**: {sponsor_image_url}\n\n")
                readme_file.write(f"**效果图地址**: {screenshot_url}\n\n")
    except Exception as e:
        raise Exception(f"生成README文件失败: {readme_path}") from e

    print(f"README文件已更新: {readme_path}")

def generate_rpk_list(rpk_directory, list_path):
    # 获取指定目录下的所有.rpk文件
    rpk_files = [f for f in os.listdir(rpk_directory) if f.endswith('.rpk')]
    
    # 生成list.txt内容
    try:
        with open(list_path, 'w', encoding='utf-8') as list_file:
            for rpk_file in rpk_files:
                list_file.write(f"{rpk_file}\n")
    except Exception as e:
        raise Exception(f"生成list.txt文件失败: {list_path}") from e

    print(f"list.txt文件已更新: {list_path}")

def generate_combined_rpk_list(categories, combined_list_path):
    all_rpk_files = []
    
    for category in categories:
        rpk_directory = category['rpk_directory']
        rpk_files = [f for f in os.listdir(rpk_directory) if f.endswith('.rpk')]
        all_rpk_files.extend(rpk_files)
    
    # 生成list.txt内容
    try:
        with open(combined_list_path, 'w', encoding='utf-8') as list_file:
            for rpk_file in all_rpk_files:
                list_file.write(f"{rpk_file}\n")
    except Exception as e:
        raise Exception(f"生成combined_list.txt文件失败: {combined_list_path}") from e

    print(f"combined_list.txt文件已更新: {combined_list_path}")

def rename_rpk_files(rpk_directory):
    for filename in os.listdir(rpk_directory):
        if filename.endswith('.rpk'):
            new_filename = re.sub(r'\s+', '_', filename)  # 将空格替换为下划线
            new_filename = re.sub(r'（', '(', new_filename)  # 将中文左括号替换为英文左括号
            new_filename = re.sub(r'）', ')', new_filename)  # 将中文右括号替换为英文右括号
            
            if new_filename != filename:
                old_file_path = os.path.join(rpk_directory, filename)
                new_file_path = os.path.join(rpk_directory, new_filename)
                try:
                    os.rename(old_file_path, new_file_path)
                    print(f"文件重命名: {old_file_path} -> {new_file_path}")
                except Exception as e:
                    raise Exception(f"重命名文件失败: {old_file_path} -> {new_file_path}") from e

def infer_screen_type(file_name):
    if "方屏" in file_name or "方表" in file_name:
        return "方屏"
    elif "圆屏" in file_name or "圆表" in file_name:
        return "圆屏"
    elif "方屏/圆屏" in file_name or "方表/圆表" in file_name:
        return "方屏/圆屏"
    else:
        return "未知"
def generate_json_for_rpk(rpk_directory, script_dir):
    for filename in os.listdir(rpk_directory):
        if filename.endswith('.rpk'):
            file_name = os.path.splitext(filename)[0]
            json_path = os.path.join(script_dir, "docs", os.path.relpath(rpk_directory, script_dir), f"{file_name}.json")
            
            if not os.path.exists(json_path):
                screen_type = infer_screen_type(file_name)
                json_data = {
                    "software_name": file_name,
                    "screen_type": screen_type,
                    "verified_devices": ["未知"],
                    "author": "未知",
                    "sponsor_image_url": "无",
                    "screenshot_url": "无"
                }
                
                os.makedirs(os.path.dirname(json_path), exist_ok=True)
                with open(json_path, 'w', encoding='utf-8') as json_file:
                    json.dump(json_data, json_file, ensure_ascii=False, indent=4)
                print(f"生成JSON文件: {json_path}")

def explore_directories(base_directory, script_dir, categories):
    for root, dirs, files in os.walk(base_directory):
        rpk_files = [f for f in files if f.endswith('.rpk')]
        if rpk_files:
            relative_path = os.path.relpath(root, base_directory)
            docs_path = os.path.join(script_dir, "docs", relative_path)
            os.makedirs(docs_path, exist_ok=True)
            readme_path = os.path.join(docs_path, "README.md")
            list_path = os.path.join(docs_path, "list.txt")
            title = relative_path.replace(os.sep, '/')
            main_readme_link = os.path.join(*(['..'] * (relative_path.count(os.sep) + 1)), "README.md")
            categories.append({
                "rpk_directory": root,
                "readme_path": readme_path,
                "list_path": list_path,
                "title": title,
                "main_readme_link": main_readme_link
            })

def clean_generated_files(categories, combined_list_path):
    # 删除之前生成的README.md和list.txt文件
    for category in categories:
        readme_path = category['readme_path']
        list_path = category['list_path']
        if os.path.exists(readme_path):
            os.remove(readme_path)
            print(f"删除文件: {readme_path}")
        if os.path.exists(list_path):
            os.remove(list_path)
            print(f"删除文件: {list_path}")
    
    # 删除combined_list.txt文件
    if os.path.exists(combined_list_path):
        os.remove(combined_list_path)
        print(f"删除文件: {combined_list_path}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))  # 获取脚本所在目录
    base_directory = script_dir  # 设置要探索的基目录为脚本所在目录

    categories = []
    explore_directories(base_directory, script_dir, categories)

    combined_list_path = os.path.join(script_dir, "docs", "combined_list.txt")

    try:
        # 重命名所有.rpk文件
        for category in categories:
            rename_rpk_files(category['rpk_directory'])

        for category in categories:
            generate_readme(category['rpk_directory'], category['readme_path'], category['title'], category['main_readme_link'])
            generate_rpk_list(category['rpk_directory'], category['list_path'])
            generate_json_for_rpk(category['rpk_directory'], script_dir)  # 生成JSON文件

        generate_combined_rpk_list(categories, combined_list_path)
    except Exception as e:
        print(f"发生错误: {e}")
        clean_generated_files(categories, combined_list_path)