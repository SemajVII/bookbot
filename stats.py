def get_book_txt(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    word_list = text.split()
    word_count = 0
    for words in word_list:
        word_count += 1
    return word_count

def character_count(text):
    character_dic = {}
    for letter in text:
        lower = letter.lower()
        if lower in character_dic:
             character_dic[lower] += 1
        else:
            character_dic[lower] = 1
    return character_dic

def new_dic(character_dic):
    new_chr_dic = []
    for key in character_dic:
        new_chr_dic.append({"char": key, "num": character_dic[key]})
    return new_chr_dic
def sort_on(characters):
    return characters["num"]
