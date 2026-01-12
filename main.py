import streamlit as st
from PIL import Image

# ========== CONFIG ==========
st.set_page_config(
    page_title="FoodGR8",
    page_icon="🍜",
    layout="wide"
)

# ========== CENTER CONTAINER ==========
left, center, right = st.columns([1, 3, 1])

with center:
    # ===== HEADER =====
    st.markdown("<h1 style='text-align: center;'>🍜 FoodGR8</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center;'>Nhận diện món ăn Việt Nam từ hình ảnh</p>",
        unsafe_allow_html=True
    )

    st.divider()

    # ===== UPLOAD =====
    uploaded_file = st.file_uploader(
        "📤 Upload ảnh món ăn",
        type=["jpg", "jpeg", "png"]
    )

    # ===== DISPLAY =====
    if uploaded_file:
        image = Image.open(uploaded_file)

        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.markdown("<h3 style='text-align: center;'>📷 Ảnh gốc</h3>", unsafe_allow_html=True)
            st.image(image, use_column_width=True)

        with col2:
            st.markdown("<h3 style='text-align: center;'>🧠 Kết quả</h3>", unsafe_allow_html=True)
            st.warning("Chưa gắn model YOLO")
            st.image(image, use_column_width=True)

        st.divider()

        # ===== CENTER BUTTON =====
        btn_left, btn_center, btn_right = st.columns([1, 2, 1])
        with btn_center:
            st.button("🚀 Detect", use_container_width=True)

    else:
        st.info("👆 Upload ảnh để bắt đầu")
