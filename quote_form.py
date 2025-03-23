import streamlit as st
import requests
import pandas as pd

list = pd.read_csv("list.csv")

def get_address(zip_code):
  res = requests.get("https://zipcloud.ibsnet.co.jp/api/search",
                   params={"zipcode":str(zip_code)})
  data = res.json()["results"][0]
  address = data["address1"] + data["address2"] + data["address3"]
  return address
  
def main():
  st.title("見積もりフォーム")
  st.subheader("お客様情報")
  st.text("お客様情報を入力して、おすすめ機種の見積もりをする")
  zip_code = st.text_input("郵便番号(半角数字・ハイフン無)", placeholder = "1234567")
  address = st.text_input("住所", value = get_address(zip_code) if zip_code and len(zip_code) == 7 and zip_code.isdigit() else "", placeholder = "東京都港区海岸1-5-20サンプルマンション202号室")
  name = st.text_input("お名前", placeholder = "東京太郎")
  phone_number = st.text_input("電話番号(半角数字・ハイフン無)", placeholder = "0123456789")
  emali = st.text_input("メールアドレス", placeholder = "sample@tokyo-gas.co.jp")
  size = int(st.selectbox("畳数", ("6", "8", "10")))

  if st.button("見積もりをする"):
    if not address or not name or not phone_number or not emali:
      st.error("すべての項目を入力してください。")
    else:
      st.subheader("おすすめの製品")
      st.image("model.png")
      st.text("型番：" + list[list["畳数"] == size]["型番"].iloc[0])
      st.text("機器販売価格：" + list[list["畳数"] == size]["機器販売価格"].iloc[0] + "円")
      st.text("基本工事費：" + list[list["畳数"] == size]["基本工事費"].iloc[0] + "円")
      st.button("本見積もりはこちらから")

if __name__ == '__main__':
  main()