import json


def process_data(input_file_path):
    # 读取原始数据
    with open(input_file_path, "r") as file:
        original_data = json.load(file)

    # 新格式的数据列表
    formatted_data = []

    # 遍历原始数据
    for entry in original_data:
        merged_entry = []
        instruction = entry["instruction"] + entry["input"]
        history = entry["history"]

        # 合并指令和历史记录
        merged_entry.append(instruction)
        merged_entry.append(entry["output"])

        # 添加历史记录
        for pair in history[1:]:
            for item in pair:
                merged_entry.append(item)

        # 添加布尔值列表
        boolean_flags = [True, False] * len(history)
        formatted_entry = [merged_entry, boolean_flags]
        formatted_data.append(formatted_entry)

    # 将转换后的数据写入文件
    with open(input_file_path, "w") as file:
        json.dump(formatted_data, file, indent=4)

    print(f"数据已成功转换并写入到文件：{input_file_path}")


# 指定输入和输出文件路径
train_file_path = "./dbgpt_hub_gql/data/example_text2sql_train.json"
dev_file_path = "./dbgpt_hub_gql/data/example_text2sql_dev.json"
# 处理数据
process_data(train_file_path)
process_data(dev_file_path)
