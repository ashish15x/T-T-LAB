import random
import string
def generate_password():
    upper_chars = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    lower_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
    digits = ''.join(random.choice(string.digits) for _ in range(3))
    punctuation = ''.join(random.choice(string.punctuation) for _ in range(3))
    password = upper_chars + lower_chars + digits + punctuation
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password
    
print("New Password: ", generate_password())