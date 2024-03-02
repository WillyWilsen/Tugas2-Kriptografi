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
'''
Berdasarkan pasangan huruf ketiga yang paling sering muncul pada bigram frequency, dapat dilakukan pemetaan pasangan huruf sebagai berikut.
QX -> in
XQ -> ni
Berdasarkan kata allafterall, BL -> ft dan LB -> tf
Berdasar kata theother, LD -> eo dan DL -> oe
Berdasar kata untilthe, QF -> un dan FQ -> nu
Berdasar kata thestreet, VA -> st dan AV -> ts
Berdasar kata everywhere, KH -> yw dan HK -> wy, TM -> ev dan MT -> ve
Berdasar kata thingthey, CA -> gt dan AC -> tg
Berdasar kata thatthenat, QE -> en dan EQ -> ne
Berdasar kata theotherendofthestreethe, OG -> do dan GO -> od
Berdasar kata allafterallhe'sdoneall, AM -> es dan MA -> se
Berdasar kata theywant, EX -> an dan XE -> na
Berdasar kata heleftthehouse, PO -> ou dan OP -> uo
Berdasar kata hethought, KA -> gh dan AK -> hg
Berdasar kata they, HQ -> ey dan QH -> ye
Berdasar kata hadnever, ME -> dn dan EM -> nd
Berdasar kata theywererelate, NH -> we dan HN -> ew
Berdasar kata leftinthewholestreet, LK -> ho dan KL -> oh
Berdasar kata outside, QG -> id dan GQ -> di
Berdasar kata understand, MQ -> de dan QM -> ed, MV -> rs dan VM -> sr
Berdasar kata which, AY -> hi dan YA -> ih, KT -> ch dan TK -> hc
Berdasar kata lights, AU -> li dan UA -> il
Berdasar kata whichwerethexeyes, AN -> ex dan NA -> xe
'''
# Bigram frequency urutan ke-3
mapping_dict["QX"] = "in"
mapping_dict["XQ"] = "ni"

# allafterall
mapping_dict["BL"] = "ft"
mapping_dict["LB"] = "tf"

# theother
mapping_dict["LD"] = "eo"
mapping_dict["DL"] = "oe"

# untilthe
mapping_dict["QF"] = "un"
mapping_dict["FQ"] = "nu"

# thestreet
mapping_dict["VA"] = "st"
mapping_dict["AV"] = "ts"

# everywhere
mapping_dict["KH"] = "yw"
mapping_dict["HK"] = "wy"
mapping_dict["TM"] = "ev"
mapping_dict["MT"] = "ve"

# thingthey
mapping_dict["CA"] = "gt"
mapping_dict["AC"] = "tg"

# thatthenat
mapping_dict["QE"] = "en"
mapping_dict["EQ"] = "ne"

# theotherendofthestreethe
mapping_dict["OG"] = "do"
mapping_dict["GO"] = "od"

# allafterallhe'sdoneall
mapping_dict["AM"] = "es"
mapping_dict["MA"] = "se"

# theywant
mapping_dict["EX"] = "an"
mapping_dict["XE"] = "na"

# heleftthehouse
mapping_dict["PO"] = "ou"
mapping_dict["OP"] = "uo"

# hethought
mapping_dict["KA"] = "gh"
mapping_dict["AK"] = "hg"

# they
mapping_dict["HQ"] = "ey"
mapping_dict["QH"] = "ye"

# hadnever
mapping_dict["ME"] = "dn"
mapping_dict["EM"] = "nd"

# theywererelate
mapping_dict["NH"] = "we"
mapping_dict["HN"] = "ew"

# leftinthewholestreet
mapping_dict["LK"] = "ho"
mapping_dict["KL"] = "oh"

# outside
mapping_dict["QG"] = "id"
mapping_dict["GQ"] = "di"

# understand
mapping_dict["MQ"] = "de"
mapping_dict["QM"] = "ed"
mapping_dict["MV"] = "rs"
mapping_dict["VM"] = "sr"

