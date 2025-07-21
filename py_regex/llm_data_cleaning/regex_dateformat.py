
#Standardizing Data Formats

#  Dates (e.g., converting MM/DD/YYYY to YYYY-MM-DD): This often requires re.sub with capturing groups.


import re

class RegexUtil:

    @staticmethod # Decorator to define a static method
    def date_conversion(): 

        sample_text = "Today's date is 07/17/2025."
        # Capture Month, Day, Year
        # Capture Month, Day, Year using capturing groups
        # \1 refers to the content of the first group (Month)
        # \2 refers to the content of the second group (Day)
        # \3 refers to the content of the third group (Year)
        cleaned_date = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\1-\2",sample_text)
        # print(cleaned_date) -this will return None 
        return cleaned_date
    

# calling method inside class
ru1=RegexUtil.date_conversion()

print(f'Static Function calling from class :{ru1}')
