import streamlit as st

st.title("Hello Streamlit!")
st.write("이것은 가장 기본적인 Streamlit 예제입니다.")

import streamlit as st
import random

st.title("🎮 숫자 맞추기 게임")
st.write("1부터 100사이의 숫자를 맞춰보세요!")

# 세션 상태에 정답 저장하기
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 20)

guess = st.number_input("숫자를 입력하세요", min_value=1, max_value=20, step=1)

if st.button("정답 확인"):
    if guess == st.session_state.answer:
        st.success("정답입니다! 🎉")
        st.session_state.answer = random.randint(1, 20)  # 새 게임 시작
        st.info("새로운 숫자가 설정되었습니다!")
    elif guess < st.session_state.answer:
        st.warning("더 큰 숫자입니다!")
    else:
        st.warning("더 작은 숫자입니다!")
