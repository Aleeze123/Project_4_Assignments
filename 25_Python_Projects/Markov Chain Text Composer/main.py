import random
from termcolor import colored

def generate_markov_chain(text, n_gram=2):
    markov_chain = {}
    words = text.split()
    for i in range(len(words) - n_gram):
        gram = tuple(words[i:i + n_gram])
        next_word = words[i + n_gram]
        if gram not in markov_chain:
            markov_chain[gram] = []
        markov_chain[gram].append(next_word)
    return markov_chain

def generate_text(markov_chain, length=50, n_gram=2):
    start = random.choice(list(markov_chain.keys()))
    result = list(start)
    for _ in range(length - n_gram):
        state = tuple(result[-n_gram:])
        if state in markov_chain:
            next_word = random.choice(markov_chain[state])
            result.append(next_word)
        else:
            break
    return ' '.join(result)

def main():
    text = '''The day begins with a gentle breeze, and the soft light of dawn.
    Every step we take in life brings us closer to understanding the beauty of our world.
    It is in the quiet moments that we find clarity, and in the rush of life, we find purpose.
    The wisdom of nature teaches us patience, and the ever-changing sky reminds us of time's passage.
    May we always be mindful of the blessings we encounter, and may our hearts remain open to the wonders that surround us.'''

    markov_chain = generate_markov_chain(text, n_gram=2)
    generated_text = generate_text(markov_chain, length=50, n_gram=2)
    print(colored(generated_text, 'cyan'))

if __name__ == '__main__':
    main()
