# 小小城建计算器 Mini Settlers Calculator

[English Version](./README_en.md)

欢迎使用小小城建计算器！这是专为游戏 [Mini Settlers](https://store.steampowered.com/app/2521630/_Mini_Settlers/) 设计的产量辅助工具。只需输入**目标产物**及**产量**，即可轻松计算出所需的**建筑数量**及**建筑关系**。借助此工具，您可以摆脱复杂的速率计算，专注于游戏中的建筑与物流规划。

![珍珠岛](./figs/珍珠岛.png)

## 功能列表

- 支持单个或多个目标产物的计算
- 选择生产配方
- 配置外部输入（适用于多个岛屿分别计算）
- 查看建筑数量
- 查看完整建筑关系树
- 查看单项资源的来源与去处

## 如何使用

1. **生成或更新建筑配方表：**

   - 在 `.\src\crafting_table_create_zh.py` 文件中更新配方。

   - 进入 `.\src\` 目录，运行 `python crafting_table_create_zh.py`，生成配方文件 `buildings_zh.json`。

2. **使用计算器：**

   - 进入 `.\src\` 目录，运行 `python ui.py`。

   - 输入目标产物及产量，例如：`1级人口 240 2级人口 1620 3级人口 6600`。

   - 选择各物资的生产配方。

   - 配置外部输入物资及速率。

   - 查看计算结果：
     - **建筑数量**：显示所需的全部建筑数量总览（数值已向上取整）。
     - **建筑关系**：显示完整的建筑关系树。
     - **某项资源生产树**：查看单项物资的来源与去处（最常用功能）。

## 参考中文名词表

| 建筑名称 | 输出名称 | 输入1 | 输入2 | 输入3 | 输入4 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 住房1级 | 1级人口 | 水 | 苹果 | 椅子 ||
| 住房2级 | 2级人口 | 果汁 | 面包 | 纸 | 沙发 |
| 住房3级 | 3级人口 | 牛奶 | 三明治 | 书 | 高档沙发 |
| 原住民小屋1级 | 1级原住民人口 | 苹果 | 石制工具 |||
| 原住民小屋2级 | 2级原住民人口 | 木板 | 铁制工具 | 皮革 ||
| 原住民小屋3级 | 3级原住民人口 | 玻璃 | 肉 | 钢制工具 ||
| 水井 | 水 | ||||
| 水泵 | 水 | 面包 ||||
| 海水过滤器 | 水 | 煤炭 ||||
| 苹果农场 | 苹果 | 水 ||||
| 果汁厂 | 果汁 | 木板 | 苹果 |||
| 小麦农场 | 小麦 | 水 ||||
| 面包坊 | 面包 | 小麦 | 煤炭 |||
| 奶牛农场 | 奶牛 | 水 | 小麦 |||
| 牛奶工厂 | 牛奶 | 奶牛 | 玻璃 |||
| 屠宰场 | 肉 | 奶牛 | 铁制工具 |||
| 餐厅 | 三明治 | 面包 | 肉 |||
| 伐木场 | 原木 | 苹果 | 树 |||
| 锯木厂 | 圆木 | 原木 ||||
| 林场 | 树 | 水 ||||
| 木匠工坊 | 木板 | 圆木 | 石制工具 |||
| 制炭厂 | 煤炭 | 苹果 | 原木 |||
| 木材工厂 | 圆木 | 面包 | 树 |||
| 木梁工坊 | 木梁 | 铁制工具 | 木板 |||
| 采石厂 | 石头 | 苹果 ||||
| 石矿 | 石头 | 面包 ||||
| 采煤厂 | 煤炭 | 苹果 ||||
| 煤矿 | 煤炭 | 面包 ||||
| 采铁厂 | 铁矿石 | 面包 ||||
| 铁矿 | 铁矿石 | 面包 ||||
| 集沙厂 | 沙子 | 果汁 ||||
| 钻石矿 | 钻石 | 肉 | 钢制工具 |||
| 石制工具厂 | 石制工具 | 石头 | 圆木 |||
| 铁制工具厂 | 铁制工具 | 铁 | 石制工具 |||
| 钢制工具厂 | 钢制工具 | 钢 | 铁制工具 |||
| 木质家具厂 | 椅子 | 原木 | 石制工具 |||
| 皮革家具厂 | 发 | 皮革 | 椅子 |||
| 高档家具厂 | 高档沙发 | 钻石 | 沙发 |||
| 石材厂 | 石材 | 石头 | 石制工具 |||
| 石材加工厂 | 石砖 | 铁制工具 | 石材 |||
| 炼铁厂 | 铁 | 煤炭 | 铁矿石 |||
| 造纸厂 | 纸 | 圆木 | 铁制工具 |||
| 皮革厂 | 皮革 | 奶牛 | 铁制工具 |||
| 玻璃厂 | 玻璃 | 沙子 | 煤炭 |||
| 炼钢厂 | 钢 | 煤炭 | 铁 |||
| 图书馆 | 书 | 皮革 | 纸 | 钢制工具 ||