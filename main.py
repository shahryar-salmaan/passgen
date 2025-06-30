import secrets
import string

# Checking string module
letters: str = string.ascii_letters
digits: str = string.digits
symbols: str = string.punctuation

all_chars: str = letters + digits + symbols
 

# Function for Generating password
def gen_pass() -> None:
    
    password: str = ""

    for i in range(8):
        
        random_char = secrets.choice(all_chars)
        password += random_char

    print(password)

if __name__ == "__main__":
    gen_pass()
