from lxml import etree


if __name__ == '__main__':
	schema = etree.parse('./secl.002.001.03.xsd')
	elements = schema.xpath("//xs:simpleType",
                            namespaces={"xs": "http://www.w3.org/2001/XMLSchema"},
                        )
	children = elements[0].getchildren()

	print(elements[0].keys())
	print(elements[0].get('name'))
	for child in children:
		print(child.tag)