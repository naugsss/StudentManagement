import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def validate_email(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def validate_uid(uid):

    regex_number = '[0-9]+'
    if re.fullmatch(regex_number, uid):
        return True
    return False


def validate_mobile_number(mobile_number):
    pattern = re.compile(r'^\d{10}$')
    return bool(pattern.match(mobile_number))