#!/usr/bin/env python3

import os
import shutil

def organize_files_by_extension(directory):
    rules = {
        'images': ['.jpg', '.jpeg', '.png', '.gif'],
        'documents': ['.pdf', '.docx', '.txt'],
        'videos': ['.mp4', '.avi', '.mkv'],
        'audio': ['.mp3', '.wav', '.aac'],
        'code': ['.py', '.js', '.html', '.css', '.java', '.cpp'],
        'others': []
    }

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            for category, extensions in rules.items():
                if ext.lower() in extensions:
                    category_path = os.path.join(directory, category)
                    os.makedirs(category_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_path, filename))
                    break
                else:
                    category_path = os.path.join(directory, 'others')
                    os.makedirs(category_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_path, filename))
                    break

if __name__ == "__main__":
    target_directory = input("请输入要整理的目录路径：")
    if os.path.isdir(target_directory):
        organize_files_by_extension(target_directory)
        print("文件整理完成！")
    else:
        print("无效的目录路径，请重新输入。")