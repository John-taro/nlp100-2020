"""
03. 円周率
“Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
text = text.replace(',', '').replace('.', '')
text = text.split()

answer = []

for i in range(len(text)):
    answer.append(len(text[i]))

print(answer)
