
def getOrg(lines):
  '''
  Function which reads list of strings and returns the organization the email came from

  Input:
  path: path of type string of the desired txt file 

  '''
  header = lines[0]

  index = header.find("[") +1
  b = header[index:]
  b = b[: b.find("]")] 

  return b

# def text_type_allocation(path):

