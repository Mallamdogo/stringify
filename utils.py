import re

def slugify(s):
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '',s)
    s = re.sub(r'[\s_-]+', '-',s)
    s = re.sub(r'^-+|-+$', '',s)
    return s

a = input("Enter a string: ")
print(slugify(a))


def digify(n:int):
    return f"{n:,}"

print(digify(12345678))

def is_valid_email(email:str):
    pattern = r'^[\w\.-]+@[\w\.-]+\.w+$'
    if re.match(pattern,email):
        return True
    else:
        return False

e = input("Enter your email: ")
print(is_valid_email(e))