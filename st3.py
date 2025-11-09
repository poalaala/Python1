import streamlit as st
import requests

st.title("匯率轉換")

amount = st.number_input("請輸入金額:", min_value=0.0)
from_currency = st.selectbox("從哪種貨幣轉換", ["USD", "TWD", "JPY", "EUR", "GBP"])
to_currency = st.selectbox("轉換成哪種貨幣", ["USD", "TWD", "JPY", "EUR", "GBP"])

if st.button("開始轉換"):
    url = f"https://v6.exchangerate-api.com/v6/6f66bedafb0e5770d8a29a998fd89ab4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    # 🔍 顯示 API 回傳內容
    st.write(data)

    # ✅ 防止沒有 conversion_rates 時報錯
    if "conversion_rates" in data:
        rate = data["conversion_rates"][to_currency]
        result = amount * rate
        st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    else:
        st.error("API 回傳內容有誤，請檢查金鑰或 API 網址。")
        if "error-type" in data:
            st.warning(f"錯誤類型：{data['error-type']}")
