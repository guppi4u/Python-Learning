
# meta char "+" matches one or more char in set []

import re 

def meta_char_plus():
    sample =  "The price is $12.50 or €10."

    match = re.search("[0-9]+",sample)

    match2 = re.search("[0-9.]+",sample)

    print(match)

    print("*********************")

    print(match2)



meta_char_plus()
