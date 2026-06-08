import os
import shutil

def example_annotation():
    """计算学生的平均成绩并返回等级。

    读取一个包含分数的列表，计算其平均值，
    并根据划分标准返回 A、B、C 或 F。

    Args:
        scores (list): 包含整型或浮点型分数的列表。

    Returns:
        str: 对应的成绩等级（如 'A'）。
        
    Raises:
        ValueError: 如果传入的列表为空，则抛出异常。
    """
    pass


def clean_folder(path):
    """Clean all files and folders inside

    Args:
        path: str that indicates the path of folder to be cleaned

    """
    if os.path.exists(path):
        for root, dirs, files in os.walk(path, topdown=False):
        # 1. 删除所有文件
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
        
            # 2. 删除所有子目录
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                os.rmdir(dir_path)
                
                


def copy_file_to(source_dir: str, target_dir: str, target_filename: str):
    # 1. 检查源文件夹是否存在
    if not os.path.exists(source_dir) or not os.path.isdir(source_dir):
        print(f"错误：源文件夹 '{source_dir}' 不存在或不是一个目录。")
        return

    # 2. 如果目标文件夹不存在，则自动创建（os.makedirs 相当于 mkdir -p）
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"已创建目标文件夹: {target_dir}")

    file_found = False

    # 3. 遍历源文件夹下的所有文件名（注意：os.listdir 只返回文件名字符串列表，不含路径）
    for filename in os.listdir(source_dir):
        
        # 4. 检查文件名是否完全匹配
        if filename == target_filename:
            # 拼接出完整的绝对/相对路径
            full_source_path = os.path.join(source_dir, filename)
            full_target_path = os.path.join(target_dir, filename)
            
            # 5. 确保它是一个文件而不是同名文件夹
            if os.path.isfile(full_source_path):
                # 执行复制（目标位置已有同名文件会直接覆盖）
                shutil.copy2(full_source_path, full_target_path)
                
                print(f"成功复制: {full_source_path} -> {full_target_path}")
                file_found = True

    if not file_found:
        print(f"在源文件夹中未找到名为 '{target_filename}' 的文件。")

