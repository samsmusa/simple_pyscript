import re

def my_function(*args, **kwargs):

    text = Element('test-input').element.value
    match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', str(text))

    unique = list(set(match))

    tee = ""
    for text in unique:
        tee = tee + "\n" + str(text.lower())
    


    Element('test-output').element.innerText = tee