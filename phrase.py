import random

def get_random_phrase(filename='phrases.txt'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            phrases = [line.strip() for line in file if line.strip()]
        return random.choice(phrases) if phrases else "No phrases found!"
    except FileNotFoundError:
        return "phrases.txt file not found!"

if __name__ == "__main__":
    print(get_random_phrase())