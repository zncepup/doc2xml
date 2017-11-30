import xml.dom.minidom as Dom


class XMLGenerator:
    def __init__(self, xml_name):
        self.doc = Dom.Document()
        self.xml_name = xml_name

    def createNode(self, node_name):
        return self.doc.createElement(node_name)

    def addNode(self, node, prev_node=None):
        cur_node = node
        if prev_node is not None:
            prev_node.appendChild(cur_node)
        else:
            self.doc.appendChild(cur_node)
        return cur_node

    def setNodeAttr(self, node, att_name, value):
        cur_node = node
        cur_node.setAttribute(att_name, value)

    def setNodeValue(self, cur_node, value):
        node_data = self.doc.createTextNode(value)
        cur_node.appendChild(node_data)

    def genXml(self):
        f = open('new/'+self.xml_name, "wb")
        f.write(self.doc.toprettyxml(indent="\t", newl="\n", encoding="utf-8"))
        f.close()


if __name__ == "__main__":
    myXMLGenerator = XMLGenerator("book_store.xml")

    # xml root node
    node_book_store = myXMLGenerator.createNode("book_store")
    myXMLGenerator.setNodeAttr(node_book_store, "name", "new hua")
    myXMLGenerator.setNodeAttr(node_book_store, "website", "http://www.ourunix.org")
    myXMLGenerator.addNode(node=node_book_store)

    # book01
    node_book_01 = myXMLGenerator.createNode("book")

    node_book_01_name = myXMLGenerator.createNode("name")

    myXMLGenerator.addNode(node_book_01_name, node_book_01)

    myXMLGenerator.setNodeValue(node_book_01_name, "Hamlet")

    node_book_01_author = myXMLGenerator.createNode("author")
    myXMLGenerator.setNodeValue(node_book_01_author, "William Shakespeare")
    myXMLGenerator.addNode(node_book_01_author, node_book_01)

    node_book_01_price = myXMLGenerator.createNode("price")
    myXMLGenerator.setNodeValue(node_book_01_price, "$20")
    myXMLGenerator.addNode(node_book_01_price, node_book_01)

    node_book_01_grade = myXMLGenerator.createNode("grade")
    myXMLGenerator.setNodeValue(node_book_01_grade, "good")
    myXMLGenerator.addNode(node_book_01_grade, node_book_01)

    myXMLGenerator.addNode(node_book_01, node_book_store)

    # gen
    myXMLGenerator.genXml()