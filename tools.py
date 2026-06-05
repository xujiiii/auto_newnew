import os


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