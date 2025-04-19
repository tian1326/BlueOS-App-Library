import os
import hashlib
import json

def calculate_md5(file_path):
    """计算文件的 MD5 值"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def infer_screen_type(file_name):
    if "方屏" in file_name or "方表" in file_name:
        return "方屏"
    elif "圆屏" in file_name or "圆表" in file_name:
        return "圆屏"
    elif "方屏/圆屏" in file_name or "方表/圆表" in file_name:
        return "方屏/圆屏"
    else:
        return "未知"

def generate_json_for_rpk(rpk_directory, script_dir, title):
    for filename in os.listdir(rpk_directory):
        if filename.endswith('.rpk'):
            file_name = os.path.splitext(filename)[0]
            json_path = os.path.join(script_dir, "docs", os.path.relpath(rpk_directory, script_dir), f"{file_name}.json")
            rpk_file_path = os.path.join(rpk_directory, filename)
            img_path = os.path.join(script_dir, "img", f"{file_name}.png")  # 假设图片扩展名为 .png
            
            if not os.path.exists(json_path):
                screen_type = infer_screen_type(file_name)
                download_url = f"https://github.akams.cn/https://github.com/tian1326/BlueOS-App-Library/raw/refs/heads/main/{title}/{filename.replace(' ', '%20')}"
                md5_value = calculate_md5(rpk_file_path)  # 计算 MD5 值
                screenshot_url = f"../img/{file_name}.png" if os.path.exists(img_path) else "../img/无.png"  # 添加图片路径
                
                json_data = {
                    "software_name": file_name,
                    "screen_type": screen_type,
                    "verified_devices": ["未知"],
                    "author": "未知",
                    "sponsor_image_url": "无",
                    "screenshot_url": screenshot_url,
                    "download_url": download_url,
                    "md5": md5_value  # 添加 MD5 值
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
            title = relative_path.replace(os.sep, '/')
            categories.append({
                "rpk_directory": root,
                "title": title
            })

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))  # 获取脚本所在目录
    base_directory = script_dir  # 设置要探索的基目录为脚本所在目录

    categories = []
    explore_directories(base_directory, script_dir, categories)

    try:
        for category in categories:
            generate_json_for_rpk(category['rpk_directory'], script_dir, category['title'])
    except Exception as e:
        print(f"发生错误: {e}")