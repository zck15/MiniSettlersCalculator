from calculate import Calculator
from math import ceil

target = input('请输入要生产的目标名称与每分钟产量（以空格隔开）：\n').split()
target_name = target[0]
target_speed = int(target[1])

c = Calculator(target_name, target_speed, 'buildings_zh.json')

c.crafting_table_select()

c.calculate()

building_num = {b:ceil(n) for b, n in c.building_num.items()}
building_tree = c.building_tree()

i = 0
while i != -1:
	print('-' * 20)
	i = int(input('请选择要查看的内容：\n0 需要的建筑数量\n1 建筑关系\n-1 退出程序\n'))
	if i == 0:
		print(f'生产每分钟{target_speed}个{target_name}需要的建筑及数量如下：')
		for b in c.crafting_table.building_list():
			if b in building_num:
				print(f'{b} {building_num[b]}个')
	elif i == 1:
		def iterate_show(tree, level):
			print('-|' * level + tree[0] + f' * {ceil(tree[1] * 10) / 10:.1f}')
			for t in tree[2]:
				iterate_show(t, level+1)
		print(f'生产每分钟{target_speed}个{target_name}需要的建筑关系如下：')
		iterate_show(building_tree, 0)