"""Convert text to Morse code and back."""

CHAR_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/',
}
MORSE_TO_CHAR = {v: k for k, v in CHAR_TO_MORSE.items()}


def text_to_morse(text):
    """Convert text to Morse code."""
    return ' '.join(CHAR_TO_MORSE.get(ch, '') for ch in text.upper())


def morse_to_text(morse):
    """Convert Morse code back to text."""
    return ''.join(MORSE_TO_CHAR.get(code, '?') for code in morse.split(' '))


if __name__ == "__main__":
    message = "Hello World"
    encoded = text_to_morse(message)
    decoded = morse_to_text(encoded)
    print(f"Text:    {message}")
    print(f"Morse:   {encoded}")
    print(f"Decoded: {decoded}")
