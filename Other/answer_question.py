#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# 小白鼠喝药水

import time

# 10 只小白鼠的编号列表
mouse = list(range(10))
# print(mouse)
# 1000 支药水的编号列表
potion = list(range(1000))
# 有毒药水的编号
poison = 10


def test() -> list:
	"""计时开始，开始实验，返回实验结果

	:return: 死亡的小白鼠编号列表
	"""
	print("两小时，计时开始，开始实验。\n实验中……\n")
	time.sleep(1)  # 模拟实验时间
	test_data = {}  # 记录每支药水被喝的小白鼠编号
	print([bin(i) for i in potion[:10]])
	for index, p in enumerate(potion):
		test_data[index] = []  # 记录喝了这支药水的小白鼠编号
		p_bin = list(bin(p)[2:])  # 将编号转成二进制数，删除二进制的前缀：'0b'，再转成列表，方便颠倒
		# print(p, p_bin)
		for i, v in enumerate(reversed(p_bin)):
			if v == '1':  # 如果值为 '1'，说明这只小白鼠喝了这支药水，记录下来
				test_data[index].append(i)
	print([(k, v) for k, v in test_data.items()][:10])  # 前 10 支药水被喝的小白鼠编号

	death = test_data[poison]
	if death:
		print(f"两小时，时间已到，死亡小白鼠的编号有：{'、'.join([str(i) for i in death])}，共 {len(death)} 只小白鼠死亡。")
	else:
		print(f"两小时，时间已到，没有小白鼠死亡。")
	print("请问第几支药水有毒，请说出有毒药水的编号?\n")
	return death


def answer(death: list) -> int:
	"""回答问题，返回问题的答案

	:param death: 死亡的小白鼠编号列表
	:return: 有毒药水的编号
	"""
	print(f"计算中……\n")
	time.sleep(1)  # 模拟回答问题时间
	if death:
		data = {i: [] for i in mouse}  # 记录每只小白鼠喝的药水编号
		for p in potion:
			p_bin = list(bin(p)[2:])  # 将编号转成二进制数，删除二进制的前缀：'0b'，再转成列表，方便颠倒
			# print(p, p_bin)
			for i, v in enumerate(reversed(p_bin)):
				if v == '1':  # 如果值为 '1'，说明这只小白鼠喝了这支药水，记录下来
					data[i].append(p)
		# print([(k, v) for k, v in data.items()][0])  # 第一只小白鼠喝了哪些药水
		print([(k, len(v)) for k, v in data.items()])  # 每一只小白鼠喝了几只药水

		no_death = set(mouse) - set(death)  # 没有死亡的小白鼠编号列表
		# print(death, no_death)
		number = set(potion)  # 需要确认是否有毒的药水集合，所有药水都有嫌疑
		# 没有死亡的小白鼠喝过的药水，是没有毒的，可以排除
		for no_d in no_death:
			number = number - set(data[no_d])  # 求差集
		print(f"初步计算结果，有的药水的编号有：{number}")  # 还需确认是否有毒的药水
		# 在死亡的小白鼠喝过的药水中，找都喝过的药水，就是有毒的
		for d in death:
			number = number & set(data[d])  # 求交集
		# 有毒的药水有且仅有一个
		if len(number) == 1:
			return number.pop()
		else:
			print(f"解答失败，你最终排除结果，有毒药水的编号有：{number}")
			return number
	else:
		return 0


def check(result) -> bool:
	"""验证你给的答案，是否正确"""
	print(f"你的答案是：【{result}】")
	if result == poison:
		print(f"回答正确，有毒的药水是第【{poison}】支。")
		return True
	else:
		print(f"回答错误！")
		return False


if __name__ == '__main__':
	death_list = test()
	your_answer = answer(death_list)
	check(your_answer)
