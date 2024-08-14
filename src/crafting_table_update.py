import os
import json

def help():
	print('==操作说明==')
	print('r 2 # 读取第2个合成表')
	print('r 石矿 # 读取石矿建筑的合成表')
	print('w 石矿 # 更新石矿建筑的合成表')
	print('s # 保存并推出')
	print('h # 输出帮助信息')

def write_ui(building_name):
	table_out = input(f'请输入"{building_name}"建筑的产物名称：\n')
	table_in = input(f'请输入"{building_name}"建筑的输入物品名称，多个物品名称以空格隔开：\n').split()
	table_ratio = input(f'请输入"{building_name}"建筑输入物品与产物的比例。\n例如，1个水和2个木板产生3个产物，则输入"1 2 3"\n').split()
	table_ratio = [int(r) for r in table_ratio]
	table_cd = int(input(f'请输入"{building_name}"建筑的冷却时间（秒）：\n'))
	return [building_name, table_out, table_in, table_ratio, table_cd]

crafting_table = []

# 提示用户输入文件名
file_name = input('请输入合成表JSON文件名：')
if file_name[-5:] != '.json':
	file_name += '.json'

# 文件若存在，读取现有合成表
if os.path.exists(file_name):
	with open(file_name, 'r') as file:
		crafting_table = json.load(file)
		print(f'已读取{len(crafting_table)}个合成表')

# 输出操作说明
help()

instruction = input().split()
while instruction[0] != "s":
	if instruction[0][0] == 'h':
		help()
	elif instruction[0] == 'r':
		pass # TBD
	elif instruction[0] == 'w':
		crafting_table.append(write_ui(instruction[1]))
	else:
		print('未知命令，输入h查看帮助信息')

	instruction = input('请输入指令\n').split()

# 将更新后的合成表存入文件中
with open(file_name, 'w') as file:
   	json.dump(crafting_table, file)

