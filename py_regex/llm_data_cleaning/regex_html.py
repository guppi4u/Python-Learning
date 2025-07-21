
# Creating regex for removing tags in html files 

import re

def remove_html_tag():

    sample_txt ="<p>This is some <b>HTML</b> content.</p>"

    pattern = r"<.*?>" # Remove anything between < and > non-greedily

    match =re.sub(pattern,"",sample_txt)

    print(f'Clean text :{match}')


#function call 

remove_html_tag()
