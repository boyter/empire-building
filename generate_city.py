import random
import pprint

def random_name(male='male'):
    length = random.randint(2, 3)
    
    if male == 'male':
        first = ['ke', 'ara', 'te', 'ta', 'ma', 'ho', 'lu', 'bun', 'kai', 'ic', 'de', 'zan']
        middle = ['yo', 'ke', 'ka', 'ku', 'to', 'mo', 'ma', 'mu', 'chin', 'saio', 'sio']
        last = ['sai', 'ke', 'ma', 'ra', 'shi', 'nu', 'jun', 'kapi', 'kai', 'dar', 'wai', 'shi']
    else:
        first = ['ma', 'na', 'ir', 'ka', 'je', 'te', 'an', 'ja', 'mu']
        middle = ['co', 'ru', 'su', 'hi', 'an']
        last = ['ra', 'ya', 'lan', 'ma', 'lia', 'ai', 'ni', 'shi']

    name = ''
    if length == 2:
        name = random.choice(first) + random.choice(last)
    if length == 3:
        name = random.choice(first) + random.choice(middle) + random.choice(last)
    return name.capitalize()


def generate_person():
    gender = random.choice(['male', 'female'])

    roll = random.randint(0, 100)
    if roll <= 50:
        age = random.randint(16, 50)
    if roll > 50 and roll <= 85:
        age = random.randint(40, 80)
    if roll > 85 and roll <= 100:
        age = random.randint(60, 110)

    return {
        'gender': gender,
        'name': random_name(male=gender),
        'age': age
    }

if __name__ == "__main__":
    for x in range(100):
        pprint.pprint(generate_person())