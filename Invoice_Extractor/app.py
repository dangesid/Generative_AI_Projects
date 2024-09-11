import io
import fitz
from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Pro Vision model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get Gemini response
def get_gemini_response(input_text, images_data, prompt):
    response = model.generate_content([input_text, images_data[0], prompt])
    return response.text

# Function to handle image upload details
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded image
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")

# Function to extract all pages from the PDF and convert them to images
def extract_pdf(upload_pdf):
    pdf_doc = fitz.open(stream=upload_pdf.read(), filetype='pdf')
    images_data = []
    for pagenum in range(len(pdf_doc)):
        page = pdf_doc[pagenum]
        pix = page.get_pixmap()  # Render page to an image
        image_bytes = pix.tobytes("png")  # Convert to PNG format
        images_data.append({"mime_type": "image/png", "data": image_bytes})
    pdf_doc.close()
    return images_data

# Initialize Streamlit application
st.set_page_config(page_title="Multi-Language Invoice Extractor")
st.header("Multi-Language Invoice Extractor")

# Get user input
input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image or PDF...", type=["jpg", "png", "jpeg", "pdf"])

images_data = []

# Display uploaded image or PDF
if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        try:
            images_data = extract_pdf(uploaded_file)
            for idx, image_data in enumerate(images_data):
                image = Image.open(io.BytesIO(image_data["data"]))
                st.image(image, caption=f"Page {idx + 1} of uploaded PDF", use_column_width=True)
        except Exception as e:
            st.error(f"Error reading PDF: {e}")
    else:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        images_data = input_image_details(uploaded_file)

# Button to submit the form
submit = st.button("Tell me more about the image")

# Prompt for the invoice analysis
input_prompt = """
You are an expert in understanding invoices. We will upload an image or PDF as an invoice, and you will answer any questions
based on the uploaded document.
"""

# If submit is clicked
if submit:
    try:
        if uploaded_file is not None:
            response = get_gemini_response(input_prompt, images_data, input_text)
            st.subheader("The Response is:")
            st.write(response)
        else:
            st.error("Please upload a file to analyze.")
    except FileNotFoundError as e:
        st.error(str(e))
    except Exception as e:
        st.error(f"An error occurred: {e}")