# which
mapping_dict["AY"] = "hi"
mapping_dict["YA"] = "ih"
mapping_dict["KT"] = "ch"
mapping_dict["TK"] = "hc"

# lights
mapping_dict["AU"] = "li"
mapping_dict["UA"] = "il"

# whichwerethexeyes
mapping_dict["AN"] = "ex"
mapping_dict["NA"] = "xe"

# Replace cipher with mapping_dict
cipher = replace_pairs(cipher, "QX", "XQ", mapping_dict)
cipher = replace_pairs(cipher, "BL", "LB", mapping_dict)
cipher = replace_pairs(cipher, "LD", "DL", mapping_dict)
cipher = replace_pairs(cipher, "QF", "FQ", mapping_dict)
cipher = replace_pairs(cipher, "VA", "AV", mapping_dict)
cipher = replace_pairs(cipher, "KH", "HK", mapping_dict)
cipher = replace_pairs(cipher, "TM", "MT", mapping_dict)
cipher = replace_pairs(cipher, "CA", "AC", mapping_dict)
cipher = replace_pairs(cipher, "QE", "EQ", mapping_dict)
cipher = replace_pairs(cipher, "OG", "GO", mapping_dict)
cipher = replace_pairs(cipher, "AM", "MA", mapping_dict)
cipher = replace_pairs(cipher, "EX", "XE", mapping_dict)
cipher = replace_pairs(cipher, "PO", "OP", mapping_dict)
cipher = replace_pairs(cipher, "KA", "AK", mapping_dict)
cipher = replace_pairs(cipher, "HQ", "QH", mapping_dict)
cipher = replace_pairs(cipher, "ME", "EM", mapping_dict)
cipher = replace_pairs(cipher, "NH", "HN", mapping_dict)
cipher = replace_pairs(cipher, "LK", "KL", mapping_dict)
cipher = replace_pairs(cipher, "QG", "GQ", mapping_dict)
cipher = replace_pairs(cipher, "MQ", "QM", mapping_dict)
cipher = replace_pairs(cipher, "MV", "VM", mapping_dict)
cipher = replace_pairs(cipher, "AY", "YA", mapping_dict)
cipher = replace_pairs(cipher, "KT", "TK", mapping_dict)
cipher = replace_pairs(cipher, "AU", "UA", mapping_dict)
cipher = replace_pairs(cipher, "AN", "NA", mapping_dict)
with open("mapping_cipher_6.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 5: ")
print(cipher)
print("\n")

