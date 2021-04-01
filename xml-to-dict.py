# xml-to-dict

import xml.etree.ElementTree as ET
import json

file_name = 'ProcessGasReferenceData'
skip_attributes = []

tree = ET.parse(file_name + '.xml')

Dict1 = {}
for level1 in tree.getroot():
    if len(level1.attrib) > 1:
        if level1 not in skip_attributes:
            Dict1[level1.attrib['name']] = level1.attrib['value']
    else:
        Dict2 = {}
        for level2 in level1:
            if len(level2.attrib) > 1:
                if level2 not in skip_attributes:
                    Dict2[level2.attrib['name']] = level2.attrib['value']
            else:
                Dict3 = {}
                for level3 in level2:
                    if len(level3.attrib) > 1:
                        if level3.attrib['name'] not in skip_attributes:
                            Dict3[level3.attrib['name']] = level3.attrib['value']
                    else:
                        Dict4 = {}
                        for level4 in level3:
                            if level4.attrib['name'] not in skip_attributes:
                                Dict4[level4.attrib['name']] = level4.attrib['value']
                        Dict3[level3.attrib['name']] = Dict4
                Dict2[level2.attrib['name']] = Dict3
            Dict1[level1.attrib['name']] = Dict2

file = open(file_name + '.py', "w")
file.write(file_name + ' = ')
json.dump(Dict1, file, sort_keys=True, indent=4)
