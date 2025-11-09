import streamlit as st


st.title("Test")

st.info("ㄟ~~是不是要輸了阿")

st.markdown("## 網頁")
st.write("網頁")
st.markdown("<p style = 'color:blue;'>網頁</p>",unsafe_allow_html=True)
st.markdown("### 網頁")
st.subheader("網頁")
st.markdown("**好粗阿**")
st.markdown("[點啊，還不點!!](https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1)")
st.markdown("[![bababooey](https://thumb.ac-illust.com/62/62432ebf5df0bf20e8885b7dcca4b4cc_w.jpeg)](https://www.youtube.com/watch?v=AOxUDz5_2iY)")





name = st.text_input("請輸入名字:")
if st.button("1"):
    st.success(f"哈哈,{name}")

if st.button("2"):
    st.success(f"笑死,{name}")

if st.button("3"):
    st.success(f"你好帥,{name}")

if st.button("4"):
    st.success(f"妳好漂亮,{name}")

age = st.slider("請輸入年齡:",-20,120,-1)
st.success(f"你多活了{age}年")

st.warning("哈哈")
