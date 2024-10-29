import os

def count_line(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for l in file if l.strip()) # 只計算非空行

levelList = []
def count_total_in_all_file(folder_path, program_type):
    total_lines = 0
    base_level = folder_path.rstrip(os.sep).count(os.sep)  # 基準層級
    for root, _, files in os.walk(folder_path):
        cur_folder_level = root.count(os.sep) - base_level + 1
        tell_level_time = 0
        for file in files:
            if any(file.endswith(pType) for pType in program_type):
                file_path = os.path.join(root, file)
                lines = count_line(file_path)
                if tell_level_time == 0 and cur_folder_level not in levelList:
                    print(f'Below is file that matched in {cur_folder_level} level: ')
                    levelList.append(cur_folder_level)
                tell_level_time = 1
                print(f'{file_path} has {lines} lines without whitespace line !!')
                total_lines += lines
    return total_lines
            
folder_path = input("請輸入資料夾路徑：")
program_type_input = input("請輸入要納入計算的程式檔種類（輸入格式請用半形的空格符分隔，如c py txt）：")

program_type = [ext.strip() for ext in program_type_input.split(' ') if ext.strip()] # 忽略多於空格
# print(program_type)

# Calculation
# 檢查 folder_path 是檔案還是資料夾
if os.path.isfile(folder_path):  # 如果是檔案
    if any(folder_path.endswith(ext) for ext in program_type):
        # 計算單個檔案的行數
        total_lines = count_line(folder_path)
        print(f"檔案 {os.path.basename(folder_path)} 的行數: {total_lines} 行")
    else:
        print("指定的檔案類型不符合要求")
elif os.path.isdir(folder_path):  # 如果是資料夾
    # 計算資料夾內符合條件的檔案總行數
    total_lines = count_total_in_all_file(folder_path, program_type)
else:
    print("無法找到指定的檔案或資料夾。請確認路徑是否正確。")