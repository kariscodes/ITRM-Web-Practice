# 리스트 테스트

# 문장을 단어로 분할하여 리스트로 넣자.
sentence = "Don't beat around the bush."    # 주위만 맴돌지마
pieces = sentence.split()
print(pieces)

# 문장 첫 단어 Hint
word1 = pieces[0]
print("The First Word: ", word1)

# 문장 두번째 단어까지 Hint
word2 = pieces[:2]
print("The First and Second Words: ", word2)

# 리스트 복사
# slices = pieces[:];     print(slices)
slices = pieces.copy(); print(slices)
# slices = list(pieces);  print(slices)

# 리스트 내용을 뒤섞기
# import random
# random.shuffle(slices)
# print(slices)
# for i in slices:
#     print(i)


class wordTile:
    def __init__(self, number, string):
        self.__order = number
        self.__word = string
    def order(self):
        return self.__order
    def word(self):
        return self.__word

# tile = wordTile(1, "test")
# print(tile.order(), tile.word())

# 단어수만큼 word tile 클래스로 된 리스트 만들기 + 리스트 내용을 뒤섞기
import random
tileList = []
for index, value in enumerate(slices):
    print(index, value)
    tileList.append(wordTile(index, value))
random.shuffle(tileList)
# word tile 클래스의 내용 출력하기
for t in tileList:
    print(t.order(), t.word())


# from tkinter import *
# root = Tk()
# lbl = Label(root, text="이름")
# lbl.pack()
# txt = Entry(root)
# txt.pack()
# btn = Button(root, text="OK")
# btn.pack()
# root.mainloop()


from tkinter import *
root = Tk()
for w in tileList:
    lbl = Label(root, text=w.word())
    lbl.pack()
root.mainloop()

