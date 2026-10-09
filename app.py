
import streamlit as st
import random

st.set_page_config(page_title="Game Đoán Số", page_icon="🎮")

st.title("🎮 GAME ĐOÁN SỐ BÍ MẬT")
st.write("Chào mừng bạn đến với trò chơi Tin học lớp 8!")

if "bi_mat" not in st.session_state:
    st.session_state.bi_mat = random.randint(1, 20)
    st.session_state.luot = 0
    st.session_state.ket_qua = ""

st.write("Máy tính đã chọn một số từ 1 đến 20.")
so_doan = st.number_input(
    "Bạn đoán số nào?",
    min_value=1,
    max_value=20,
    step=1
)

if st.button("Kiểm tra đáp án"):
    st.session_state.luot += 1

    if so_doan < st.session_state.bi_mat:
        st.session_state.ket_qua = "⬆️ Số bí mật lớn hơn!"
    elif so_doan > st.session_state.bi_mat:
        st.session_state.ket_qua = "⬇️ Số bí mật nhỏ hơn!"
    else:
        st.session_state.ket_qua = "🎉 Chính xác! Bạn đã chiến thắng!"

st.info(st.session_state.ket_qua or "Hãy thử đoán một số nhé!")
st.write("Số lượt đoán:", st.session_state.luot)

if st.button("🔄 Chơi lại"):
    st.session_state.bi_mat = random.randint(1, 20)
    st.session_state.luot = 0
    st.session_state.ket_qua = ""
    st.rerun()
