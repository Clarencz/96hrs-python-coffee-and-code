# import xml.sax


# class GroupHandler(xml.sax.ContentHandler):
#     def startElement(self, name, attrs):
#         self.current = name
#         if self.current == "person":
#             print(".....PERSON....")
#             print("id {}".format(attrs['id']))
#     def Characters(self,content):
#         if self.current == "name":
#             self.name = content
#         elif self.current == "age":
#             self.age = content
#         elif self.current == "weight":
#             self.weight = content
#         elif self.current == "height":
#             self.height = content
#     def endElement(self, name):
#         if self.current == "name":
#             print("name {}".format(self.name))
#         if self.current == "age":
#             print("age {}".format(self.age))
#         if self.current == "weight":
#             print("weight {}".format(self.weight))
#         if self.current == "weight":
#             print("height {}".format(self.height))
#         self.current == ""
# handler = GroupHandler()
# parser = xml.sax.make_parser()
# parser.setContentHandler(handler)
# parser.parse('data.xml')


import xml.dom.minidom

domtree = xml.dom.minidom.parse('data.xml')
group = domtree.documentElement

persons = group.getElementsByTagName("person")

for person in persons:
    print("......person.......")
    if person.hasAttribute('id'):
        print("id {}".format(person.getAttribute('id')))
    print("name {}".format(person.getElementsByTagName('name')[0].childNodes[0].data))
    print("age {}".format(person.getElementsByTagName('age')[0].childNodes[0].data))
    print("weight {}".format(person.getElementsByTagName('weight')[0].childNodes[0].data))
    print("height {}".format(person.getElementsByTagName('height')[0].childNodes[0].data))
    
    
# person[2].getElementsByTagName('name')[0].childNodes[0].nodeValue ="new value"
# persons[0].setAttribute('id', '100')
# persons[3].getElementsByTagName('name')[0].childNodes[0].nodeValue = "-10"
# domtree.writexml("data.xml","w")

newperson = domtree.createElement("person")
newperson.setAttribute("id","6")

name = domtree.createElement("name")
name.appendChild(domtree.createTextNode("paul green"))

age = domtree.createElement("age")
age.appendChild(domtree.createTextNode("22"))

weight = domtree.createElement("weight")
weight.appendChild(domtree.createTextNode("80"))

height = domtree.createElement("height")
height.appendChild(domtree.createTextNode("178"))

newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

group.appendChild(newperson)

domtree.writexml(open("data.xml","w"))