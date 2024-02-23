# Read cipher from file
file_name = "cipher.txt"
with open(file_name, "r") as file:
  cipher = file.read()
cipher = cipher.replace("\n", "")

# STEP 1: Mencari tabel frekuensi bigram dalam Bahasa Inggris

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

# STEP 2: Melakukan trial dan error dalam bentuk iterasi terhadap pasangan huruf

def replace_pairs(text, pair_1, pair_2, mapping_dict):
  replaced_text = ""
  i = 0
  while i < len(text) - 1:
    pair = text[i:i+2]
    if pair in mapping_dict:
      if (pair == pair_1 or pair == pair_2):
        replaced_text += mapping_dict[pair]
        i += 2
        continue
    replaced_text += pair
    i += 2
  return replaced_text

mapping_dict = dict()

# Iterasi 1
'''
Berdasarkan pasangan huruf yang paling sering muncul pada bigram frequency, dapat dilakukan pemetaan pasangan huruf sebagai berikut.
HE -> th
EH -> ht
'''
mapping_dict["HE"] = "th"
mapping_dict["EH"] = "ht"

# Replace cipher with mapping_dict
cipher = replace_pairs(cipher, "HE", "EH", mapping_dict)
with open("mapping_cipher_1.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 1: ")
print(cipher)
print("\n")

# Iterasi 2
'''
Berdasarkan pasangan huruf kedua yang paling sering muncul pada bigram frequency, dapat dilakukan pemetaan pasangan huruf sebagai berikut.
EL -> he
LE -> eh
'''
mapping_dict["EL"] = "he"
mapping_dict["LE"] = "eh"

# Replace cipher with mapping_dict
cipher = replace_pairs(cipher, "EL", "LE", mapping_dict)
with open("mapping_cipher_2.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 2: ")
print(cipher)
print("\n")