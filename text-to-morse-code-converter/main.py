def text_to_morse(text):
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.',

        ', ': '--..--', '.': '.-.-.-', '?': '..--..', ' ': '/', '-': '-....-', '(': '-.--.', ')': '-.--.-',
        '!': '-.-.--', '': ''
    }

    text = text.upper()
    morse_code = ''

    for char in text:
        if char not in morse_dict:
            morse_code += ' '
        else:
            morse_code += morse_dict[char] + ' '

    return morse_code


if __name__ == "__main__":
    while True:
        user_input = input("Input text: ")
        if user_input.lower() == "exit":
            break
        print(text_to_morse(user_input))
