import streamlit as st
import requests

st.markdown("# BMI計算機")
a = st.number_input("請輸入身高(m)>")
b = st.number_input("請輸入體重(kg)>")



if st.button("開始計算"):
    if a <= 0 or b <= 0:
        st.error("輸入錯誤，請再試一次")
    else:    
        c = b/(a*a)
        st.write(f'你的BMI值是{c:.2f}\n')
        if (c < 18.5):
                st.error("營養不足!!!!")
        elif (c >= 18.5 and c < 24.9):
                st.success("健康範圍")
        elif (c >= 24.9 and c < 30):
                st.warning("可能引起肥胖")
        elif (c > 30):
                st.error("肥胖!!!!")




st.title("匯率轉換")


API_KEY = "6f66bedafb0e5770d8a29a998fd89ab4"

amount = st.number_input("請輸入金額:", min_value=0.0)
from_currency = st.selectbox("從哪種貨幣轉換", ["USD", "TWD", "JPY", "EUR", "GBP"])
to_currency = st.selectbox("轉換成哪種貨幣", ["USD", "TWD", "JPY", "EUR", "GBP"])

if st.button("開始轉換"):
    
    url = f"https://api.exchangerate.host/convert?access_key={API_KEY}&from={from_currency}&to={to_currency}&amount={amount}"
    
    response = requests.get(url)
    data = response.json()
    

    
    if data.get("success", False):
        result = data["result"]
        rate = data["info"]["quote"]
        st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
        st.info(f"即時匯率：1 {from_currency} = {rate:.4f} {to_currency}")
    else:
        st.error("API 回傳錯誤，請檢查金鑰或網址。")
        if "error" in data:
            st.warning(f"錯誤代碼：{data['error'].get('code')}，類型：{data['error'].get('type')}")



    
    








