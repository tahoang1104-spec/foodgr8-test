import streamlit as st
from PIL import Image

# ========== CONFIG ==========
st.set_page_config(
    page_title="FoodGR8",
    page_icon="🍜",
    layout="wide"
)

# ========== HEADER ==========
st.title("🍜 FoodGR8 – Nhận diện món ăn Việt Nam")
st.markdown(
    "Upload ảnh món ăn và nhấn **Detect** để nhận diện (model sẽ gắn sau)."
)

st.divider()

# ========== UPLOAD ==========
uploaded_file = st.file_uploader(
    "📤 Upload ảnh món ăn",
    type=["jpg", "jpeg", "png"]
)

# ========== DISPLAY ==========
if uploaded_file:
    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📷 Ảnh gốc")
        st.image(image, use_column_width=True)

    with col2:
        st.subheader("🧠 Kết quả")
        st.warning("⚠️ Chưa gắn model YOLO")
        st.image(image, use_column_width=True)

    st.divider()
    st.button("🚀 Detect")

else:
    st.info("👆 Vui lòng upload ảnh để bắt đầu")
