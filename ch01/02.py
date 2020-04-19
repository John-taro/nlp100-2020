"""
02. 「パトカー」＋「タクシー」＝「パタトクカシー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""
str1 = "パトカー"
str2 = "タクシー"
answer = []

for i in range(0,len(str1)):
    answer.append(str1[i]+str2[i])

answer = "".join(answer)
print(answer)
