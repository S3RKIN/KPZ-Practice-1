# Завдання1:
def palindrom(text):
    words = text.split()
    palindrome_words = []
    for word in words:
        if word.lower() == word.lower()[::-1] and len(word) > 1:
            palindrome_words.append(word)
    return palindrome_words

print(palindrom('lol app neen need deen rom ror ese UwU something'))
  
  
# Завдання2:
import re

def validate_ip(ip_address):
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    return True if pattern.match(ip_address) else False

print(validate_ip("192.168.0.1"))
print(validate_ip("192.168.0.256"))
  
  
  # Завдання3:
  import platform

def get_os():
    os = platform.system()
    if os == 'Darwin':
        return 'Mac'
    elif os == 'Windows':
        return 'Windows'
    elif os == 'Linux':
        return 'Linux'
    else:
        return 'Unknown OS'

print(get_os())
