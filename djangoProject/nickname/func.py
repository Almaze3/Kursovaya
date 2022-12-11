import re


def nickname(mail):
    exr = r'(\S*)@'
    d = {}
    matches = re.findall(exr, mail)
    for i in range(len(matches)):
        d[i] = matches
    return matches
#py manage.py runserver