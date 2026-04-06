from cryptography.fernet import Fernet
from pathlib import Path

# Generate and save a key
def generate_key(key_file="secret.key"):
    key = Fernet.generate_key()
    Path(key_file).write_bytes(key)
    return key

# Load an existing key
def load_key(key_file="secret.key"):
    return Path(key_file).read_bytes()

# Encrypt a short piece of text
def encrypt_text(text, key):
    cipher = Fernet(key)
    encrypted = cipher.encrypt(text.encode())
    return encrypted

# Encrypt a text file and save the encrypted output
def encrypt_file(input_file, output_file, key):
    cipher = Fernet(key)
    data = Path(input_file).read_bytes()
    encrypted_data = cipher.encrypt(data)
    Path(output_file).write_bytes(encrypted_data)

# Main program
if __name__ == "__main__":
    key_path = "secret.key"

    if not Path(key_path).exists():
        key = generate_key(key_path)
        print("New key generated.")
    else:
        key = load_key(key_path)
        print("Existing key loaded.")

    # Short text example
    sample_text = "This is a short confidential message."
    encrypted_text = encrypt_text(sample_text, key)
    print("Encrypted text:", encrypted_text)

    # File encryption example
    input_filename = "sample.txt"
    output_filename = "sample_encrypted.txt"

    if Path(input_filename).exists():
        encrypt_file(input_filename, output_filename, key)
        print(f"Encrypted file created: {output_filename}")
    else:
        print(f"Input file '{input_filename}' not found.")