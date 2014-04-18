import sched
import time
import urllib2
import base64
import httplib

from xml_parser import  get_builds_to_monitor


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
        return "Invalid Configuration : HTTPError - " + str(e.code)
    except urllib2.URLError, e:
        return "Invalid Configuration : URLError - " + str(e.reason)
    except httplib.HTTPException, e:
        return "Invalid Configuration : HTTPException"
    except Exception:
        return "Invalid Configuration : Exception"
    return cctray


def download_cctray_xml(url, username, password, file_name):
    if(url[-4:] != ".xml"):
        return "Give the cctray url ending with .xml"
    if(username and password):
        cctray = get_cctray_xml(password, url, username)
    else:
        cctray = get_cctray_xml(url=url)
    if("Invalid Configuration : " in cctray):
        return cctray
    else:
        save_cctray(cctray, file_name)
        return "Success"