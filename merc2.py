def sentence(strings):
    return{string:strings.count(string) for string in strings}
strings=["anne","alice","alice","kellen","anne"]
print(sentence(strings))
