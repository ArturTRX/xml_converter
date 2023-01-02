"""
Utility functions for XML manipulation in Django.

These functions provide tools for parsing and modifying XML files in Django
    views, forms, and models.
"""

import xml.etree.ElementTree as ET
from typing import Union, Dict


def parse_xml(xml_file: bytes) -> Union[ET.Element, None]:
    """
    :xml_file: The XML file to be parsed, as a bytes object.


    Returns:
        ET.Element: The root element of the parsed XML file.
            Returns None if the XML file could not be parsed.
    """
    try:
        tree = ET.parse(xml_file)
    except ET.ParseError:
        return None
    return tree.getroot()


# Convert the XML file to a Python dictionary
def xml_to_dict(node: ET.Element) -> Dict:
    """
    Convert an XML element to a Python dictionary.

    :node: The XML element to be converted.
    :root: The root element of the XML tree.

    Returns:
        dict: A Python dictionary representing the XML element.
    """
    data = {}
    if len(node) == 0:
        # Leaf node
        data[node.tag] = node.text if node.text else ''

    else:
        # Non-leaf node
        data[node.tag] = []
        for child in node:
            data[node.tag].append(xml_to_dict(child))
    return data
