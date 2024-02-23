from collections import defaultdict

def find_repeated_patterns(text, length=3):
    patterns = defaultdict(list)
    for i in range(len(text) - length):
      pattern = text[i:i+length]
      indices = []
      for j in range(i+1, len(text) - length + 1):
        if text[j:j+length] == pattern:
          indices.append(j - i)
      if indices:
        patterns[pattern].extend(indices)
    return {pattern: indices for pattern, indices in patterns.items() if len(indices) > 1}

def gcd(a, b):
    while b:
      a, b = b, a % b
    return a

def find_key_length(indices):
    distances = []
    for i in range(len(indices) - 1):
      for j in range(i + 1, len(indices)):
        distances.append(abs(indices[i] - indices[j]))
    key_length = distances[0]
    for distance in distances[1:]:
      key_length = gcd(key_length, distance)
    return key_length

def kasiski_method(ciphertext):
    repeated_patterns = find_repeated_patterns(ciphertext)
    pattern_indices = {pattern: sorted(indices) for pattern, indices in repeated_patterns.items()}
    key_length_candidates = []
    for indices in pattern_indices.values():
      key_length_candidates.append(find_key_length(indices))
    key_length = max(set(key_length_candidates), key=key_length_candidates.count)
    return key_length

# Read cipher from file
file_name = "cipher.txt"
with open(file_name, "r") as file:
  cipher = file.read()
cipher = cipher.replace("\n", "")
possible_key_length = kasiski_method(cipher)

'''
Kelompokkan cipher setiap kelipatan key, dimulai dari huruf cipherteks pertama, kedua, dan seterusnya.
'''
cipher_grouped = {i: "" for i in range(possible_key_length)}
for i, letter in enumerate(cipher):
  cipher_grouped[i % possible_key_length] += letter
print(cipher_grouped)

'''
Mencari huruf yang paling sering muncul pada setiap kelompok cipher.
'''
letter_frequency = dict()
for i, group in cipher_grouped.items():
  letter_frequency[i] = dict()
  for letter in group:
    if letter in letter_frequency[i]:
      letter_frequency[i][letter] += 1
    else:
      letter_frequency[i][letter] = 1
  letter_frequency[i] = dict(sorted(letter_frequency[i].items(), key=lambda item: item[1], reverse=True))
print(letter_frequency)

'''
Mencari huruf kunci dengan menerka dan menguji coba, didapat key = CHEONKIMSONG
'''
