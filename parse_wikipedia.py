from wiki_xml_handler import *
import xml.sax
import sys
import subprocess

data_path = sys.argv[1]

# Object for handling xml
handler = WikiXmlHandler()
# Parsing object
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
# Iteratively process file
for line in subprocess.Popen(['bzcat'], 
                              stdin = open(data_path), 
                              stdout = subprocess.PIPE).stdout:
    parser.feed(line)
    
    # Stop when 3 articles have been found
    if len(handler._pages) > 5:
        for page in handler._pages:
            print(page[0] + page[1])
        break