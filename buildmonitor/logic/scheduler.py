import sched
import time
import urllib2
import base64
import httplib

from xml_parser import get_builds_to_monitor_from_xml, read_file, get_builds_to_monitor


poll_scheduler = sched.scheduler(time.time, time.sleep)
current_build_status = {}


def create_file(filename, content):
    file_handle = open(filename, 'w')
    file_handle.truncate()
    file_handle.write(content)
    file_handle.close()


def get_attribs_of_builds_to_monitor(build_names, all_builds):
    global build_names_to_monitor
    build_names_to_monitor = build_names
    return filter(get_builds_to_monitor, all_builds)

def save_cctray(cctray, file_name):
    create_file(file_name, cctray.read())


def get_cctray_xml(password=None, url=None, username=None):
    request = urllib2.Request(url)
    if(username and password):
        base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
    try:
        cctray = urllib2.urlopen(request)
    except urllib2.HTTPError, e:
        return None
    except urllib2.URLError, e:
        return None
    except httplib.HTTPException, e:
        return None
    except Exception:
        return None
    return cctray


def download_cctray_xml(url, username, password, file_name):
    if(url[-4:] != ".xml"):
        return None
    if(username and password):
        cctray = get_cctray_xml(password, url, username)
    else:
        cctray = get_cctray_xml(url=url)
    if(cctray):
        save_cctray(cctray, file_name)
        return 1
    else:
        return None

def read_config(config_file_name):
    config = read_file(config_file_name)
    config_array = config.split("\n")
    return config_array[0], config_array[1], config_array[2]


def controller():
    download_url, username, password = read_config("config")
    download_cctray_xml(download_url, username, password, file_name="cctray.xml")
    builds_to_monitor = get_builds_to_monitor_from_xml('cctray.xml', 'builds_to_monitor')
    for build in builds_to_monitor:
        current_build_status[str(build['name'])] = str(build['lastBuildStatus'])
    return current_build_status


def scheduler_minute(scheduler_local):
    controller()
    for build_name in current_build_status.keys():
        if (current_build_status[build_name] == "Success"):
            print "Success"
        else:
            pass
    scheduler_local.enter(1, 1, scheduler_minute, (scheduler_local, ))