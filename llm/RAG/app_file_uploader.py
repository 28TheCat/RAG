# 基于Streamlit完成WEB网页上传服务
import sys
import os
import time

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if root_path not in sys.path:
    sys.path.append(root_path)

import streamlit as st
from llm.RAG.knowledge_base import KnowledgeBaseService

st.title("📚 知识库更新服务")

uploaded_file = st.file_uploader(
    "请上传 TXT 文件",
    type=['txt'],
    accept_multiple_files=False
)

if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()

if uploaded_file is not None:
    file_name = uploaded_file.name
    file_type = uploaded_file.type
    file_size = uploaded_file.size / 1024
    # 读取文件内容
    try:
        content = uploaded_file.read().decode("utf-8")
    except UnicodeDecodeError:
        content = uploaded_file.read().decode("gbk", errors="ignore")

    # 获取结果
    result = st.session_state["service"].upload_by_str(content, file_name)
    if "【跳过】" in result:
        st.warning(result)  # 使用黄色警告框显示“已存在”
    else:
        st.success(result)  # 使用绿色成功框显示“已入库”
    st.subheader("📄 文件信息")
    st.write(f"文件名：{file_name}")
    st.write(f"格式：{file_type}")
    st.write(f"大小：{file_size:.2f} KB")


    st.subheader("📖 文件内容预览")
    time.sleep(1)
    st.text(content[:1000])  # 只展示前1000字符
    result=st.session_state["service"].upload_by_str(content,file_name)
    st.write(result)