'''
Kemudian, dicari sumber yang sedemikian mendekati plain teks.
Dikutip dari https://www.hp-lexicon.org/2002/01/02/the-put-outer-and-magic-on-privet-drive/

Didapat:
[Dumbledore] found what he was looking for in his inside pocket.
It seemed to be a silver cigarette lighter.
He flicked it open, held it up in the air, and clicked it.
The nearest street lamp went out with a little pop.
He clicked it again—the next lamp flickered into darkness.
Twelve times he clicked the Put-Outer, until the only lights left on the whole street were two tiny pinpricks in the distance, which were the eyes of the cat watching him. 
If anyone looked out of their window now, even beady-eyed Mrs. Dursley, they wouldn't be able to see anything that was happening down on the pavement.
Dumbledore slipped the Put-Outer back inside his cloak and set off down the street toward number four, where he sat down on the wall next to the cat.

Maka, dapat dilakukan pemetaan sebagai berikut.
KN -> dt, NK -> td
OX -> gf, XO -> fg
XM -> ns, MX -> sn
GK -> oc, KG -> co
VK -> rc, KV -> cr
GS -> ig, SG -> gi
HS -> ar, SH -> ra
WY -> rh, YW -> hr
LN -> ef, NL -> fe
EO -> ld, OE -> dl
OK -> dc, KO -> cd
PS -> mp, SP -> pm
PF -> op, FP -> po
SI -> ga, IS -> ag
ES -> am, SE -> ma
FL -> pf, LF -> fp
GE -> da, EG -> ad
WR -> rk, RW -> kr
XA -> sx, AX -> xs
TP -> lv, PT -> vl
OT -> cl, TO -> lc
ZG -> ic, GZ -> ci
DH -> ke, HD -> ek
AZ -> ti, ZA -> it
HU -> ly, UH -> yl
UR -> yp, RU -> py
SM -> pr, MS -> rp
GR -> ks, RG -> sk
GX -> is, XG -> si
BD -> nc, DB -> cn
PL -> of, LP -> fo
TD -> ec, DT -> ce
XH -> wa, HX -> aw
ZV -> tc, VZ -> ct
XD -> ng, DX -> gn
SQ -> mi, QS -> im
XL -> fa, LX -> af
WQ -> ny, QW -> yn
DF -> on, FD -> no
GF -> ox, FG -> xo
GD -> ok, DG -> ko
LC -> to, CL -> ot
YS -> ir, SY -> ri
XY -> wi, YX -> iw
KF -> ow, FK -> wo
KQ -> dy, QK -> yd
PM -> mr, MP -> rm
MG -> sd, GM -> ds
YP -> ur, PY -> ru
PA -> sl, AP -> ls
OU -> ul, UO -> lu
ZT -> tb, TZ -> bt
FT -> bl, TF -> lb
GP -> os, PG -> so
HB -> tw, BH -> wt
IX -> as, XI -> sa
SF -> px, FS -> xp
ML -> pe, LM -> ep
NF -> wn, FN -> nw
TS -> av, ST -> va
QN -> em, NQ -> me
EC -> td, CE -> dt
QP -> um, PQ -> mu
KP -> or, PK -> ro
FO -> pu, OF -> up
ZL -> ut, LZ -> tu
XT -> ba, TX -> ab
KD -> ck, DK -> kc
VG -> sc, GV -> cs
UP -> lo, PU -> ol
HG -> ak, GH -> ka
NO -> fd, ON -> df
BE -> nt, EB -> tn
MK -> rd, KM -> dr
NT -> be, TN -> eb
PW -> rf, WP -> fr
WH -> rw, HW -> wr
AF -> lx, FA -> xl
EF -> ln, FE -> nl
AB -> tx, BA -> xt
'''
mapping_dict["KN"] = "dt"
mapping_dict["NK"] = "td"
mapping_dict["OX"] = "gf"
mapping_dict["XO"] = "fg"
mapping_dict["XM"] = "ns"
mapping_dict["MX"] = "sn"
mapping_dict["GK"] = "oc"
mapping_dict["KG"] = "co"
mapping_dict["VK"] = "rc"
mapping_dict["KV"] = "cr"
mapping_dict["GS"] = "ig"
mapping_dict["SG"] = "gi"
mapping_dict["HS"] = "ar"
mapping_dict["SH"] = "ra"
mapping_dict["WY"] = "rh"
mapping_dict["YW"] = "hr"
mapping_dict["LN"] = "ef"
mapping_dict["NL"] = "fe"
mapping_dict["EO"] = "ld"
mapping_dict["OE"] = "dl"
mapping_dict["OK"] = "dc"
mapping_dict["KO"] = "cd"
mapping_dict["PS"] = "mp"
mapping_dict["SP"] = "pm"
mapping_dict["PF"] = "op"
mapping_dict["FP"] = "po"
mapping_dict["SI"] = "ga"
mapping_dict["IS"] = "ag"
mapping_dict["ES"] = "am"
mapping_dict["SE"] = "ma"
mapping_dict["FL"] = "pf"
mapping_dict["LF"] = "fp" 
mapping_dict["GE"] = "da"
mapping_dict["EG"] = "ad"
mapping_dict["WR"] = "rk"
mapping_dict["RW"] = "kr"
mapping_dict["XA"] = "sx"
mapping_dict["AX"] = "xs"
mapping_dict["TP"] = "lv"
mapping_dict["PT"] = "vl"
mapping_dict["OT"] = "cl"
mapping_dict["TO"] = "lc"
mapping_dict["ZG"] = "ic"
mapping_dict["GZ"] = "ci"
mapping_dict["DH"] = "ke"
mapping_dict["HD"] = "ek"
mapping_dict["AZ"] = "ti"
mapping_dict["ZA"] = "it"
mapping_dict["HU"] = "ly"
mapping_dict["UH"] = "yl"
mapping_dict["UR"] = "yp"
mapping_dict["RU"] = "py"
mapping_dict["SM"] = "pr"
mapping_dict["MS"] = "rp"
mapping_dict["GR"] = "ks"
mapping_dict["RG"] = "sk"
mapping_dict["GX"] = "is"
mapping_dict["XG"] = "si"
mapping_dict["BD"] = "nc"
mapping_dict["DB"] = "cn"
mapping_dict["PL"] = "of"
mapping_dict["LP"] = "fo"
mapping_dict["TD"] = "ec"
mapping_dict["DT"] = "ce"
mapping_dict["XH"] = "wa"
mapping_dict["HX"] = "aw"
mapping_dict["ZV"] = "tc"
mapping_dict["VZ"] = "ct"
mapping_dict["XD"] = "ng"
mapping_dict["DX"] = "gn"
mapping_dict["SQ"] = "mi"
mapping_dict["QS"] = "im"
mapping_dict["XL"] = "fa"
mapping_dict["LX"] = "af"
mapping_dict["WQ"] = "ny"
mapping_dict["QW"] = "yn"
mapping_dict["DF"] = "on"
mapping_dict["FD"] = "no"
mapping_dict["GF"] = "ox"
mapping_dict["FG"] = "xo"
mapping_dict["GD"] = "ok"
mapping_dict["DG"] = "ko"
mapping_dict["LC"] = "to"
mapping_dict["CL"] = "ot"
mapping_dict["YS"] = "ir"
mapping_dict["SY"] = "ri"
mapping_dict["XY"] = "wi"
mapping_dict["YX"] = "iw"
mapping_dict["KF"] = "ow"
mapping_dict["FK"] = "wo"
mapping_dict["FW"] = "nb"
mapping_dict["WF"] = "bn"
mapping_dict["KQ"] = "dy"
mapping_dict["QK"] = "yd"
mapping_dict["PM"] = "mr"
mapping_dict["MP"] = "rm"
mapping_dict["MG"] = "sd"
mapping_dict["GM"] = "ds"
mapping_dict["YP"] = "ur"
mapping_dict["PY"] = "ru"
mapping_dict["PA"] = "sl"
mapping_dict["AP"] = "ls"
mapping_dict["OU"] = "ul"
mapping_dict["UO"] = "lu"
mapping_dict["ZT"] = "tb"
mapping_dict["TZ"] = "bt"
mapping_dict["FT"] = "bl"
mapping_dict["TF"] = "lb"
mapping_dict["GP"] = "os"
mapping_dict["PG"] = "so"
mapping_dict["HB"] = "tw"
mapping_dict["BH"] = "wt"
mapping_dict["IX"] = "as"
mapping_dict["XI"] = "sa"
mapping_dict["SF"] = "px"
mapping_dict["FS"] = "xp"
mapping_dict["ML"] = "pe"
mapping_dict["LM"] = "ep"
mapping_dict["NF"] = "wn"
mapping_dict["FN"] = "nw"
mapping_dict["TS"] = "av"
mapping_dict["ST"] = "va"
mapping_dict["QN"] = "em"
mapping_dict["NQ"] = "me"
mapping_dict["EC"] = "td"
mapping_dict["CE"] = "dt"
mapping_dict["QP"] = "um"
mapping_dict["PQ"] = "mu"
mapping_dict["KP"] = "or"
mapping_dict["PK"] = "ro"
mapping_dict["FO"] = "pu"
mapping_dict["OF"] = "up"
mapping_dict["ZL"] = "ut"
mapping_dict["LZ"] = "tu"
mapping_dict["XT"] = "ba"
mapping_dict["TX"] = "ab"
mapping_dict["KD"] = "ck"
mapping_dict["DK"] = "kc"
mapping_dict["VG"] = "sc"
mapping_dict["GV"] = "cs"
mapping_dict["UP"] = "lo"
mapping_dict["PU"] = "ol"
mapping_dict["HG"] = "ak"
mapping_dict["GH"] = "ka"
mapping_dict["NO"] = "fd"
mapping_dict["ON"] = "df"
mapping_dict["BE"] = "nt"
mapping_dict["EB"] = "tn"
mapping_dict["MK"] = "rd"
mapping_dict["KM"] = "dr"
mapping_dict["NT"] = "be"
mapping_dict["TN"] = "eb"
mapping_dict["PW"] = "rf"
mapping_dict["WP"] = "fr"
mapping_dict["WH"] = "rw"
mapping_dict["HW"] = "wr"
mapping_dict["AF"] = "lx"
mapping_dict["FA"] = "xl"
mapping_dict["EF"] = "ln"
mapping_dict["FE"] = "nl"
mapping_dict["AB"] = "tx"
mapping_dict["BA"] = "xt"

