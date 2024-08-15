import json

class CraftingTable():
	"""docstring for CraftingTable"""
	def __init__(self, file_name):
		self.table = []	# 建筑名 产物名 输入物品名称列表 输入与输出比例列表 建筑冷却时间
		with open(file_name, 'r') as file:
			self.table = json.load(file)
		self.disable_building_list = []

	def show(self, building_name):
		for t in self.table:
			if t[0] == building_name:
				description = f'{t[0]}: '
				for i, r in enumerate(t[2]):
					description += f'{t[3][i]} * {r} + '
				if len(t[2]) > 0:
					description = description[:-2]
				description += f'-> {t[3][-1]} * {t[1]} '
				description += f'/ {t[4]} s'
				return description
		return ''

	def building_list(self):
		return [t[0] for t in self.table]

	def resource_list(self):
		return list(set([t[1] for t in self.table]))

	def output_name(self, building_name):
		for t in self.table:
			if t[0] == building_name:
				return t[1]
		return ''

	def input_name_list(self, building_name):
		for t in self.table:
			if t[0] == building_name:
				return t[2]
		return []

	def output_speed(self, building_name):
		ratio = []
		cd = 0
		for t in self.table:
			if t[0] == building_name:
				ratio = t[3]
				cd = t[4]
				if 'Population' in t[1] or '人口' in t[1]:
					return ratio[-1]
				else:
					return ratio[-1] * 60 / cd
		return 0

	def input_speed_list(self, building_name, output_speed=0):
		ratio = []
		cd = 0
		for t in self.table:
			if t[0] == building_name:
				ratio = t[3]
				cd = t[4]
				if output_speed == 0:
					if 'Population' in t[1] or '人口' in t[1]:
						input_type_num = len(ratio) - 1
						return [r * 60 / cd / input_type_num for r in ratio[:-1]]
					else:
						return [r * 60 / cd  for r in ratio[:-1]]
				else:
					if 'Population' in t[1] or '人口' in t[1]:
						input_type_num = len(ratio) - 1
						return [output_speed * r * 60 / cd / input_type_num  / ratio[-1] for r in ratio[:-1]]
					else:
						return [output_speed * r / ratio[-1]  for r in ratio[:-1]]
		return []

	def input_speed(self, building_name, input_name, output_speed=0):
		ratio = []
		cd = 0
		for t in self.table:
			if t[0] == building_name:
				ratio = t[3]
				cd = t[4]
				input_index = t[2].index(input_name)
				if output_speed == 0:
					if 'Population' in t[1] or '人口' in t[1]:
						input_type_num = len(ratio) - 1
						return ratio[input_index] * 60 / cd / input_type_num
					else:
						return ratio[input_index] * 60 / cd 
				else:
					if 'Population' in t[1] or '人口' in t[1]:
						input_type_num = len(ratio) - 1
						return output_speed * ratio[input_index] * 60 / cd / input_type_num  / ratio[-1]
					else:
						return output_speed * ratio[input_index] / ratio[-1] 
		return 0
		
	def maker_find(self, resource_name):
		maker_list = []
		for t in self.table:
			if t[1] == resource_name:
				if t[0] not in self.disable_building_list:
					maker_list.append(t[0])
		return maker_list

	def all_maker_find(self, resource_name):
		maker_list = []
		for t in self.table:
			if t[1] == resource_name:
				# if t[0] not in self.disable_building_list:
				maker_list.append(t[0])
		return maker_list

	def user_find(self, resource_name):
		user_list = []
		for t in self.table:
			if resource_name in t[2]:
				if t[0] not in self.disable_building_list:
					user_list.append(t[0])
		return user_list
	
	def disable_building(self, building_list):
		self.disable_building_list += building_list
		self.disable_building_list = list(set(self.disable_building_list))
		return self.disable_building_list