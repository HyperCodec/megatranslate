import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import argparse, random, packages, sys
from megatranslate import megatranslate
from argostranslate import translate

def cli():
    parser = argparse.ArgumentParser(
        prog="megatranslate",
        description="Translates text a bunch of times, leading to potential disfigurement or loss of original meaning."
    )

    parser.add_argument("-t", "--text", required=False, help="The text to megatranslate.")
    parser.add_argument("-p", "--text-path", required=False, help="The path to a file containing the text to megatranslate.")
    parser.add_argument("-c", "--count", default=5, help="The number of times to translate the text")
    parser.add_argument("-s", "--seed", required=False, help="A specific seed to use for generation.")
    parser.add_argument("-n", "--no-pkg-install", action="store_true", help="Skip the translation package installation step")
    parser.add_argument("-r", "--root-lang", default="en", help="The language of the provided text")
    parser.add_argument("-u", "--update-existing-pkgs", action="store_true", help="Update existing installed translation packages")
    parser.add_argument("-o", "--output-path", required=False, help="An optional path to write the translated text to. Will not print to console if provided.")

    return parser.parse_args()

def main():
    args = cli()

    text = args.text

    if text is None:
        if args.text_path is None:
            print("Either --text or --text-path must be set. Check --help.")
            sys.exit(1)
        
        with open(args.text_path, "r") as f:
            text = f.read()

    if args.seed is not None:
        random.seed(int(args.seed))

    if args.update_existing_pkgs:
        packages.update_packages()

    if not args.no_pkg_install:
        packages.install_packages()

    langs = translate.get_installed_languages()

    print("Megatranslating")
    output = megatranslate(text, args.root_lang, int(args.count), langs)

    if args.output_path is not None:
        with open(args.output_path, "w+") as f:
            f.write(output)
        print("Output written to:", args.output_path)
        return
    print("Translated text:", output)

if __name__ == "__main__":
    main()