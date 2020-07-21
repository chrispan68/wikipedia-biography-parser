from wiki_xml_handler import *
import xml.sax
import sys
import subprocess

data_path = sys.argv[1]
output = sys.argv[2]

# Object for handling xml
handler = WikiXmlHandler()
# Parsing object
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
# Iteratively process file
with open(output, 'w') as f:
    for line in subprocess.Popen(['bzcat'], 
                                stdin = open(data_path), 
                                stdout = subprocess.PIPE).stdout:
        begin = len(handler._people)
        try:
            parser.feed(line)
        except StopIteration:
            break

        if len(handler._people) > begin:
            print(handler._people[-1][0] + ": " + handler._people[-1][1]["Born"])
            f.write(handler._people[-1][0] + ":\n")
            f.write(handler._people[-1][2] +"\n")



    