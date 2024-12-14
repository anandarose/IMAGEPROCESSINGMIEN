import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

# Sidebar menu for navigation
menu = st.sidebar.selectbox(
    "Select Page",
    ["Home", "Image Processing App"]
)

# ----------------- Home Page -----------------
if menu == "Home":
    # University logo
    st.image("Logo PU.jpg", width=300)
    st.title("Welcome to Our Application")
    st.write("""
        This application is brought to you by Group 1 of M-Industrial Engineering-Class 3. 
        Explore the members of our group and try out our advanced image processing app!
    """)

    # Members section
    st.header("Group Members")
    
    member = st.radio(
        "Select a member to view their photo:",
        ["Ananda Rose Wardani", "Cilya Anggreina", "Gracia", "Nadia Salsabila Ramadhani"]
    )

    # Display the selected member's photo
    if member == "Ananda Rose Wardani":
        st.subheader("004202300025")
        st.image("Rose.jpeg", width=200)
    elif member == "Cilya Anggreina":
        st.subheader("004202300007")
        st.image("Cilya.jpeg", width=200)
    elif member == "Gracia":
        st.subheader("004202300036")
        st.image("Gracia.jpeg", width=200)
    elif member == "Nadia Salsabila Ramadhani":
        st.subheader("004202300075")
        st.image("Nadia.jpeg", width=200)

# ----------------- Image Processing App Page -----------------
elif menu == "Image Processing App":
    # App title
    st.title("Advanced Image Processing App")
    st.write("Upload an image and apply various transformations.")

    # File uploader
    uploaded_file = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        # Load the image
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_container_width=True)

        # Convert to NumPy array for OpenCV processing
        img_array = np.array(image)

        # Sidebar options
        st.sidebar.title("Processing Options")

        # Apply blur
        blur_amount = st.sidebar.slider("Blur", 0, 50, 0)
        if blur_amount > 0:
            img_array = cv2.GaussianBlur(img_array, (blur_amount * 2 + 1, blur_amount * 2 + 1), 0)

        # Rotate image
        rotate_angle = st.sidebar.slider("Rotate (degrees)", 0, 360, 0)
        if rotate_angle > 0:
            (h, w) = img_array.shape[:2]
            center = (w // 2, h // 2)
            matrix = cv2.getRotationMatrix2D(center, rotate_angle, 1.0)
            img_array = cv2.warpAffine(img_array, matrix, (w, h))

        # Adjust contrast
        contrast_factor = st.sidebar.slider("Contrast", 0.5, 3.0, 1.0)
        if contrast_factor != 1.0:
            enhancer = ImageEnhance.Contrast(Image.fromarray(img_array))
            img_array = np.array(enhancer.enhance(contrast_factor))

        # Display the processed image
        st.image(img_array, caption="Processed Image", use_container_width=True)
