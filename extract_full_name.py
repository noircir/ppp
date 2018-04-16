names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

def extract_full_name(l):
    return list(map(lambda x: "{} {}".format(x['first'], x['last']), l))


print(extract_full_name(names))