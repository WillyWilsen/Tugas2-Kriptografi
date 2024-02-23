# Read cipher from file
file_name = "cipher.txt"
with open(file_name, "r") as file:
  cipher = file.read()
cipher = cipher.replace("\n", "")

# STEP 1: Mencari tabel frekuensi kemunculan huruf, bigram, dan trigram dalam Bahasa Inggri

# Cipher letter frequency in English
letter_frequency = dict()
for letter in cipher:
  if letter.isalpha():
    if letter in letter_frequency:
      letter_frequency[letter] += 1
    else:
      letter_frequency[letter] = 1
letter_frequency = dict(sorted(letter_frequency.items(), key=lambda item: item[1], reverse=True))
print("Cipher letter frequency in English: ")
for letter, frequency in letter_frequency.items():
  print(f"{letter}: {frequency}", end=", ")
print("\n")  

# Cipher bigram frequency in English
bigram_frequency = dict()
for i in range(len(cipher) - 1):
  bigram = cipher[i:i+2]
  if bigram.isalpha():
    if bigram in bigram_frequency:
      bigram_frequency[bigram] += 1
    else:
      bigram_frequency[bigram] = 1
bigram_frequency = dict(sorted(bigram_frequency.items(), key=lambda item: item[1], reverse=True))
print("Cipher bigram frequency in English: ")
for bigram, frequency in bigram_frequency.items():
  print(f"{bigram}: {frequency}", end=", ")
print("\n")

# Cipher trigram frequency in English
trigram_frequency = dict()
for i in range(len(cipher) - 2):
  trigram = cipher[i:i+3]
  if trigram.isalpha():
    if trigram in trigram_frequency:
      trigram_frequency[trigram] += 1
    else:
      trigram_frequency[trigram] = 1
trigram_frequency = dict(sorted(trigram_frequency.items(), key=lambda item: item[1], reverse=True))
print("Cipher trigram frequency in English: ")
for trigram, frequency in trigram_frequency.items():
  print(f"{trigram}: {frequency}", end=", ")
print("\n")

# STEP 2: Melakukan trial dan error dalam bentuk iterasi

mapping_dict = dict()

# Iterasi 1
'''
Berdasarkan huruf yang sering muncul pada letter frequency, bigram frequency, dan trigram frequency, dapat dilakukan pemetaan sebagai berikut.
H -> t
Z -> h
E -> e
'''
mapping_dict["H"] = "t"
mapping_dict["Z"] = "h"
mapping_dict["E"] = "e"

# Replace cipher with mapping_dict
for key, value in mapping_dict.items():
  cipher = cipher.replace(key, value)
with open("mapping_cipher_1.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 1: ")
print(cipher)
print("\n")

# Iterasi 2
'''
HZYH dipetakan menjadi th*t, kemungkinan Y -> a
'''
mapping_dict["Y"] = "a"

# Replace cipher with mapping_dict
for key, value in mapping_dict.items():
  cipher = cipher.replace(key, value)
with open("mapping_cipher_2.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 2: ")
print(cipher)
print("\n")

# Iterasi 3
'''
Atate dan theAe dipetakan menjadi state dan these, kemungkinan A -> s
'''
mapping_dict["A"] = "s"

# Replace cipher with mapping_dict
for key, value in mapping_dict.items():
  cipher = cipher.replace(key, value)
with open("mapping_cipher_3.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 3: ")
print(cipher)
print("\n")

# Iterasi 4
'''
aFC dapat dipetakan menjadi and, kemungkinan F -> n, C -> d
'''
mapping_dict["F"] = "n"
mapping_dict["C"] = "d"

# Replace cipher with mapping_dict
for key, value in mapping_dict.items():
  cipher = cipher.replace(key, value)
with open("mapping_cipher_4.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 4: ")
print(cipher)
print("\n")

# Iterasi 5
'''
Jumlah LF dan L cukup besar diduga L -> i
'''
mapping_dict["L"] = "i"

# Replace cipher with mapping_dict
for key, value in mapping_dict.items():
  cipher = cipher.replace(key, value)
with open("mapping_cipher_5.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 5: ")
print(cipher)
print("\n")

