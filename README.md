
# <div align="center">🐍 PDA 编程语言</div>

<div align="center">
  
**Pinyin Programming Language —— 用母语思维写代码**

[![license](https://img.shields.io/badge/license-Apache--2.0-blue)](https://gitee.com/magicianswand/pda/blob/master/LICENSE)
[![python](https://img.shields.io/badge/python-3.6%2B-blue)](https://python.org)
[![stars](https://gitee.com/magicianswand/pda/badge/star.svg?theme=dark)](https://gitee.com/magicianswand/pda)
[![forks](https://gitee.com/magicianswand/pda/badge/fork.svg?theme=dark)](https://gitee.com/magicianswand/pda)
<a href='https://gitee.com/magicianswand/pda'><img src='https://gitee.com/magicianswand/pda/widgets/widget_1.svg' alt='Fork me on Gitee'></img></a>

</div>

---

## 📋 目录

- [项目概述](#-项目概述)
- [快速开始](#-快速开始)
- [安装指南](#-安装指南)
- [语法参考](#-语法参考)
- [示例代码](#-示例代码)
- [贡献指南](#-贡献指南)
- [常见问题](#-常见问题)
- [许可证](#-许可证)

---

## 📖 项目概述

### 这是什么？

**PDA**（**P**in**D**a **A**lternative）是一门基于汉语拼音的编程语言。它将编程关键字映射为拼音，让开发者无需记忆英文单词即可编写程序。

### 设计动机

| 问题 | PDA 解决方案 |
|------|--------------|
| 英文关键字记忆困难 | 拼音关键字：`ru`、`xunhuan`、`dang` |
| 中英文输入频繁切换 | 拼音输入，无需切换输入法 |
| 英文错误信息难以理解 | 中文错误提示（开发中） |
| 编程入门门槛过高 | 专注逻辑，跳过语言障碍 |

### 目标用户

- **编程初学者**：降低入门门槛
- **K-12 教育**：适合编程启蒙教学
- **技术爱好者**：探索中文编程范式

---

## 🚀 快速开始

### 第一个程序

创建 `hello.pda`：

```python
pda("你好，PDA！")
名字 = shuru("你叫什么名字？")
pda("欢迎你，" + 名字)
```

### 运行方式

```bash
# 命令行运行
python pda_runner.py hello.pda

# 或直接双击 .pda 文件（需关联）
```

---

## 📦 安装指南

### Windows 一键安装

1. 下载 PDA_Setup.exe
2. 以管理员身份运行
3. 选择安装路径，勾选"关联 .pda 文件"
4. 完成安装

### 手动安装（Python 3.6+）

```bash
git clone https://gitee.com/magicianswand/pda.git
cd pda
python pda_runner.py
```

### 验证安装

创建 `test.pda`：

```python
pda("安装成功")
shuru("按回车退出...")
```

双击运行，看到输出即安装成功。

---

## 📚 语法参考

### 基础语法

| 功能 | 语法 | 示例 |
|------|------|------|
| 输出 | `pda(表达式)` | `pda("Hello")` |
| 输入 | `变量 = shuru(提示)` | `名字 = shuru("姓名：")` |
| 变量赋值 | `变量 = 值` | `计数 = 0` |
| 类型转换 | `zhengshu()` / `xiaoshu()` | `数字 = zhengshu("123")` |

### 条件控制

```python
ru 条件1
    # 代码块
否则 ru 条件2
    # 代码块
否则
    # 代码块
ru
```

### 循环结构

**遍历循环：**

```python
xunhuan 变量 = 可迭代对象
    # 循环体
ru
```

**条件循环：**

```python
dang 条件
    # 循环体
ru
```

**循环控制：**

- `tingzhi` - 跳出循环
- `jixu` - 跳过本次迭代

### 内置函数

| 函数 | 说明 | 示例 |
|------|------|------|
| `changdu(对象)` | 返回长度 | `changdu([1,2,3])` → 3 |
| `suiji(a, b)` | 随机整数 | `suiji(1,100)` |
| `zhengshu(值)` | 转整数 | `zhengshu("10")` → 10 |
| `xiaoshu(值)` | 转浮点数 | `xiaoshu("3.14")` → 3.14 |

### 关键字一览

| 关键字 | 对应英文 | 状态 |
|--------|----------|------|
| `pda` | print | ✅ |
| `ru` | if/endif | ✅ |
| `否则` | else | ✅ |
| `xunhuan` | for | ✅ |
| `dang` | while | ✅ |
| `tingzhi` | break | ✅ |
| `jixu` | continue | ✅ |
| `shuru` | input | ✅ |
| `changdu` | len | ✅ |
| `suiji` | random | ✅ |
| `zhengshu` | int | ✅ |
| `xiaoshu` | float | ✅ |
| `且` / `或` / `非` | and/or/not | 🚧 |

---

## 💡 示例代码

### 猜数字游戏

```python
目标 = suiji(1, 100)
次数 = 0

pda("猜数字游戏 (1-100)")

dang True
    猜测 = zhengshu(shuru("输入数字："))
    次数 = 次数 + 1
    
    ru 猜测 == 目标
        pda("恭喜猜对了！共" + 次数 + "次")
        tingzhi
    否则 ru 猜测 > 目标
        pda("太大了")
    否则
        pda("太小了")
    ru
ru
```

### 九九乘法表

```python
xunhuan i = [1,2,3,4,5,6,7,8,9]
    行 = ""
    xunhuan j = [1,2,3,4,5,6,7,8,9]
        ru j <= i
            行 = 行 + j + "×" + i + "=" + (i*j) + "\t"
        ru
    ru
    pda(行)
ru
```

### 计算器

```python
pda("简易计算器")
a = zhengshu(shuru("第一个数："))
op = shuru("运算符(+ - * /)：")
b = zhengshu(shuru("第二个数："))

ru op == "+": 结果 = a + b
否则 ru op == "-": 结果 = a - b
否则 ru op == "*": 结果 = a * b
否则 ru op == "/":
    ru b == 0
        pda("错误：除数不能为零")
        tingzhi
    ru
    结果 = a / b
否则
    pda("错误：不支持的运算符")
    tingzhi
ru

pda(a + op + b + "=" + 结果)
```

---

## 🤝 贡献指南

### 贡献者等级

| 等级 | 要求 | 权益 |
|------|------|------|
| 🥉 青铜 | 1 次有效 PR | 贡献者名单 |
| 🥈 白银 | 3 次有效 PR | 电子证书 |
| 🥇 黄金 | 10 次 PR / 模块维护者 | 专属徽章 |

### 待办任务

- [ ] 修复中文路径处理 Bug
- [ ] 实现 `且` / `或` / `非` 逻辑运算符
- [ ] 编写单元测试
- [ ] 提供英文版 README
- [ ] 开发 VS Code 语法高亮插件

### 当前贡献者

| 贡献者 | 等级 | 贡献 |
|--------|------|------|
| @magicianswand | 🥇 黄金 | 创始人、核心开发 |
| @MLC | 🥈 白银 | 部分代码 |

![输入图片说明](MLC%E7%9A%84%E8%B4%A1%E7%8C%AE%E8%AF%81%E4%B9%A6.png)

---

## ❓ 常见问题

<details>
<summary><b>如何关联 .pda 文件？</b></summary>

以管理员身份运行安装程序，勾选"关联 .pda 文件"。若已安装，可运行 `associate.reg` 手动关联。
</details>

<details>
<summary><b>提示"找不到 python"怎么办？</b></summary>

安装 Python 3.6+，安装时勾选 **"Add Python to PATH"**。
</details>

<details>
<summary><b>支持中文变量名吗？</b></summary>

完全支持。例如：`学生姓名 = "张三"`。
</details>

<details>
<summary><b>PDA 和 Python 的关系？</b></summary>

PDA 解释器由 Python 编写，PDA 代码会被转换为 Python 执行。使用 PDA 无需了解 Python。
</details>

<details>
<summary><b>如何卸载？</b></summary>

删除 `C:\Program Files\PDA` 目录及桌面快捷方式即可。
</details>

---

## 📄 许可证

Copyright © 2026 Magician's Wand

本项目基于 **Apache License 2.0** 开源，详见 [LICENSE](LICENSE) 文件。

---

<div align="center">

## ⭐ 支持 PDA

如果这个项目对你有帮助，或者你觉得“用拼音写代码”这个想法有点意思：

- **点一个 Star** → 让更多人发现这门语言
- **提一个 PR** → 哪怕是修 typo，也会获得贡献者证书
- **分享给朋友** → 尤其是正在学编程的孩子或初学者
- **商务合作 / 企业定制** → 企业版组织正式授权，可签合同、开发票

> 你的支持，是 PDA 继续生长的动力 ❤️

</div>
```

---

 