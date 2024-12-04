import random
from tqdm import tqdm

def get_lang_by_code(code, langs):
    return list(filter(lambda lang: lang.code == code, langs))[0]

def megatranslate(text, root_lang_code, count, langs):
    root_lang = get_lang_by_code(root_lang_code, langs)
    last_lang = root_lang

    for _ in tqdm(range(count)):
        next_lang = random.choice(langs)

        while next_lang == last_lang:
            next_lang = random.choice(langs)
        
        translation = last_lang.get_translation(next_lang)

        text = translation.translate(text)
        last_lang = next_lang

    # convert back to root language
    translation = last_lang.get_translation(root_lang)
    return translation.translate(text)