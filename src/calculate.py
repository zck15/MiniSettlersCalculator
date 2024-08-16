from crafting_table import *

class Calculator():
	"""docstring for Calculator"""
	def __init__(self, target_name, target_speed, crafting_table_name='buildings.json'):
		self.target_name = target_name
		self.target_speed = target_speed
		self.crafting_table = CraftingTable(crafting_table_name)
		self.input_resources_list = []

	def crafting_table_select(self):
		self.crafting_table.disable_building_list = self.crafting_table.building_list()
		self.resources_produced = []
		resources_tbp = [name for name in self.target_name]
		while len(resources_tbp) > 0:
			r = resources_tbp.pop()
			maker_list = self.crafting_table.all_maker_find(r)
			if len(maker_list) > 1:
				print(f'请选择生产{r}的配方：')
				for i, m in enumerate(maker_list):
					print(f'{i}: ' + self.crafting_table.show(m))
				maker_select = int(input())
			else:
				maker_select = 0
			maker = maker_list[maker_select]
			self.resources_produced.append(r)
			# self.crafting_table.disable_building(maker_list)
			self.crafting_table.disable_building_list.remove(maker)
			for r_i in self.crafting_table.input_name_list(maker):
				if r_i not in self.resources_produced:
					if r_i not in resources_tbp:
						resources_tbp.append(r_i)
		print('是否有外部输入的资源？（没有请直接回车）\n例：铁 4.5 （外部输入每分钟4.5个铁）')
		r_list = input().split()
		while len(r_list) > 0:
			for i in range(len(r_list)//2):
				self.input_resources_list.append((r_list[2*i], float(r_list[2*i+1])))
			r_list = input('是否还有外部输入的资源？（没有请直接回车）').split()


	def calculate(self):
		self.resources_require_speed = {r : 0 for r in self.resources_produced}
		# resources_produce_speed = {r : 0 for r in self.resources_produced}
		resources_tbp_speed = {r : 0 for r in self.resources_produced}
		for i, name in enumerate(self.target_name):
			resources_tbp_speed[name] = self.target_speed[i]
		for r, s in self.input_resources_list:
			resources_tbp_speed[r] -= s
		self.building_num = {}

		num_unsatisfied = 1
		while num_unsatisfied > 0:
			num_unsatisfied = 0
			for r, s in resources_tbp_speed.items():
				if s > 0.001:
					num_unsatisfied += 1
					maker = self.crafting_table.maker_find(r)[0]
					if maker not in self.building_num:
						self.building_num[maker] = 0
					self.resources_require_speed[r] += s
					self.building_num[maker] = self.resources_require_speed[r] / self.crafting_table.output_speed(maker)
					resources_tbp_speed[r] = 0
					for i, r_in in enumerate(self.crafting_table.input_name_list(maker)):
						resources_tbp_speed[r_in] += self.crafting_table.input_speed_list(maker, s)[i]

	def building_tree(self, resource, speed, level=0):
		maker = self.crafting_table.maker_find(resource)[0]
		maker_num = speed / self.crafting_table.output_speed(maker)
		if level >= 10:
			return [maker, maker_num, resource, speed, []]
		r_in_list = self.crafting_table.input_name_list(maker)
		return [maker, maker_num, resource, speed,
				[self.building_tree(r_in, self.crafting_table.input_speed_list(maker, speed)[i], level+1)
				 for i, r_in in enumerate(r_in_list) 
				 if self.crafting_table.maker_find(r_in)[0] in self.building_num]]

	def using_tree(self, resource, level=1):
		user_list = self.crafting_table.user_find(resource)
		for user in user_list:
			if user not in self.building_num:
				user_list.remove(user)
		user_product_list = [self.crafting_table.output_name(b) for b in user_list]
		using_speed_list = [self.crafting_table.input_speed(b, resource, 
								self.resources_require_speed[user_product_list[i]]) for i, b in enumerate(user_list)]
		if level == 1:
			return resource, [[user, using_speed_list[i]] for i, user in enumerate(user_list)]
		else:
			return resource, [[user, using_speed_list[i], self.using_tree(user_product_list[i], level-1)]
						for i, user in enumerate(user_list)]
