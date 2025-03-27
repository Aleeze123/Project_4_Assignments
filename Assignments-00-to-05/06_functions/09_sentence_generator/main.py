from termcolor import colored

def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print(colored(f"I am excited to add this {word} to my vast collection of them!", "cyan"))
    elif part_of_speech == 1:
        print(colored(f"It's so nice outside today it makes me want to {word}!", "magenta"))
    elif part_of_speech == 2:
        print(colored(f"Looking out my window, the sky is big and {word}!", "green"))
    else:
        print(colored("Part of speech must be 0, 1, or 2! Can't make a sentence.", "red"))
def main():
    word = input(colored("Please type a noun, verb, or adjective: ", "yellow"))
    print(colored("Is this a noun, verb, or adjective?", "yellow"))
    part_of_speech = int(input(colored("Type 0 for noun, 1 for verb, 2 for adjective: ", "yellow")))
    make_sentence(word, part_of_speech)
if __name__ == '__main__':
    main()
