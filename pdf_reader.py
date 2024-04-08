#credits: https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/
#         https://www.tutorialspoint.com/How-do-I-wrap-a-string-in-a-file-in-Python#:~:text=To%20wrap%20a%20string%20in,the%20string%20to%20the%20file.
#         https://www.tutorialspoint.com/extract-hyperlinks-from-pdf-in-python#:~:text=To%20extract%20the%20hyperlinks%20from%20the%20PDF%20we%20generally%20use,print%20it%20on%20the%20screen.

# importing required modules 
import txt_parser
import PyPDF2
from cleantext import clean
import pandas as pd
import numpy as np

#Categories
WICC =["W1", "W2", "W3","W4","W5","W6","W7","W8","W9","W10","W11", "W12", "W13","W14","W15","W16","W17","W18","W19","W20",]
WICC_CORN =["C1", "C2", "C3","C4","C5","C6","C7","C8","C9","C10","C11", "C12", "C13","C14","C15","C16","C17","C18","C19","C20"]
WICC_OPPS =["O1", "O2", "O3","O4","O5","O6","O7","O8","O9","O10","O11", "O12", "O13","O14","O15","O16","O17","O18","O19","O20"]
WICC_collective = []
WICC_collective.append(WICC)
WICC_collective.append(WICC_CORN)
WICC_collective.append(WICC_OPPS)



def read_pdf(pdf_path):
    """
    Method which reads a pdf input to scrape out information and returns a Pandas 
    dataframe object containing all scraped opportunities from the email

    pdf_path : string representing the path of downloaded email file 
    
    """
    # Creating a PDF reader object
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Printing number of pages in PDF file
        # print("LENGTH:")
        print(len(reader.pages))
        # print("STARING ...")

        segments = []
        links = []

        
        # Iterate through each page to add a non-empty line
        for i in range(len(reader.pages)):    
            # print("PAGE NUMBER :", i)
            # Getting a specific page from the PDF file

            page = reader.pages[i]

            # Extracting text from page
            page_text = page.extract_text()
            pagetext = page_text

            if(i==0):
                p1_list = pagetext.split("\n")

                org, subj = txt_parser.get_org_and_sub(p1_list)
                # topper = p1_list[2]
                # topper_start = topper[:5]
                # topper_end = topper[]

                # print("ORG: ", org)
                # print("SUBJ: ", subj)
                print(p1_list)

            # page_parsed = np.array([])

            for c in range(len(WICC_collective)):
                if(i==0 or len(pagetext)==0):   #skipping the content page or when nothing else in the page to copy over
                    break

                cat = WICC_collective[c]
                for item_index in range(len(cat)): #searching for relevant categories 

                    # print("ITEM :", cat[item_index])
                    # print("PAGE CONTENTS :", pagetext)

                    if(pagetext.find(cat[item_index]) >= 0): # the opportunity is found 
                        
                        loc = pagetext.find(cat[item_index])
                        if(loc>0):
                            # print("CASE 1 ")
                            # the opportunity starts in the middle hence we remove the start and append to the previous cell
                            if(len(segments) > 0 ):
                                # print("SECTION 1")
                                #previous opportunities exist!
                                prev_info = pagetext[:loc]
                                prev_seg = segments[-1]
                                prev_seg_mod = prev_seg + " "+prev_info
                                segments[-1] = prev_seg_mod
                                pagetext = pagetext[loc:]

                            else:
                                # print("SECTION 2")
                                #the opportunity is a first for segments but the opportunity starts from the middle of the document 
                                pagetext = pagetext[loc:]

                        #the opportunity header at the start now 

                        #we can determine the end point of the opportunity if we are able to identify the start of the next header 
                        normal_cases = ( item_index +1 < len(cat) and pagetext.find(cat[item_index+1])> 0 ) or \
                        ( item_index +1 == len(cat) and c+1 < len(WICC_collective) and pagetext.find(WICC_collective[c+1][item_index+1]) )

                        if(normal_cases): #endpoint determinable 
                            # print("CASE 2")

                            #last possible item
                            if ( (item_index +1) < len(cat) and (pagetext.find(cat[item_index+1]) > 0 )):
                                # print("SECTION 1")
                                end_loc = pagetext.find(cat[item_index+1])
                                # print("the next item is: ",cat[item_index+1] )
                                # print("the end loc is :", end_loc)

                            elif ( item_index +1 == len(cat) and c+1 < len(WICC_collective) and pagetext.find(WICC_collective[c+1][item_index+1]) ):
                                # print("SECTION 2")
                                end_loc = pagetext.find(WICC_collective[c+1][item_index+1])

                            new_info = pagetext[:end_loc]
                            pagetext = pagetext[end_loc:] # updating the rest of page text to read 
                            # print("left over page text :", pagetext)

                            # print("CASE 2 INFO: ", new_info, " PAGE # :", i)
                            segments.append(new_info)

                        else: #endpoint does not exist in this page 
                            # print("CASE 3")
                            new_info = pagetext[:]
                            segments.append(new_info) #add everything remaining on this page into segments 


            testing_txt_file2("trial1", segments)
            # print("DONE")
            
        
    df = pd.DataFrame(segments)
    link_df = pd.DataFrame(links)
    df = pd.concat([df,link_df], axis=1)
    # # Print the organization if you have the txt_parser module
    # org = txt_parser.getOrg(text)  # Getting the organization
    # print(org) 
    return df, org, subj #, org 

    # #calling on testing
    # if True:
    #     testing_txt_file(pdf_path=pdf_path, text=text)
 
def testing_txt_file(pdf_path, text):
    """
    Method which returns a txt file of information scraped from an inputted pdf.

    This method is used for testing purposes: to vizualize the scrapped data.

    pdf_path: string representing the path of pdf inputted, used to name the txt tile 
    text: scraped data from the inputted pdf
    """
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

def testing_txt_file2(name, text):
    """
    Method which returns a txt file of information scraped

    This method is used for testing purposes: to vizualize the scrapped data.

    name: a string used to name the txt tile 
    text: scraped data which is to be vizualized 
    """
    # # TESTING PURPOSES
    #storing parsed text into a txt for vizualization >>>>>>>>
    file_name = name
    file = open(file_name, "w")

    # Write string to file
    txt = ""
    for l in text:
      txt += l
      txt += "\n"

    file.write(txt)
    # Close the file
    file.close()


def parsing_links(page_text, links):
    """
    Method returning a modified list of links obtained from text of a page 

    page_text: string representing text scrapped from a page of a pdf file 
    links: the list to which the links are to be appended to 
    """
    # Parsing through each page of text
    #if there is a visible url, the parser will save it 
    for line in page_text.split('\n'):
        if line.strip():  # If line is not empty
            link = txt_parser.find_url(line.strip())
            if(len(link) > 0):
                links.append(link)
            else:
                links.append("")
    
    return links




