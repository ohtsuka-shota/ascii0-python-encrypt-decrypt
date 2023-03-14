############ 復号化対象の文章と暗号鍵を取得 ############
inputEncryptedSentence = input("暗号文:")
inputEncryptedKey = input("暗号鍵:")

############ データを格納するための空配列を生成 ############
beforeBin = list(inputEncryptedSentence)
beforeKeyBin = list(inputEncryptedKey)
afterBin = []
afterKeyBin = []
cryptList = []
cryptSentence = []
toDec = []
toSentence = []

############ 復号対象の文章を2進数に変換 ############
for i in beforeBin:
    afterBin.append((f'{ord(i):b}'.zfill(8)))

############ 暗号鍵を2進数に変換 ############
for i in beforeKeyBin:
    afterKeyBin.append((f'{ord(i):b}'.zfill(8)))

############ 復号対象の文章と暗号鍵を使用し排他的論理和を取得 ############
for a,b in zip(afterBin, afterKeyBin):
    A = int(a,2)
    B = int(b,2)
    cryptSentence.append(bin(int(A) ^ int(B)))

############ 復号対象の文章を復号化する ############
for c in cryptSentence:
    c = int(c,2)
    toSentence.append(chr(c))
print("")
print("=================================================-")
print("復号化した文章は以下")
print("".join(toSentence))
