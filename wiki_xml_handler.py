import xml.sax
import mwparserfromhell

class WikiXmlHandler(xml.sax.handler.ContentHandler):
    """Content handler for Wiki XML data using SAX"""
    def __init__(self):
        xml.sax.handler.ContentHandler.__init__(self)
        self._buffer = None
        self._values = {}
        self._current_tag = None
        self._people = []

    def process_article(self, title, text, template = 'Infobox person'):
        """Process a wikipedia article looking for template"""
        
        # Create a parsing object
        wikicode = mwparserfromhell.parse(text)
        
        # Search through templates for the template
        matches = wikicode.filter_templates(matches = template)
        
        properties = {}
        if len(matches) >= 1:
            if len(matches) >= 2):
                print('JFIAOIJEIOSEFJOAJSEIFJAOSEJFOIASJEFIJASEOIFOASIEFJOIASEJFIASJEFOAJSEFEASOJAFASEJFAS')
            # Extract information from infobox
            for match in matches:
                properties += {param.name.strip_code().strip(): param.value.strip_code().strip() 
                            for param in match.params
                            if param.value.strip_code().strip()}
            
            raw_text = wikicode.strip_code().strip()
            return (title, properties, raw_text)

    def characters(self, content):
        """Characters between opening and closing tags"""
        if self._current_tag:
            self._buffer.append(content)

    def startElement(self, name, attrs):
        """Opening tag of element"""
        if name in ('title', 'text'):
            self._current_tag = name
            self._buffer = []

    def endElement(self, name):
        """Closing tag of element"""
        if name == self._current_tag:
            self._values[name] = ' '.join(self._buffer)

        if name == 'page':
            person = self.process_article(**self._values, 
                               template = 'Infobox person')
            # If article is a book append to the list of books
            if person:
                self._people.append(person)

    