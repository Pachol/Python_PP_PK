from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("C:\Users\Przemek\PycharmProjects\Python\Python2\cd_catalog.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element : %s" % collection.getAttribute("shelf"))
# Get all cd's
cds = collection.getElementsByTagName("CD")
# Print detail of each movie.
for cd in cds:
        title = cd.getElementsByTagName('TITLE')[0]
        print("TITLE: %s" % title.childNodes[0].data)
        artist = cd.getElementsByTagName('ARTIST')[0]
        print("ARTIST: %s" % artist.childNodes[0].data)
        country = cd.getElementsByTagName('COUNTRY')[0]
        print("COUNTRY: %s" % country.childNodes[0].data)
        company = cd.getElementsByTagName('COMPANY')[0]
        print("COMPANY: %s" % company.childNodes[0].data)
        year = cd.getElementsByTagName('YEAR')[0]
        print("YEAR: %s" % year.childNodes[0].data)
DOMTree.getElementsByTagName('TITLE')[0].firstChild.replaceWholeText("music")

