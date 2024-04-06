#credits: https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/
#         https://www.tutorialspoint.com/How-do-I-wrap-a-string-in-a-file-in-Python#:~:text=To%20wrap%20a%20string%20in,the%20string%20to%20the%20file.
#         https://www.tutorialspoint.com/extract-hyperlinks-from-pdf-in-python#:~:text=To%20extract%20the%20hyperlinks%20from%20the%20PDF%20we%20generally%20use,print%20it%20on%20the%20screen.

# importing required modules 
import txt_parser
import PyPDF2
from cleantext import clean



def read_pdf(pdf_path):
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
            #if there is a visible url, the parser will save it 
            for line in page_text.split('\n'):
                if line.strip():  # If line is not empty

                    text.append(txt_parser.remove_emoji(line.strip()))
                    # print(txt_parser.find_url(line.strip()))

    # Print the organization if you have the txt_parser module
    org = txt_parser.getOrg(text)  # Getting the organization
    print(org) 

    #calling on testing
    if True:
        testing_txt_file(pdf_path=pdf_path, text=text)
 
def testing_txt_file(pdf_path, text):
    # # TESTING PURPOSES
    #storing parsed text into a txt for vizualization >>>>>>>>
    name_index = pdf_path.rindex("/") + 1 #obtaining the naming convention for the file --- storage?
    file_name = pdf_path[name_index : -4]

    file = open(file_name, "w")

    # Write string to file
    txt = ""
    for l in text:
      txt += l
      txt += "\n"

    file.write(txt)
    # Close the file
    file.close()




def parsing_text(text_list):
    pass



