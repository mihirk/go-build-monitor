jQuery(function ($, undefined) {
        var builds = $('#all_builds').val();
        builds = JSON.parse(builds);
        var builds_to_monitor = [];
        var build_completion = function (terminal, command, callback) {
            callback(builds);
        };
        var greetings = function () {
            builds.forEach(function (build) {
                $('.build_list').append('<div class="build_name">' + build + "</div>")
            });
        };
        greetings();
        var term_config = {
            greetings: "",
            name: 'build_monitor',
            height: $('body').height(),
            tabcompletion: true,
            completion: build_completion,
            prompt: "Enter build name > "
        };

        var validate_build_name = function (build_name) {
            return builds.indexOf(build_name) > -1
        };

        var get_builds_to_monitor = function (command, term) {
            term.focus(true);
            if (validate_build_name(command)) {
                builds_to_monitor.push(command);
                $("input[value='" + command + "']").prop('checked', true);
            }
            else if (command == "") {
                if (builds_to_monitor.length == 0) {
                    term.error("No builds selected");
                }
                else {
                    $('.form').submit();
                }
            }
            else {
                term.error('Build does not exist, please check that you have typed in the build name correctly');
            }

        };

        $('#build_form').terminal(get_builds_to_monitor, term_config);
    }
);