import random

############ データを格納するための空配列を生成 ############
afterBin = []
cryptList = []
cryptSentence = []
toSentence = []
toKeySentence = []

############ 関数定義 ############
def listXOR(argA, argB):
    for a,b in zip(argA, argB):
        A = int(a,2)
        B = int(b,2)
        cryptSentence.append(bin(int(A) ^ int(B)))

def numXOR(argC, argD):
    C = int(argC,2)
    D = int(argD,2)
    return bin(int(C) ^ int(D))

def checkNum(checkNumber,listNum):
    randomNumber = bin(random.randint(33,126))
    retake = bin(int(checkNumber,2) ^ int(int(randomNumber,2)))
    if int(retake,2) > 32 and int(retake,2) < 127:
        print(retake, " :retake:○")
        cryptSentence[listNum] = retake
        cryptList[listNum] = randomNumber
    else:
        print(retake, " :retake:× 有効桁外。暗号鍵の再生成を実行。checkNum関数を再度呼び出します。")
        checkNum(afterBin[k], listNum)

def checkTail(checkTailNumber,listNum):
    randomNumber = bin(random.randint(33,126))
    retake = bin(int(checkTailNumber,2) ^ int(int(randomNumber,2)))
    if int(retake,2) == 32:
        print(retake + ":retake:× 末尾が半スペース。暗号鍵の再生成を実行。checkTail関数を 再度呼び出します。")
        checkTail(cryptSentence[listNum-1], listNum-1)
    else:
        print(retake + "retake:○")
        cryptSentence[listNum] = retake
        cryptList[listNum] = randomNumber


############ 暗号化対象文章の取得 ############
text = input("Enter the sentence you want to encrypt:")
beforeBin = list(text)

############ 暗号化対象文章を10進数→2進数に変換する ############
for i in beforeBin:
    afterBin.append((f'{ord(i):b}'.zfill(8)))
print("")
print("=================================================-")
print("暗号化対象を2進数に変換したものは以下")
print("2進数表記:", afterBin)
print("文字列の長さ:", len(afterBin))

############ 暗号鍵を2進数で作成する ############
listNum = len(afterBin)
for j in range(listNum):
    cryptList.append(bin(random.randint(33,126)))
print("")
print("=================================================-")
print("暗号鍵は以下")
print("2進数表記:", cryptList)
print("文字列の長さ:", len(cryptList))

############ 暗号化対象文章と暗号鍵を使い排他的論理和を取得する ###########
listXOR(afterBin, cryptList)
print("")
print("=================================================-")
print("上記で変換した2進数と鍵となる2進数でXORを実施し暗号化したものは以下")
print("2進数表記:" , cryptSentence)

############ 排他的論理和がASCIIの範囲内(有効桁33-126)であることを確認する ###########
############ ASCIIの範囲外(有効桁33-126)である場合暗号鍵を修正する ###########
k = 0
print("")
print("=================================================-")
print("ASCIIの有効桁内であることの確認")
for c in cryptSentence:
    if int(c,2) > 32 and int(c,2) < 127:
        print(c, " :○")
        k += 1
    else:
        print(c + " :× 有効桁外。暗号鍵修正の実行。checkNum関数を呼び出します。")
        checkNum(afterBin[k], k)
        k += 1
print("")
print("有効桁であることを確認した後の2進数表記")
print(cryptSentence)
print("有効桁であることを確認した後の暗号鍵（2進数表記）")
print(cryptList)

############ 排他的論理和の末尾がASCIIの半スペース（10進数：32及び2進数：00100000） ###########
############ 末尾がASCIIの半スペース(10進数：32及び2進数：00100000)である場合暗号鍵を修正する ###########
if int(cryptSentence[listNum-1],2) == 32:
    print(cryptSentence[listNum-1] + " :× 末尾が半スペースになることを回避する為暗号鍵の再生成を実行 checktail関数を呼び出します。")
    checktail(cryptSentence[listNum-1], listNum-1)
else:
    print(cryptSentence[listNum-1] + " :○")
print("")
print("末尾が半スペースで無いことを確認した後の2進数表記")
print(cryptSentence)
print("末尾が半スペースで無いことを確認した後の暗号鍵（2進数表記）")
print(cryptList)

############ 排他的論理和で計算した2進数を10進数に直し、ASCIIに変換し文字列に変換し文章を生成 ###########
for e in cryptSentence:
    e = int(e,2)
    toSentence.append(chr(e))
print("")
print("=================================================-")
print("暗号化した文章は以下")
print("".join(toSentence))
print("文字列の長さ:", len(toSentence))

############ 排他的論理和で計算した2進数を10進数に直し、ASCIIに変換し文字列に変換し暗号鍵を生成 ###########
for f in cryptList:
    f = int(f,2)
    toKeySentence.append(chr(f))
print("")
print("=================================================-")
print("暗号化に使用した鍵は以下")
print("".join(toKeySentence))
print("文字列の長さ:", len(toKeySentence))
