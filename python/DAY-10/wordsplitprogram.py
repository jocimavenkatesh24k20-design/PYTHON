with open("day-10/file.txt", "r") as f:
    words = f.read()
    words = words.split()
    for word in words:
        print(word)
        