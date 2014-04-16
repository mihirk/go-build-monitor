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


def read_file(filename):
    file_handle = open(filename, 'r')
    return file_handle.read()


def read_builds_to_monitor_from_config(build_config_file):
    read_config = read_file(build_config_file)
    return read_config.split('\n')


def get_builds_to_monitor(child):
    if (get_child_name(child) in build_names_to_monitor):
        return True
    else:
        return False


def read_build_names_from_xml(xml_file_name):
    return map(get_child_attributes, get_tree_root(parse_xml_tree(xml_file_name)))


def child_name_in_build_handles(child, build_handles):
    for build in build_handles:
        if(child['name'] == build['name']):
            return True
    else:
        return False


def read_selected_builds_from_xml(xml_file_name, build_handles):
    tree_root = get_tree_root(parse_xml_tree(xml_file_name))
    selected_handles = []
    for child in tree_root:
        if(child_name_in_build_handles(child.attrib, build_handles)):
            selected_handles.append(child.attrib)
    return selected_handles


def get_builds_to_monitor_from_xml(xml_file_name, build_names_to_monitor_config_filename):
    child_attributes = read_selected_builds_from_xml(xml_file_name)
    global build_names_to_monitor
    build_names_to_monitor = read_builds_to_monitor_from_config(build_names_to_monitor_config_filename)
    builds_to_monitor = filter(get_builds_to_monitor, child_attributes)
    return builds_to_monitor
