# 🧠 RAG 项目（Retrieval-Augmented Generation）

一个基于 **RAG（检索增强生成）** 的简单实现项目，结合信息检索（IR）与大语言模型（LLM），实现对本地数据的智能问答。

---

## 📌 项目简介

本项目实现了一个基础的 RAG 系统，主要流程如下：

1. 📄 文档加载（txt / pdf 等）
2. ✂️ 文本切分（chunking）
3. 🔍 向量化（embedding）
4. 🗂️ 向量数据库存储
5. 🤖 用户提问
6. 📚 检索相关内容
7. 🧠 LLM 生成回答

👉 核心思想：  
**让模型“查资料再回答”，而不是只靠训练数据**

---

## 🚀 功能特点

- ✅ 本地文档问答
- ✅ 多种文本处理方式
- ✅ 支持不同 LLM 模型
- ✅ 支持 embedding 检索
- ✅ 模块化设计（方便扩展）

---

## 🧱 项目结构

```bash
RAG/
├── data/                # 数据文件
├── tests/               # 测试代码
├── splitingMethodsOutputs/ # 文本切分结果
├── main.ipynb          # 主程序（Jupyter Notebook）
├── requirements.txt    # 依赖
└── README.md