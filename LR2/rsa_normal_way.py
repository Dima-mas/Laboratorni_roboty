"""
Згенеруйте RSA-ключ, виведіть інформацію про n, d, e
(кількість десяткових, двійкових, шістнадцяткових цифр,
їх hex-значення). Зашифруйте і розшифруйте рядок зі своїм прізвищем
(для обчислення me/d mod n використайте інформацію з пункту 4).
"""
from cryptography.hazmat.primitives.asymmetric import rsa

key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

openkey, secretkey, mode = (key.private_numbers().public_numbers.e,
                            key.private_numbers().d,
                            key.private_numbers().public_numbers.n
                            ) # e, d, n

print(f"""
Завдання 5:
e:
    decimal legth: {len(str(openkey))}
    bin legth: {len(bin(openkey))}
    hex legth: {len(hex(openkey))}
      
d:
    decimal legth: {len(str(secretkey))}
    bin legth: {len(bin(secretkey))}
    hex legth: {len(hex(secretkey))}
      
c:
    decimal legth: {len(str(mode))}
    bin legth: {len(bin(mode))}
    hex legth: {len(hex(mode))}
      """) #information about e, d and n


text = "maslov" #text to encrypt/decipher

#transforming text to bytes, then to int
encoded = text.encode("utf-8")
fromb = int.from_bytes(encoded, byteorder="big")

# encrypting int
encrypted = pow(fromb, openkey, mode)

#deciphering int
deciphered = pow(encrypted, secretkey, mode)

#transforming back to str
tob = deciphered.to_bytes((deciphered.bit_length()+7)//8,byteorder="big")
message = tob.decode("utf-8")


print(f"""
•message before encryption:{text}
•int before encryption: {fromb}
•encrypted int: {encrypted}
•deciphered int: {deciphered}
•deciphered message: {message}
      """)