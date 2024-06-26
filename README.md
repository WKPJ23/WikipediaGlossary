# WikipediaGlossary
Wikipedia API to pull article summary data into Excel based on title list to create custom open-source glossary.

The program contains 3 options:
{1} Pull article summary with paragraph breaks (i.e., everything before 'contents')
{2} Pull article summary as block of text (i.e., without paragrah breaks)
{3} Pull first sentence of article summary.

By creating a list in Excel in one column of terms you'd like to pull, you can then upload that list and have the API enter the data for you. There is a funciton to enter "No article found" if the term returns no exact hit.

There is also a dictionary and function to replace common American spellings with their Canadian/UK variants.
