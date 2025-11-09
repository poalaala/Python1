import streamlit as st

st.title("Test")
name = st.text_input("請輸入名字:")

option = st.radio("選擇回覆：", ["哈哈", "笑死", "你好帥", "妳好漂亮"])
st.success(f"{option},{name}")

age = st.slider("請輸入年齡:", -20, 120, -1)
st.success(f"你多活了{age}年")
