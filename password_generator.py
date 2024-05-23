import secrets
import string

def generate():
  # generate a password
  characters = " " + string.ascii_letters + string.digits + string.punctuation
  password = ""
  for _ in range(64):
    password += secrets.choice(characters)
    
  return password
  
if __name__ == "__main__":
  print(generate())