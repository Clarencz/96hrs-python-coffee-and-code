import xml.sax


class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "person":
            print(".....PERSON....")
            print("id {}".format(attrs['id']))
    def Characters(self,content):
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content
    def endElement(self, name):
        if self.current == "name":
            print("name {}".format(self.name))
        if self.current == "age":
            print("age {}".format(self.age))
        if self.current == "weight":
            print("weight {}".format(self.weight))
        if self.current == "weight":
            print("height {}".format(self.height))
        self.current == ""
handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')