import secrets
import string

def main():
  # generate a password
  characters = " " + string.ascii_letters + string.digits + string.punctuation
  password = ""
  for _ in range(64):
    password += secrets.choice(characters)
  print(password)
  
if __name__ == "__main__":
  main()