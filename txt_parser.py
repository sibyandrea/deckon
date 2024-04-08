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


def find_url(string):
    # Find all the Strings that match the pattern
    regex = r"(https?://\S+)"
    urls = re.findall(regex, string)
    urls = ", ".join(urls)
    return urls

def remove_url(string):
    # Find all the Strings that match the pattern
    regex = r"(https?://\S+)"
    urls = re.findall(regex, string)
    for e in urls:
        string = string.replace(e,"")
    
    return string

def removeNonAscii(s): 
   #credit: https://stackoverflow.com/questions/20183669/remove-formatting-from-strings
   return "".join(i for i in s if ord(i)<126 and ord(i)>31)

def removeSubject(string, subj):
    if(string.find(subj) > 0):
      string = string.replace(subj, "")
    return string




#credits: https://gist.github.com/slowkow/7a7f61f495e3dbb7e3d767f97bd7304b
def remove_emoji(string):
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