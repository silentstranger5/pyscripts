import argparse, json, requests, sys

def translate(q, source, target):
    payload = dict([
        ("q", q),
        ("source", source),
        ("target", target)
    ])
    r = requests.post("https://trans.zillyhuhn.com/translate", data=payload)
    if r.status_code != 200:
        exit("Bad source/target code")
    return r.json().get("translatedText")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Translate",
        description="Translate text to another language")
    parser.add_argument("file", nargs="?",
        help="source text filename (optional)")
    parser.add_argument("-s", "--source", default="en",
	help="source language in two-letter format (i.e. `en`)")
    parser.add_argument("-t", "--target", default="es",
        help="target language in two-letter format (i.e. `es`)")
    parser.epilog = "If no source file specified, program accepts\
        source text from input, terminated with EOF"
    args = parser.parse_args()
    if args.file:
        try:
            f = open(args.file, "r")
        except OSError:
            exit("Invalid file")
        else:
            text = f.read().decode("utf-8")
            f.close()
    else:
        text = ""
        while True:
            try:
                text += input() + "\n"
            except EOFError:
                break
    
    translated = translate(text, args.source, args.target)
    print(translated)