# Iterasi 6
'''
XRntent dipetakan menjadi content dan jumlah R cukup besar, kemungkinan X -> c, R -> o
'''
mapping_dict["X"] = "c"
mapping_dict["R"] = "o"

# Replace cipher with mapping_dict
for key, value in mapping_dict.items():
  cipher = cipher.replace(key, value)
with open("mapping_cipher_6.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 6: ")
print(cipher)
print("\n")

# Iterasi 7
'''
TitheachotheB dipetakan menjadi witheachother, kemungkinan T -> w, B -> r
'''
mapping_dict["T"] = "w"
mapping_dict["B"] = "r"

# Replace cipher with mapping_dict
for key, value in mapping_dict.items():
  cipher = cipher.replace(key, value)
with open("mapping_cipher_7.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 7: ")
print(cipher)
print("\n")

# Iterasi 8
'''
VrodUces dipetakan menjadi produces, kemungkinan V -> p, U -> u
'''
mapping_dict["V"] = "p"
mapping_dict["U"] = "u"

# Replace cipher with mapping_dict
for key, value in mapping_dict.items():
  cipher = cipher.replace(key, value)
with open("mapping_cipher_8.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 8: ")
print(cipher)
print("\n")

# Iterasi 9
'''
crMpto dipetakan menjadi crypto, kemungkinan M -> y
'''
mapping_dict["M"] = "y"

# Replace cipher with mapping_dict
for key, value in mapping_dict.items():
  cipher = cipher.replace(key, value)
with open("mapping_cipher_9.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 9: ")
print(cipher)
print("\n")

# Iterasi 10
'''
GundaPentaW dipetakan menjadi fundamental, kemungkinan G -> f, P -> m, W -> l
'''
mapping_dict["G"] = "f"
mapping_dict["P"] = "m"
mapping_dict["W"] = "l"

# Replace cipher with mapping_dict
for key, value in mapping_dict.items():
  cipher = cipher.replace(key, value)
with open("mapping_cipher_10.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 10: ")
print(cipher)
print("\n")

# Iterasi 11
'''
cryptoloOy dipetakan menjadi cryptology, kemungkinan O -> g
'''
mapping_dict["O"] = "g"

# Replace cipher with mapping_dict
for key, value in mapping_dict.items():
  cipher = cipher.replace(key, value)
with open("mapping_cipher_11.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 11: ")
print(cipher)
print("\n")

# Iterasi 12
'''
Kranches dipetakan menjadi branches, kemungkinan K -> b
'''
mapping_dict["K"] = "b"

# Replace cipher with mapping_dict
for key, value in mapping_dict.items():
  cipher = cipher.replace(key, value)
with open("mapping_cipher_12.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 12: ")
print(cipher)
print("\n")

# Iterasi 13
'''
eDistence dipetakan menjadi existence, kemungkinan D -> x
'''
mapping_dict["D"] = "x"

# Replace cipher with mapping_dict
for key, value in mapping_dict.items():
  cipher = cipher.replace(key, value)
with open("mapping_cipher_13.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 13: ")
print(cipher)
print("\n")

# Iterasi 14
'''
oNer dipetakan menjadi over, kemungkinan N -> v
'''
mapping_dict["N"] = "v"

# Replace cipher with mapping_dict
for key, value in mapping_dict.items():
  cipher = cipher.replace(key, value)
with open("mapping_cipher_14.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 14: ")
print(cipher)
print("\n")

# Iterasi 15
'''
techniQue and subJect dipetakan menjadi technique dan subject, kemungkinan Q -> q, J -> j
'''
mapping_dict["Q"] = "q"
mapping_dict["J"] = "j"

# Replace cipher with mapping_dict
for key, value in mapping_dict.items():
  cipher = cipher.replace(key, value)
with open("mapping_cipher_15.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 15: ")
print(cipher)
print("\n")

# Iterasi 16
'''
cryptanalyS dan codebreaIing dipetakan menjadi cryptanalyst dan codebreaking, kemungkinan S -> t, I -> k
'''
mapping_dict["S"] = "t"
mapping_dict["I"] = "k"

# Replace cipher with mapping_dict
for key, value in mapping_dict.items():
  cipher = cipher.replace(key, value)
with open("mapping_cipher_16.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 16: ")
print(cipher)
print("\n")