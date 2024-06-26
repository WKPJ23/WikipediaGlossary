import pandas as pd
import wikipediaapi

#Initialise API with user agent
user_agent = "WikipediaFlash/2.1 (https://github.com/WKPJ23; will.power.jenkins@gmail.com)"
wikiAPI = wikipediaapi.Wikipedia(language="en", user_agent=user_agent)

#Correct for most common American spellings to Canadian/British
word_replace = {
    "behavior": "behaviour",
    "color": "colour",
    "United States": "U.S.",
    "modeling": "modelling",
    "license": "licence",
    "neighbor": "neighbour",
    "favorite": "favourite",
    "theater": "theatre",
}

#Function for replacing incorrect American spellings
def replace_words(text, word_replace):
    for target_word, replacement_word in word_replace.items():
        text = text.replace(target_word, replacement_word)
    return text

#Function to determine whether page exists or not & extract pre-contents
def get_intro(term):
    page = wikiAPI.page(term)
    if not page.exists():
        return "No article found"
    
    summary = page.summary
    
# OPTION 1 → Split summary into parapgraphs (if required)
    # paragraph = page.summary.split("\n")
    # intro_paragraphs = []
    # for paragraph in paragraph:
    #     #stop before 'contents' section
    #     if 'Contents' in paragraph:
    #         break
    #     if paragraph.strip(): #Ensure non-empy paragraphs
    #         intro_paragraphs.append(paragraph)
    
    # return "\n\n".join(intro_paragraphs)

# OPTION 2 → Find summary and extract pre-'Contents'
    # if "Contents" in summary:
    #     intro_text = summary.split("Contents")[0]
    # else:
    #     intro_text = summary
    # return intro_text.strip()

# OPTION 3 → For only the first sentence:
    first_sentence = summary.split(".")[0] + "."
    return first_sentence.strip()

#load, transform, and save xlsx
glossary = pd.read_excel("FILE.xlsx")

glossary['Definition Column'] = glossary['Title Column'].apply(get_intro)

# Replace words in the introductory text based on word_replacements dictionary
glossary['Term Column'] = glossary['Definition Column'].apply(lambda x: replace_words(x, word_replace))

glossary.to_excel("FILE.xlsx", index=False)