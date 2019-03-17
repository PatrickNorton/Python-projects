#!/usr/bin/env python3

import string


def encode(test_str):
    possible_chr = string.printable
    chr_num = len(possible_chr)
    encoded_str = ''
    last_chr = ''
    for letter in test_str:
        letter_index = possible_chr.index(letter)
        shift = possible_chr.index(last_chr) if last_chr else len(test_str)
        new_index = (letter_index + shift) % chr_num
        last_chr = letter
        encoded_ltr = possible_chr[new_index]
        encoded_str += encoded_ltr
    return encoded_str


def decode(test_str):
    possible_chr = string.printable
    chr_num = len(possible_chr)
    decoded_str = ''
    last_chr = ''
    for pos, letter in enumerate(test_str):
        letter_index = possible_chr.index(letter)
        shift = possible_chr.index(last_chr) if last_chr else len(test_str)
        new_index = (letter_index - shift) % chr_num
        last_chr = letter
        encoded_ltr = possible_chr[new_index]
        decoded_str += encoded_ltr
    return decoded_str


if __name__ == "__main__":
    import sys
    import re
    code_dict = {'e': encode, 'd': decode}
    verbose_dict = {"--encode": "-e", "--decode": "-d"}
    options = {x if x[1] != '-' else verbose_dict[x]
               for x in sys.argv if re.match(r"^--?[a-zA-Z]+$", x)}
    options = ''.join(options)
    options = options.replace("-", "")
    raw_output = 'r' in options
    try:
        current_state = re.search(r"d|e", options)[0]
        function = code_dict[current_state]
    except (IndexError, KeyError, TypeError):
        current_state = "-"
        while current_state not in "de":
            print("Choose whether to decode or encode.")
            current_state = input("Enter a mode (d/e) ")
    if '--file' in sys.argv or '-f' in sys.argv:
        test_strs = []
        file_names = (sys.argv[x+1] for x, y in enumerate(sys.argv)
                      if y in ('--file', '-f'))
        try:
            for x in file_names:
                with open(x) as f:
                    test_strs.append(f.read())
        except FileNotFoundError:
            print(f"File '{x}' not found")
            sys.exit(1)
        for test_str in test_strs:
            coded_text = function(test_str)
            print(coded_text if raw_output else repr(coded_text)[1:-1])
        sys.exit()
    print("Interactive code evaluator")
    while True:
        to_code = input(f"{current_state}> ")
        if to_code == "quit":
            sys.exit()
        elif to_code in ("encode", "decode"):
            current_state = to_code[0]
            function = code_dict[current_state]
            print(f"Switching to {to_code} mode")
            continue
        if '\\' in to_code:
            replacement_dict = {
                r"\n": "\n",
                r"\t": "\t",
                r"\r": "\r",
                r"\x0b": "\x0b",
                r"\x0c": "\x0c",
            }
            for key, val in replacement_dict.items():
                to_code = to_code.replace(key, val)
            to_code = re.sub(r"(?<!\\)\\(\\*)(?=\1)", "", to_code)
        from_code = function(to_code)
        print(from_code if raw_output else repr(from_code)[1:-1])
