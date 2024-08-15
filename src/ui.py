from calculate import Calculator
from math import ceil

def show_building_tree(tree, level, last=False):
	print('-|' * level + tree[0] + f' * {ceil(tree[1] * 10) / 10:.1f} ({tree[2]} {tree[3]:.1f})')
	if not last:
		if tree[0] in ['水井', '水泵', '海水过滤器', '煤矿']:
			for t in tree[4]:
				show_building_tree(t, level+1, True)
		else:
			for t in tree[4]:
				show_building_tree(t, level+1)

def show_using_tree(tree, level):
	for t in tree[1]:
		if level > 1:
			show_using_tree(t, level-1)
		print('->' * level + tree[0] + f' * {t[1]:.1f} 用于 {t[0]}')

i = 0

while i != -1:
	print('请输入要生产的目标名称与每分钟产量：')
	print('例1：人口 3000')
	print('例2：人口 3000 原住民人口 1500')
	target = input().split()
	target_name = []
	target_speed = []
	for i in range(len(target)//2):
		target_name.append(target[2*i])
		target_speed.append(int(target[2*i+1]))

	c = Calculator(target_name, target_speed, 'buildings_zh.json')

	c.crafting_table_select()

	c.calculate()

	building_num = {b:ceil(n) for b, n in c.building_num.items()}

	i = 1
	while i > 0:
		print('-' * 20)
		i = int(input('请选择要查看的内容：\n1 需要的建筑数量\n2 建筑关系\n3 某项资源的生产树\n0 重新计算\n-1 退出程序\n'))
		if i == 1:
			print('生产每分钟' + '，'.join([f'{target_speed[i]:.2f}个{n}' for i, n in enumerate(target_name)])
					+ '需要的建筑及数量如下：')
			for b in c.crafting_table.building_list():
				if b in building_num:
					print(f'{b} {building_num[b]}个')
		elif i == 2:
			print('生产每分钟' + '，'.join([f'{target_speed[i]:.2f}个{n}' for i, n in enumerate(target_name)])
					+ '需要的建筑关系如下：')
			for i, name in enumerate(target_name):
				building_tree = c.building_tree(name, target_speed[i])
				show_building_tree(building_tree, 0)
		elif i == 3:
			r = input('请输入要查看的资源：\n')
			r_speed = c.resources_require_speed[r]
			r_build_tree = c.building_tree(r, r_speed)
			r_use_tree = c.using_tree(r)
			print(f'生产每分钟{r_speed:.2f}个{r}需要的建筑关系如下：')
			show_using_tree(r_use_tree, 1)
			show_building_tree(r_build_tree, 0)
