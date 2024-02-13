import re


def convert_persian_for_db(text):
    """Function To Convert Default input text to text acceptable by amoozeshyar's Data Base"""

    mapping = {
        '۰': '0',
        '۱': '1',
        '۲': '2',
        '۳': '3',
        '۴': '4',
        '۵': '5',
        '۶': '6',
        '۷': '7',
        '۸': '8',
        '۹': '9',
        '.': '.',
    }
    
    # Handle Persian Numbers (Converted to english numbers)
    pattern = "|".join(map(re.escape, mapping.keys()))
    text =  re.sub(pattern, lambda m: mapping[m.group()], str(text))

    # Handle ک and ی and space, add % to beginning and end of string 
    rep = {"ی": "%", "ک": "%", " ": "%"} # define desired replacements here
    rep = dict((re.escape(k), v) for k, v in rep.items()) 
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    text = "%" + text + "%"

    return text


    