#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# 小白鼠喝药水

mouse_number = 10  # 小白鼠的数量
potion_number = 10  # 药水的数量
mouse = list(range(mouse_number))  # 小白鼠的编号列表
potion = list(range(potion_number))  # 药水的编号列表
mouse_data = {i: [] for i in mouse}  # 记录每只小白鼠喝的药水编号
potion_data = {i: [] for i in potion}  # 记录每支药水被喝的小白鼠编号


def test_case():
    """测试用例验证，假设每一支药水都有毒，分别验证结果"""
    # 实验，并记录实验数据：mouse_data、potion_data
    # print([bin(i) for i in potion[:10]])
    for index, p in enumerate(potion):
        p_bin = list(bin(p)[2:])  # 将编号转成二进制数，删除二进制的前缀：'0b'，再转成列表，方便颠倒
        # print(p, p_bin)
        for i, v in enumerate(reversed(p_bin)):
            if v == '1':  # 如果值为 '1'，说明这只小白鼠喝了这支药水，记录下来
                potion_data[index].append(i)
                mouse_data[i].append(p)
    # print("每支药水被喝的小白鼠编号：", [(k, v) for k, v in potion_data.items()], "\n")
    # print("每只小白鼠喝了哪些药水：", [(k, v) for k, v in mouse_data.items()], "\n")
    # print("每只小白鼠共喝了几支药水：", [(k, len(v)) for k, v in mouse_data.items()], "\n")

    # 假设每一支药水都有毒，通过有毒药水的编号、死亡小白鼠的编号列表，调用 answer() 函数验证结果
    for p in potion:
        death = potion_data[p]  # 喝了有毒药水的小白鼠死亡
        print(f"有毒药水的编号是：{p}，死亡小白鼠的编号列表：{death}")

        poison = answer(death)  # 调用回答问题函数

        # 验证你给的答案，是否正确
        if poison != p:
            print(f"回答错误，有毒的药水是第【{p}】支，你的答案是第【{poison}】支。")
            exit(1)
    # else:
    # 	print(f"回答正确，有毒的药水是第【{p}】支。")


def answer(death: list) -> int:
    """回答问题，返回问题的答案

    :param death: 死亡的小白鼠编号列表
    :return: 有毒药水的编号
    """
    if death:
        number = 0  # 定义一个初始编号，0 + 任何数，都等于任何数本身
        for d in death:
            number += 2 ** d
        return number
    else:
        return 0


if __name__ == '__main__':
    test_case()
