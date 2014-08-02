import xml.etree.ElementTree as ET


def get_attribs_of_builds_to_monitor(build_names, all_builds):
    global build_names_to_monitor
    build_names_to_monitor = build_names
    return filter(get_builds_to_monitor, all_builds)


def parse_xml_tree(file_name):
    return ET.parse(file_name)


def get_tree_root(tree):
    return tree.getroot()


def get_child_attributes(child):
    return child.attrib


def get_child_name(child):
    return child['name']


def get_builds_to_monitor(child):
    if (get_child_name(child) in build_names_to_monitor):
        return True
    else:
        return False


def read_build_names_from_xml(xml_file_name):
    return map(get_child_attributes, get_tree_root(parse_xml_tree(xml_file_name)))


def is_child_name_in_build_handles(child, build_handles):
    for build in build_handles:
        if (child['name'] == build['name']):
            return True
    else:
        return False


def read_selected_builds_from_xml(xml_file_name, build_handles):
    tree_root = get_tree_root(parse_xml_tree(xml_file_name))
    selected_handles = []
    for child in tree_root:
        if (is_child_name_in_build_handles(child.attrib, build_handles)):
            selected_handles.append(child.attrib)
    return selected_handles