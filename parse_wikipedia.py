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
    begin = len(handler._people)
    try:
        parser.feed(line)
    except StopIteration:
        break

    if len(handler._people) > begin:
        print(handler._people[-1][0])


    