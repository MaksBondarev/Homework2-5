# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def text_format(text):
    text = str(text)
    text_format = text.replace('а', '').replace('б', '').replace('в', '')
    return text_format

text2 = 'Я благоговел перед той маленькой героической птицей, перед любовным ее порывом.'
print(text_format(text2))



# text = 'Я благоговел перед той маленькой героической птицей, перед любовным ее порывом.'
# text_format = text.replace('а', '').replace('б', '').replace('в', '')
# print(text_format)