# importing required modules 
import txt_parser


#credits: https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/
#         https://www.tutorialspoint.com/How-do-I-wrap-a-string-in-a-file-in-Python#:~:text=To%20wrap%20a%20string%20in,the%20string%20to%20the%20file.
#         https://www.tutorialspoint.com/extract-hyperlinks-from-pdf-in-python#:~:text=To%20extract%20the%20hyperlinks%20from%20the%20PDF%20we%20generally%20use,print%20it%20on%20the%20screen.
import re
import PyPDF2

def find_url(string):
    # Find all the Strings that match the pattern
    regex = r"(https?://\S+)"
    urls = re.findall(regex, string)
    return urls

# Path to the PDF file
pdf_path = '/Users/andreasiby/Documents/comms/deckon/dataset/WICC03312024.pdf'

# Creating a PDF reader object
with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    # Printing number of pages in PDF file
    print("LENGTH:")
    print(len(reader.pages))
    print("STARING ...")
    
    text = []
    
    # Iterate through each page to add a non-empty line
    for i in range(len(reader.pages)):
        # Getting a specific page from the PDF file
        page = reader.pages[i]
        
        # Extracting text from page
        page_text = page.extract_text()
        
        # Parsing through each page of text
        for line in page_text.split('\n'):
            if line.strip():  # If line is not empty
                text.append(line.strip())
                print(find_url(line.strip()))

org = txt_parser.getOrg(text)  # Getting the organization
print(org)  # Print the organization if you have the txt_parser module



#storing parsed text into a txt for vizualization >>>>>>>>
# name_index = path.rindex("/") + 1 #obtaining the naming convention for the file --- storage?
# file_name = path[name_index : -4]
 

# # TESTING PURPOSES
# file = open(file_name, "w")

# # Write string to file
# txt = ""
# for l in text:
#   txt += l
#   txt += "\n"

# file.write(txt)
# # Close the file
# file.close()

