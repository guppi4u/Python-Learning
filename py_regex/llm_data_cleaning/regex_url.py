
# removing text between url 

import re
def remove_text_url():
    sample_txt = "Visit our website at https://www.example.com or http://sub.domain.org."

    pattern = r"https?://\S+" # Matches http or https, followed by non-whitespace

    match =re.sub(pattern,"",sample_txt)


    print(f'Clean text : {match}')



remove_text_url()