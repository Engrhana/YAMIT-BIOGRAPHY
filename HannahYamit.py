import streamlit as st
from PIL import Image  # Import for image processing
import requests  # Import for image fetching (if using URL)
from io import BytesIO

# Set page title and icon
st.set_page_config(page_title="BIOGRAPHY", page_icon=":memo:")

# Add a header
st.title("BIOGRAPHY")

# Who am I? Section
st.header("Who am I?")
st.write("I am currently a first-year student taking up Computer Engineering at Surigao del Norte State University.")

# Image Section
with st.container():  # Use container for image section
    # Default image URL
    default_image_url = (
        "https://scontent.fmnl9-6.fna.fbcdn.net/v/t39.30808-6/445799438_1150472912762352_6361690226075917281_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=833d8c&_nc_eui2=AeFWRy1OQOhlIuiu2J5zd5X7fjnqrSfNq1h-OeqtJ82rWO1yUHHSNaXuL3ryYCOCk38Z8BcbXscbq2V4iB2QfIou&_nc_ohc=iLx34bj8hEYQ7kNvgH3DVtg&_nc_zt=23&_nc_ht=scontent.fmnl9-6.fna&_nc_gid=AFyKM1--Wm7VK5ZB1i24UIf&oh=00_AYBAo5ZC3ssrHw2kRdXjuRi6TIOVSMOZxMWHbBcPYHbhzQ&oe=674AFFE5"
    )

    # File uploader
    uploaded_image = st.file_uploader("Upload Profile Picture", type=["png", "jpg", "jpeg"])

    if uploaded_image is not None:
        try:
            image = Image.open(uploaded_image)
            st.image(image, caption="Profile Picture", width=400)
        except Exception as e:
            st.error(f"Error displaying the uploaded image: {e}")
    else:
        try:
            # Fetch default image from URL
            response = requests.get(default_image_url)
            response.raise_for_status()  # Raise an error for invalid responses
            default_image = Image.open(BytesIO(response.content))
            st.image(default_image, caption="Profile Picture", width=400)
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching the default image: {e}")

# Personal Information and Contact
st.header("Personal Information")

col1, col2 = st.columns(2)

with col1:
    last_name = st.text_input("Last Name:", value="Yamit", key="last_name_personal")
    first_name = st.text_input("First Name:", value="Hannah Bea", key="first_name_personal")
    middle_initial = st.text_input("Middle Initial:", value="M.", key="middle_initial_personal")
    gender = st.text_input("Gender:", value="Female", key="gender")
    age = st.number_input("Age:", min_value=0, value=18, key="age")
    address = st.text_area("Home Address:", value="Barangay Ombong, Alegria, Surigao del Norte", key="address")

with col2:
    number = st.text_input("Number:", value="+639852273262", key="number")
    email = st.text_input("Email:", value="beayamit16@gmail.com", key="email")
    facebook = st.text_input("Facebook account:", value="Hana Yamit", key="facebook")

# Parents/Guardian
st.header("Parents/Guardian")
father_name = st.text_input("Father's Name:", value="Rogelio Y. Yamit", key="father_name")
mother_name = st.text_input("Mother's Name:", value="Thelma M. Yamit", key="mother_name")

# Educational Attainment
st.header("Educational Attainment")
elementary = st.text_input("Elementary:", value="Ombong Elementary School", key="elementary")
junior_high = st.text_input("Junior High School:", value="Alegria National High School", key="junior_high")
senior_high = st.text_input("Senior High School:", value="Alegria Stand Alone Senior High School", key="senior_high")
