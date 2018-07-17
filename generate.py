import random


def random_name(male=True):
    length = random.randint(2, 3)
    
    if male:
        first = ['ke', 'ara', 'te', 'ta', 'ma', 'ho', 'lu', 'bun', 'kai', 'ic', 'de', 'zan']
        middle = ['yo', 'ke', 'ka', 'ku', 'to', 'mo', 'ma', 'mu', 'chin', 'saio', 'sio']
        last = ['sai', 'ke', 'ma', 'ra', 'shi', 'nu', 'jun', 'kapi', 'kai', 'dar', 'wai', 'shi']
    else:
        first = ['ma', 'na', 'ir', 'ka', 'je', 'te', 'an', 'ja']
        middle = ['co', 'ru', 'su', 'hi', 'an']
        last = ['ra', 'ya', 'lan', 'ma', 'lia', 'ai', 'ni', 'shi']

    name = ''
    if length == 2:
        name = random.choice(first) + random.choice(last)
    if length == 3:
        name = random.choice(first) + random.choice(middle) + random.choice(last)
    return name.capitalize()

def house_name():
    length = random.randint(2, 3)

    first = ['a', 'min', 'xu', 'ana', 'lu', 'ke', 'tsu', 'du', 'xa', 'ko', 'cho', 'io', 'shon', 'ton', 'shin', 'tus', 'tu', 'ek', 'da', 'in']
    middle = ['co', 'wa', 'ra', 'sa', 'le', 'sta', 'cat', 'cha', 'ca', 'na', 'sho', 'mar', 'za', 'cal', 'am', 'chin', 'rod']
    last = ['ma', 'nabi', 'tes', 'ti', 'jun', 'wan', 'ni', 'ri', 'ecas', 'tai', 'pan', 'da', 'la', 'mi', 'gu', 'wai', 'ora', 'chi', 'do', 'aka']

    name = ''
    if length == 2:
        name = random.choice(first) + random.choice(last)
    if length == 3:
        name = random.choice(first) + random.choice(middle) + random.choice(last)
    return name.capitalize()



if __name__ == "__main__":
    for x in range(10):
        male = random.randint(0, 10) <= 8

        prefix = 'Lady '
        if male:
            prefix = 'Lord '

        print prefix + random_name(male=male) + ' of the ' + house_name()