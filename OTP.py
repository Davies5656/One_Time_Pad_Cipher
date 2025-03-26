import streamlit as st
import random
import string

# Function to generate a random key (A-Z only)
def generate_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

# Function to convert text to numbers (A=0, B=1, ..., Z=25)
def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]

# Function to convert numbers back to text
def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)

# Encrypt function
def encrypt(plaintext, key):
    plaintext = plaintext.upper().strip()
    key = key.upper().strip()

    if not plaintext.isalpha():
        return "⚠️ Error: Plaintext must contain only letters!", ""

    if not key:
        key = generate_key(len(plaintext))

    if len(key) != len(plaintext):
        return "⚠️ Error: Key must be the same length as plaintext!", ""

    plaintext_nums = text_to_numbers(plaintext)
    key_nums = text_to_numbers(key)
    ciphertext_nums = [(p + k) % 26 for p, k in zip(plaintext_nums, key_nums)]
    ciphertext = numbers_to_text(ciphertext_nums)

    return ciphertext, key

# Decrypt function
def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().strip()
    key = key.upper().strip()

    if len(ciphertext) != len(key) or not ciphertext.isalpha() or not key.isalpha():
        return "⚠️ Error: Invalid input. Ensure both ciphertext and key are the same length and contain only letters!"

    ciphertext_nums = text_to_numbers(ciphertext)
    key_nums = text_to_numbers(key)
    plaintext_nums = [(c - k) % 26 for c, k in zip(ciphertext_nums, key_nums)]
    plaintext = numbers_to_text(plaintext_nums)

    return plaintext

# Streamlit UI
st.set_page_config(page_title="🔐 One-Time Pad Cipher", layout="centered")
st.title("🔐 One-Time Pad Cipher")

# Input for encryption
st.subheader("Encryption")
plaintext = st.text_input("Enter Plaintext (A-Z only):")
key = st.text_input("Enter Key (or leave blank to generate one):")

if st.button("🔐 Encrypt"):
    ciphertext, generated_key = encrypt(plaintext, key)
    if "Error" not in ciphertext:
        st.success(f"**Ciphertext:** `{ciphertext}`")
        st.info(f"**Key Used:** `{generated_key}`")
    else:
        st.error(ciphertext)

# Input for decryption
st.subheader("Decryption")
ciphertext_input = st.text_input("Enter Ciphertext (A-Z only):")
key_input = st.text_input("Enter Key for Decryption:")

if st.button("🔓 Decrypt"):
    decrypted_text = decrypt(ciphertext_input, key_input)
    if "Error" not in decrypted_text:
        st.success(f"**Decrypted Text:** `{decrypted_text}`")
    else:
        st.error(decrypted_text)