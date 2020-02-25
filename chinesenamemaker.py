import random

if __name__ == "__main__":
    f = open("data.txt", "r")
    dict = []
    for i in f:
        i = i.replace("\n", "")
        if i not in dict:
            dict.append(i)
    f.close()
    print(dict)
    while True:
        print("".join(random.sample(dict, random.randint(2, 4))))
        input()
    pass
