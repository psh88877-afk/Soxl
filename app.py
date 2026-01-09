import streamlit as st
from datetime import date

st.set_page_config(page_title="SOXL 전략 대시보드", layout="centered")

st.title("📊 SOXL V2 매매 대시보드")

st.markdown("### 현재 전략 상태")

col1, col2 = st.columns(2)

with col1:
    st.metric("현재가", "$45.20")
    st.metric("VWAP", "$44.85")
    st.metric("평단", "$44.70")

with col2:
    st.metric("보유 수량", "220주")
    st.metric("분할 단계", "2 / 3.5")
    st.metric("손절 D-Day", "D+4")

st.divider()

st.markdown("### 📌 전략 규칙 요약")
st.write("""
- 전일 대비 **-5% 이상 하락 시 VWAP 매수**
- 3.5분할: **35% / 30% / 25% + 예비 10%**
- 매도: **익일부터 평단 +0.3% VWAP 전량**
- 손절: **마지막 매수 후 9거래일**
""")

st.divider()

st.markdown("### 🧾 오늘 상태")
st.success("✅ 매도 대기 상태")

st.caption(f"마지막 업데이트: {date.today()}")
