#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# 木板拼接木桶

def test_case():
	"""测试用例验证"""
	number = 10
	for n in range(number):
		answer(n)  # 木板个数


def answer(n: int) -> int:
	"""回答问题，返回问题的答案

	:param n: 木板个数，即几个边的木桶
	:return: 木板拼接角度
	"""
	if n < 2:
		print(f"木板个数太少【{n}】。")
	elif n == 2:
		angle = 90 // n
		print(f"两块木板拼接直角边，木板拼接角度为：{angle}")
	else:
		interior_angle_sum = (n - 2) * 180
		angle = interior_angle_sum // (2 * n)
		print(f"{n}块木板拼接{n}边形木桶，木板拼接角度为：{angle}")


if __name__ == '__main__':
	test_case()
