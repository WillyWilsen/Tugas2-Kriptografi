import math
from sympy import mod_inverse

def affine_plain(hex_values, m, b, n):
  cipher_hex = []
  for i in range(len(hex_values)):
    C = hex((int(hex_values[i], 16) - b) * (mod_inverse(m, n)) % n)
    cipher_hex.append(C)
  return cipher_hex

def read_image_to_hex(image_path):
  try:
    with open(image_path, "rb") as image:
      f = image.read()
      b = bytearray(f)
      array_of_hex = [hex(byte) for byte in b]
      return array_of_hex
  except FileNotFoundError:
    print("Error: File not found.")
    return None
  except ValueError as e:
    print("Error:", e)
    return None

def array_of_hex_to_bytearray(array_of_hex):
  bytearray_data = bytearray()
  for hex_value in array_of_hex:
    if hex_value.startswith('0x'):
      hex_value = hex_value[2:]
    byte_value = int(hex_value, 16)
    bytearray_data.append(byte_value)
  return bytearray_data

def create_file_from_bytes(file_path, bytes_data):
  try:
    with open(file_path, "wb") as file:
      file.write(bytes_data)
      print("File berhasil dibuat:", file_path)
  except Exception as e:
    print("Error:", e)

def find_m(cipher, plain, n):
  for i in range(1, n):
    if math.gcd(i, n) == 1:
      if (i * plain) % n == cipher:
        return i
  return -1

def find_b(cipher, plain, n):
  for i in range(1, n):
    if (i + plain) % n == cipher:
      return i
  return -1

JPG_HEADER = ['0xff', '0xd8']
def main():
  image_path = "./chall.jpg"
  n = 256
  
  hex_values = read_image_to_hex(image_path)
  if hex_values is not None:
    cipher0 = int(hex_values[0], 16)
    cipher1 = int(hex_values[1], 16)
    plain0 = int(JPG_HEADER[0], 16)
    plain1 = int(JPG_HEADER[1], 16)

    if (cipher1 > cipher0):
      m = find_m(cipher1 - cipher0, plain1 - plain0, n)
    else:
      m = find_m(cipher0 - cipher1, plain0 - plain1, n)
    b = find_b(cipher0, plain0 * m, n)
    plain_hex = affine_plain(hex_values, m, b, n)
    bytearray_plain = array_of_hex_to_bytearray(plain_hex)
    create_file_from_bytes("./flag.jpg", bytearray_plain)

if __name__ == "__main__":
  main()