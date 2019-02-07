import re

def clean_html(sentence):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', sentence)
    return cleantext

def clean_punc(word):
    cleaned = re.sub(r'[?|!|\'|#]', r'', word)
    cleaned = re.sub(r'[.|,|)|(|\|/]', r' ', cleaned)
    return cleaned

def clean(text_file):
    with open(text_file, encoding='utf8', errors='ignore') as f:
        text = f.read()
        text = clean_html(text)
        #text = clean_punc(text) # if you want to remove punctuation use this line
    with open("cleaned_" + text_file, "w") as c:
        c.write(text)

clean("atlantic.txt")
