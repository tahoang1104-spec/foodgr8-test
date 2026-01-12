import streamlit as st
from PIL import Image

# ========== CONFIG ==========
st.set_page_config(
    page_title="FoodGR8",
    page_icon="🍜",
    layout="wide"
)

# ========== SIDEBAR ==========
st.sidebar.title("🍽 FoodGR8")
st.sidebar.markdown("Nhận diện món ăn Việt Nam")
st.sidebar.divider()

menu = st.sidebar.radio(
    "Chức năng",
    ["Trang chủ", "Nhận diện ảnh", "Giới thiệu"]
)

# ========== MAIN ==========
st.title("🍜 FoodGR8 – Nhận diện món ăn Việt Nam")

# ---- TRANG CHỦ ----
if menu == "Trang chủ":
    st.subheader("📌 Giới thiệu")
    st.write(
        """
        FoodGR8 là web nhận diện món ăn Việt Nam sử dụng YOLO.
        
        👉 Hiện tại: **xây dựng giao diện**  
        👉 Sắp tới: **detect ảnh / video**
        """
    )

    st.info("Chọn chức năng bên trái để bắt đầu 👈")

# ---- NHẬN DIỆN ẢNH ----
elif menu == "Nhận diện ảnh":
    st.subheader("📷 Nhận diện món ăn từ ảnh")

    uploaded_file = st.file_uploader(
        "Upload ảnh món ăn",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        image = Image.open(uploaded_file)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Ảnh gốc")
            st.image(image, use_column_width=True)

        with col2:
            st.markdown("### Kết quả")
            st.warning("⚠️ Chưa gắn model YOLO")
            st.image(image, use_column_width=True)

        st.button("🚀 Detect (sắp có)")

# ---- GIỚI THIỆU ----
elif menu == "Giới thiệu":
    st.subheader("ℹ️ Thông tin")
    st.write(
        """
        👤 Tác giả: **Bạn**  
        🧠 Model: YOLOv10  
        🌐 Nền tảng: Streamlit  

        Dự án phục vụ học tập và nghiên cứu AI.
        """
    )