# Replace cipher with mapping_dict
cipher = replace_pairs(cipher, "KN", "NK", mapping_dict)
cipher = replace_pairs(cipher, "OX", "XO", mapping_dict)
cipher = replace_pairs(cipher, "XM", "MX", mapping_dict)
cipher = replace_pairs(cipher, "GK", "KG", mapping_dict)
cipher = replace_pairs(cipher, "VK", "KV", mapping_dict)
cipher = replace_pairs(cipher, "GS", "SG", mapping_dict)
cipher = replace_pairs(cipher, "HS", "SH", mapping_dict)
cipher = replace_pairs(cipher, "WY", "YW", mapping_dict)
cipher = replace_pairs(cipher, "LN", "NL", mapping_dict)
cipher = replace_pairs(cipher, "EO", "OE", mapping_dict)
cipher = replace_pairs(cipher, "OK", "KO", mapping_dict)
cipher = replace_pairs(cipher, "PS", "SP", mapping_dict)
cipher = replace_pairs(cipher, "PF", "FP", mapping_dict)
cipher = replace_pairs(cipher, "SI", "IS", mapping_dict)
cipher = replace_pairs(cipher, "ES", "SE", mapping_dict)
cipher = replace_pairs(cipher, "FL", "LF", mapping_dict)
cipher = replace_pairs(cipher, "GE", "EG", mapping_dict)
cipher = replace_pairs(cipher, "WR", "RW", mapping_dict)
cipher = replace_pairs(cipher, "XA", "AX", mapping_dict)
cipher = replace_pairs(cipher, "TP", "PT", mapping_dict)
cipher = replace_pairs(cipher, "OT", "TO", mapping_dict)
cipher = replace_pairs(cipher, "ZG", "GZ", mapping_dict)
cipher = replace_pairs(cipher, "DH", "HD", mapping_dict)
cipher = replace_pairs(cipher, "AZ", "ZA", mapping_dict)
cipher = replace_pairs(cipher, "HU", "UH", mapping_dict)
cipher = replace_pairs(cipher, "UR", "RU", mapping_dict)
cipher = replace_pairs(cipher, "SM", "MS", mapping_dict)
cipher = replace_pairs(cipher, "GR", "RG", mapping_dict)
cipher = replace_pairs(cipher, "GX", "XG", mapping_dict)
cipher = replace_pairs(cipher, "BD", "DB", mapping_dict)
cipher = replace_pairs(cipher, "PL", "LP", mapping_dict)
cipher = replace_pairs(cipher, "TD", "DT", mapping_dict)
cipher = replace_pairs(cipher, "XH", "HX", mapping_dict)
cipher = replace_pairs(cipher, "ZV", "VZ", mapping_dict)
cipher = replace_pairs(cipher, "XD", "DX", mapping_dict)
cipher = replace_pairs(cipher, "SQ", "QS", mapping_dict)
cipher = replace_pairs(cipher, "XL", "LX", mapping_dict)
cipher = replace_pairs(cipher, "WQ", "QW", mapping_dict)
cipher = replace_pairs(cipher, "DF", "FD", mapping_dict)
cipher = replace_pairs(cipher, "GF", "FG", mapping_dict)
cipher = replace_pairs(cipher, "GD", "DG", mapping_dict)
cipher = replace_pairs(cipher, "LC", "CL", mapping_dict)
cipher = replace_pairs(cipher, "YS", "SY", mapping_dict)
cipher = replace_pairs(cipher, "XY", "YX", mapping_dict)
cipher = replace_pairs(cipher, "KF", "FK", mapping_dict)
cipher = replace_pairs(cipher, "FW", "WF", mapping_dict)
cipher = replace_pairs(cipher, "KQ", "QK", mapping_dict)
cipher = replace_pairs(cipher, "PM", "MP", mapping_dict)
cipher = replace_pairs(cipher, "MG", "GM", mapping_dict)
cipher = replace_pairs(cipher, "YP", "PY", mapping_dict)
cipher = replace_pairs(cipher, "PA", "AP", mapping_dict)
cipher = replace_pairs(cipher, "OU", "UO", mapping_dict)
cipher = replace_pairs(cipher, "ZT", "TZ", mapping_dict)
cipher = replace_pairs(cipher, "FT", "TF", mapping_dict)
cipher = replace_pairs(cipher, "GP", "PG", mapping_dict)
cipher = replace_pairs(cipher, "HB", "BH", mapping_dict)
cipher = replace_pairs(cipher, "IX", "XI", mapping_dict)
cipher = replace_pairs(cipher, "SF", "FS", mapping_dict)
cipher = replace_pairs(cipher, "ML", "LM", mapping_dict)
cipher = replace_pairs(cipher, "NF", "FN", mapping_dict)
cipher = replace_pairs(cipher, "TS", "ST", mapping_dict)
cipher = replace_pairs(cipher, "QN", "NQ", mapping_dict)
cipher = replace_pairs(cipher, "EC", "CE", mapping_dict)
cipher = replace_pairs(cipher, "QP", "PQ", mapping_dict)
cipher = replace_pairs(cipher, "KP", "PK", mapping_dict)
cipher = replace_pairs(cipher, "FO", "OF", mapping_dict)
cipher = replace_pairs(cipher, "ZL", "LZ", mapping_dict)
cipher = replace_pairs(cipher, "XT", "TX", mapping_dict)
cipher = replace_pairs(cipher, "KD", "DK", mapping_dict)
cipher = replace_pairs(cipher, "VG", "GV", mapping_dict)
cipher = replace_pairs(cipher, "UP", "PU", mapping_dict)
cipher = replace_pairs(cipher, "HG", "GH", mapping_dict)
cipher = replace_pairs(cipher, "NO", "ON", mapping_dict)
cipher = replace_pairs(cipher, "BE", "EB", mapping_dict)
cipher = replace_pairs(cipher, "MK", "KM", mapping_dict)
cipher = replace_pairs(cipher, "NT", "TN", mapping_dict)
cipher = replace_pairs(cipher, "PW", "WP", mapping_dict)
cipher = replace_pairs(cipher, "WH", "HW", mapping_dict)
cipher = replace_pairs(cipher, "AF", "FA", mapping_dict)
cipher = replace_pairs(cipher, "EF", "FE", mapping_dict)
cipher = replace_pairs(cipher, "AB", "BA", mapping_dict)
with open("mapping_cipher_7.txt", "w") as file:
  file.write(cipher)
print("Mapping cipher 7: ")
print(cipher)
print("\n")

'''
Didapat hasil plain teks: https://media.bloomsbury.com/rep/files/harry-potter-and-the-philosophers-stone.pdf
'''