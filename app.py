import streamlit as st

st.title("Hello Streamlit!")
st.write("이것은 가장 기본적인 Streamlit 예제입니다.")

import streamlit as st
import random

st.title("🐎 랜덤 경마 배팅 게임 (8마리, 코인 1000)")

# 초기 코인
if "coins" not in st.session_state:
    st.session_state.coins = 1000

# 경주 마리 수
horses = ["🐴1번", "🐴2번", "🐴3번", "🐴4번", "🐴5번", "🐴6번", "🐴7번", "🐴8번"]

# 배팅 선택
st.write(f"💰 현재 코인: {st.session_state.coins}")
bet_amount = st.number_input("배팅 금액", min_value=1, max_value=st.session_state.coins, value=10)
bet_horse = st.selectbox("어떤 말에 배팅하시겠습니까?", horses)

# 경주 진행 함수
def race():
    if bet_amount > st.session_state.coins:
        st.warning("코인이 부족합니다!")
        return

    winner = random.choice(horses)
    st.write(f"🏁 경주 결과: {winner} 승리!")

    if bet_horse == winner:
        st.session_state.coins += bet_amount
        st.success(f"🎉 승리! 코인 +{bet_amount} → {st.session_state.coins}")
    else:
        st.session_state.coins -= bet_amount
        st.error(f"💀 패배! 코인 -{bet_amount} → {st.session_state.coins}")

# 버튼
if st.button("🎬 경주 시작"):
    race()
    st.experimental_rerun()

# 리셋 버튼
if st.button("🔄 리셋"):
    st.session_state.coins = 1000
    st.experimental_rerun()

