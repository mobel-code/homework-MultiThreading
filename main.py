import threading
#1--

# def son(a):
#     return sum(int(i) for i in str(a))
#
# print(son(int(input())))

#2--
# names = ['ali', 'vali', 'hoshim', 'aziz']
# def full_name(names):
#     return [name.capitalize() for name in names]
#
# # names = str(input())
# print(full_name(names))

#3--

# score = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
#
# def scores(score):
#     return [a for a in score if a > 75]
#
# print(scores(score))

#4-

#5--
def soz(text):
    i = 0
    result = ""

    while i < len(text):
        if text[i] == 'e':
            result += '3'
        else:
            result += text[i]
        i += 1

    print(result)

text = input("tekst kiriting: ")
print(soz(text))

#6--

def soz(text):
    i = 0
    result = ""

    while i< len(text):
        if text[i] == " ":
            result += text[i]
        i += 1
    print(result)

text = input("tekst kiriting: ")
print(soz(text))

#7--

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)
t5 = threading.Thread(target=task5)
t6 = threading.Thread(target=task6)


t1.start()
t2.start()
t3.start()
t5.start()
t6.start()


t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()


