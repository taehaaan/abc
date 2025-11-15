import streamlit as st

st.title("Hello Streamlit!")
st.write("이것은 가장 기본적인 Streamlit 예제입니다.")

import streamlit as st
import random

st.title("🗡️ 검 강화 게임 (이미지)")

# 검 이미지 URL 리스트 (강화 단계별)
sword_images = [
    "https://i.imgur.com/7y9U2XQ.png",  # 1단계
    "https://i.imgur.com/W1lqB9M.png",  # 2단계
    "https://i.imgur.com/hz2kXkI.png",  # 3단계
    "https://i.imgur.com/Ux8xH6N.png",  # 4단계
    "https://i.imgur.com/3pSke9f.png",  # 5단계
]

# 세션 상태 초기화
if "sword_level" not in st.session_state:
    st.session_state.sword_level = 0  # 강화 레벨
if "sword_attack" not in st.session_state:
    st.session_state.sword_attack = 5

# 검 강화 함수
def enhance_sword():
    if st.session_state.sword_level >= len(sword_images)-1:
        st.warning("⚔️ 검이 최대 강화입니다!")
        return
    success_rate = random.randint(1, 100)
    if success_rate <= 70:  # 70% 성공
        st.session_state.sword_level += 1
        increase = random.randint(2,5)
        st.session_state.sword_attack += increase
        st.success(f"🗡️ 검 강화 성공! 공격력 +{increase} → {st.session_state.sword_attack}")
    else:
        st.error("💥 강화 실패! 공격력 변화 없음.")

# 현재 검 이미지 표시
st.image(sword_images[st.session_state.sword_level], width=300)

st.write(f"⚔️ 현재 공격력: {st.session_state.sword_attack}")
st.write(f"🆙 강화 레벨: {st.session_state.sword_level + 1} / {len(sword_images)}")

# 강화 버튼
if st.button("⚒️ 검 강화"):
    enhance_sword()
    st.experimental_rerun()

# 리셋 버튼
if st.button("🔄 리셋"):
    st.session_state.sword_level = 0
    st.session_state.sword_attack = 5
    st.experimental_rerun()
