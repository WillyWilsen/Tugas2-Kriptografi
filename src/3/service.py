# Read cipher from file
file_name = "cipher.txt"
with open(file_name, "r") as file:
  cipher = file.read()
cipher = cipher.replace("\n", "")

# STEP 1: Mencari tabel frekuensi bigram dalam Bahasa Inggris

# Cipher bigram frequency in English
bigram_frequency = dict()
for i in range(0, len(cipher) - 1, 2):
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

# Iterasi 3
'''
Didapatkan contoh susunan key sebagai berikut.
T H E L X
X X X X X
X X X X X
X X X X X
X X X X X

Sehingga
HL -> te
LH -> et
'''
mapping_dict["HL"] = "te"
mapping_dict["LH"] = "et"

# Replace cipher with mapping_dict
cipher = replace_pairs(cipher, "HL", "LH", mapping_dict)
with open("mapping_cipher_3.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 3: ")
print(cipher)
print("\n")

# Iterasi 4
'''
Dari contoh susunan key tersebut, ET dipetakan menjadi hX. Karena jumlah ET banyak, maka ET diduga sebagai ha. Sehingga susunan key sebagai berikut.
T H E L A
X X X X X
X X X X X
X X X X X
X X X X X

Sehingga
TH -> at
HT -> ta
TE -> ah
ET -> ha
TL -> ae
LT -> ea
TA -> al
AT -> la
HA -> tl
AH -> lt
EA -> hl
AE -> lh
LA -> el
AL -> le
'''
mapping_dict["TH"] = "at"
mapping_dict["HT"] = "ta"
mapping_dict["TE"] = "ah"
mapping_dict["ET"] = "ha"
mapping_dict["TL"] = "ae"
mapping_dict["LT"] = "ea"
mapping_dict["TA"] = "al"
mapping_dict["AT"] = "la"
mapping_dict["HA"] = "tl"
mapping_dict["AH"] = "lt"
mapping_dict["EA"] = "hl"
mapping_dict["AE"] = "lh"
mapping_dict["LA"] = "el"
mapping_dict["AL"] = "le"

# Replace cipher with mapping_dict
cipher = replace_pairs(cipher, "TH", "HT", mapping_dict)
cipher = replace_pairs(cipher, "TE", "ET", mapping_dict)
cipher = replace_pairs(cipher, "TL", "LT", mapping_dict)
cipher = replace_pairs(cipher, "TA", "AT", mapping_dict)
cipher = replace_pairs(cipher, "HA", "AH", mapping_dict)
cipher = replace_pairs(cipher, "EA", "AE", mapping_dict)
cipher = replace_pairs(cipher, "LA", "AL", mapping_dict)
with open("mapping_cipher_4.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 4: ")
print(cipher)
print("\n")

# Iterasi 5
'''
MH dan HM sama-sama memiliki jumlah yang banyak muncul dan apabila dilihat dari pola kata, thHM muncul 28 kali dan thMH muncul 1 kali sehingga kemungkinan
HM -> er
MH -> re
'''
mapping_dict["HM"] = "er"
mapping_dict["MH"] = "re"

# Replace cipher with mapping_dict
cipher = replace_pairs(cipher, "HM", "MH", mapping_dict)
with open("mapping_cipher_5.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 5: ")
print(cipher)
print("\n")

# Iterasi 6

for i in cipher:
  if i.islower():
    print(i, end="")
  else:
    print(" ", end="")