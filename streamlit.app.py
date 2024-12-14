import streamlit as st
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
    st.image("Logo pu.png", width=300)
    st.title("Image Processing")
    st.write("""
        This application is made by Group 1 of M-Industrial Engineering-Class 3. 
        With this Application you can :
        1. Apply Blur to your image 
        2. Rotate your image 
        3. Adjust your image contrast 
        
        Explore the members of our group and try out our advanced image processing app! 
        you can select page "image processing app" to try our application
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
        st.image("Rose.jpeg", width=150)
    elif member == "Cilya Anggreina":
        st.subheader("004202300007")
        st.image("Cilya.jpeg", width=150)
    elif member == "Gracia":
        st.subheader("004202300036")
        st.image("Gracia.jpeg", width=150)
    elif member == "Nadia Salsabila Ramadhani":
        st.subheader("004202300075")
        st.image("Nadia.jpeg", width=150)

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

        # Sidebar options
        st.sidebar.title("Processing Options")

        # Apply blur
        blur_amount = st.sidebar.slider("Blur", 0, 10, 0)
        if blur_amount > 0:
            # Using Pillow for Gaussian Blur
            image = image.filter(ImageFilter.GaussianBlur(radius=blur_amount))

        # Rotate image
        rotate_angle = st.sidebar.slider("Rotate (degrees)", 0, 360, 0)
        if rotate_angle > 0:
            image = image.rotate(rotate_angle, expand=True)

        # Adjust contrast
        contrast_factor = st.sidebar.slider("Contrast", 0.5, 3.0, 1.0)
        if contrast_factor != 1.0:
            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(contrast_factor)

        # Display the processed image
        st.image(image, caption="Processed Image", use_container_width=True)
