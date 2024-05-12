import re

def get_org_and_sub(lines):
  '''
  Function which reads list of strings and returns the organization the email came from

  Input:
  path: path of type string of the desired txt file 
  '''
  header = lines[0]

  index = header.find("[") +1
  b = header[index:]
  b = b[: b.find("]")] 

  sub = lines[1]

  return b, sub

def get_cat(info):
  '''
  Function retrieves the type of opportunity according to given classifications
  '''
  string = info[0]

  return string


def find_url(string):
    """
    Method returning links (concatenated by commas) obtained from an input 

    string: the string from which the links are to be extracted from 
    """
    # Find all the Strings that match the pattern
    regex = r"(https?://\S+)"
    urls = re.findall(regex, string)
    urls = ", ".join(urls)
    return urls

def remove_url(string):
    """
    Method removing all links from an string

    string: the string from which the links are to be removed from 
    """
    # Find all the Strings that match the pattern
    regex = r"(https?://\S+)"
    urls = re.findall(regex, string)
    for e in urls:
        string = string.replace(e,"")
    
    return string

def removeNonAscii(s): 
   """
   Method used to remove all non-ascii characters from a text 

   s: the string from which non-ascii characters are to be removed from 
   """
   #credit: https://stackoverflow.com/questions/20183669/remove-formatting-from-strings
   return "".join(i for i in s if ord(i)<126 and ord(i)>31)

def removeSubject(string, subj):
    """
    Method used to remove the subj from a string.

    If subj not in string, string is returned unchanged 

    string: the string from which subj is to be removed from 
    subj: the string which is to be removed if present
    
    """
    if(string.find(subj) > 0):
      string = string.replace(subj, "")
    return string




#credits: https://gist.github.com/slowkow/7a7f61f495e3dbb7e3d767f97bd7304b
def remove_emoji(string):
    """
    Method which returns a string after removing all emjoiis from it 

    Does not work on certain edge cases like the clock emoji 

    string: the string from which emjoiis are to be removed from 
    """
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)