import sched
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from threading import Timer
import time
from logic.scheduler import download_cctray_xml
from logic.xml_parser import *
from forms import ConfigurationForm, BuildForm


def set_session_with_attributes(configuration_form, request):
    request.session.__setitem__("pipeline_url", configuration_form.data['pipeline_url'])
    request.session.__setitem__("username", configuration_form.data['username'])
    request.session.__setitem__("password", configuration_form.data['password'])


def configuration_page(request, template='configuration.html'):
    if request.method == 'POST':
        configuration_form = ConfigurationForm(request.POST)
        if configuration_form.is_valid():
            set_session_with_attributes(configuration_form, request)
            return HttpResponseRedirect('/getbuilds/')
    else:
        configuration_form = ConfigurationForm()
    return render(request, template, {'configuration_form': configuration_form, })


def get_file_name_per_session(request):
    return "cctrays/" +str(request.session._get_session_key()) + '.xml'


def set_session_with_build_handles(build_names, request):
    request.session.__setitem__("build_handles", build_names)


def get_config_from_session(request):
    pipeline_url = request.session.__getitem__("pipeline_url")
    username = request.session.__getitem__("username")
    password = request.session.__getitem__("password")
    return password, pipeline_url, username


def get_builds(request, template='build_list.html'):
    password, pipeline_url, username = get_config_from_session(request)
    if(download_cctray_xml(pipeline_url, username, password, get_file_name_per_session(request))):
        all_builds = read_build_names_from_xml(get_file_name_per_session(request))
        if request.method == "POST":
            build_form = BuildForm(all_builds=all_builds, data=request.POST)
            if build_form.is_valid():
                build_handles = get_attribs_of_builds_to_monitor(build_form.data.getlist('builds'), all_builds)
                set_session_with_build_handles(build_handles, request)
                return HttpResponseRedirect('/monitor/')
        else:
            build_form = BuildForm(all_builds=all_builds)
        return render(request, template, {"all_builds": all_builds, "build_form": build_form},
                  context_instance=RequestContext(request))
    else:
        return render(request, "invalid.html")


def poll_builds(request):
    password, pipeline_url, username = get_config_from_session(request)
    download_cctray_xml(pipeline_url, username, password, get_file_name_per_session(request))
    build_handles = read_selected_builds_from_xml(get_file_name_per_session(request), request.session.__getitem__('build_handles'))
    set_session_with_build_handles(build_handles, request)
    return HttpResponseRedirect('/monitor/')


def failed_builds(build):
    if (build['lastBuildStatus'] == 'Success'):
        return False
    else:
        return True


def name_status(build):
    return {"name": build['name'], "status": build['lastBuildStatus']}



def show_builds(request, template='monitor.html'):
    build_handles = request.session.__getitem__('build_handles')
    build_handles = map(name_status, build_handles)
    return render(request, template, {"build_handles": build_handles, "div_height": 100/build_handles.__len__() })