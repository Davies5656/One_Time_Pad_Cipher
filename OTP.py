import streamlit as st  # Importing Streamlit for creating the web app
import random  # Importing random module to generate random keys
import string  # Importing string module for working with alphabets

# Function to generate a random key (A-Z only)
def generate_key(length):ggg
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))  # Generates a key with random uppercase letters

# Function to convert text to numbers (A=0, B=1, ..., Z=25)
def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]  # Converts each letter to its corresponding number

# Function to convert numbers back to text
def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)  # Converts numbers back to letters

# Encrypt function
def encrypt(plaintext, key):
    plaintext = plaintext.upper().strip()  # Convert plaintext to uppercase and remove extra spaces
    key = key.upper().strip()  # Convert key to uppercase and remove extra spaces

    if not plaintext.isalpha():  # Ensure plaintext contains only letters
        return "⚠️ Error: Plaintext must contain only letters!", ""

    if not key:  # If no key is provided, generate a random key of the same length as plaintext
        key = generate_key(len(plaintext))

    if len(key) != len(plaintext):  # Ensure key and plaintext are the same length
        return "⚠️ Error: Key must be the same length as plaintext!", ""

    plaintext_nums = text_to_numbers(plaintext)  # Convert plaintext to numerical values
    key_nums = text_to_numbers(key)  # Convert key to numerical values
    ciphertext_nums = [(p + k) % 26 for p, k in zip(plaintext_nums, key_nums)]  # Apply encryption formula
    ciphertext = numbers_to_text(ciphertext_nums)  # Convert numerical values back to text

    return ciphertext, key  # Return the encrypted text and the key

# Decrypt function
def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().strip()  # Convert ciphertext to uppercase and remove extra spaces
    key = key.upper().strip()  # Convert key to uppercase and remove extra spaces

    if len(ciphertext) != len(key) or not ciphertext.isalpha() or not key.isalpha():
        return "⚠️ Error: Invalid input. Ensure both ciphertext and key are the same length and contain only letters!"

    ciphertext_nums = text_to_numbers(ciphertext)  # Convert ciphertext to numerical values
    key_nums = text_to_numbers(key)  # Convert key to numerical values
    plaintext_nums = [(c - k) % 26 for c, k in zip(ciphertext_nums, key_nums)]  # Apply decryption formula
    plaintext = numbers_to_text(plaintext_nums)  # Convert numerical values back to text

    return plaintext  # Return the decrypted text

# Streamlit UI Setup
st.set_page_config(page_title="🔐 One-Time Pad Cipher", layout="centered")  # Set Streamlit app title and layout
st.title("🔐 One-Time Pad Cipher")  # Display the title in the Streamlit app

# Input for encryption
st.subheader("Encryption")  # Section header
plaintext = st.text_input("Enter Plaintext (A-Z only):")  # Input field for plaintext
key = st.text_input("Enter Key (or leave blank to generate one):")  # Input field for key

if st.button("🔐 Encrypt"):  # Button to trigger encryption
    ciphertext, generated_key = encrypt(plaintext, key)  # Call encryption function
    if "Error" not in ciphertext:
        st.success(f"**Ciphertext:** `{ciphertext}`")  # Display encrypted text
        st.info(f"**Key Used:** `{generated_key}`")  # Display key used
    else:
        st.error(ciphertext)  # Display error message if any

# Input for decryption
st.subheader("Decryption")  # Section header
ciphertext_input = st.text_input("Enter Ciphertext (A-Z only):")  # Input field for ciphertext
key_input = st.text_input("Enter Key for Decryption:")  # Input field for key

if st.button("🔓 Decrypt"):  # Button to trigger decryption
    decrypted_text = decrypt(ciphertext_input, key_input)  # Call decryption function
    if "Error" not in decrypted_text:
        st.success(f"**Decrypted Text:** `{decrypted_text}`")  # Display decrypted text
    else:
        st.error(decrypted_text)  # Display error message if any
