
# removal of Special Characters/Punctuation (keeping only alphanumeric):

import re

def keeping_only_alphanumeric():
    sample_txt = "Hello! How are you? @User #Tag $Amount"

    pattern =r"[^a-zA-Z0-9\s+]"

    clean_text =re.sub(pattern,"",sample_txt)

    print (f'Cleaned text :{clean_text}')


keeping_only_alphanumeric()