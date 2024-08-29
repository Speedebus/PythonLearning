message = input(">")
def translator(list):
    output = ""
    words = list.split(" ")
    translate = {
        ':)':"😀",
        ':(':"😢"
    }
    for word in words:
        output += translate.get(word, word) + " "
    return (output)

print(translator(message))