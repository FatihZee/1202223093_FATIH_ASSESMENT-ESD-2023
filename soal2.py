def check_palindrome(text):
    clean_text = ''.join(char.lower() for char in text if char.isalnum())

    return clean_text == clean_text[::-1]

user_input = input("Masukkan kata atau kalimat: ")

result = check_palindrome(user_input)

if result:
    print("eureeka!")
else:
    print("suka blyat")