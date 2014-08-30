jQuery(function ($, undefined) {
        var term_config = {
            greetings: '',
            name: 'build_monitor',
            height: $('body').height(),
            prompt: "Pipeline CCTray XML url > "
        };
        var credentials = {
            username: "",
            password: ""
        };
        var build_config = {
            pipeline_url: "",
            credentials: credentials
        };

        var is_authentication_required = false;

        var validate_url = function (url, term) {
            return url;
        };

        var insert_input_data = function (input_field, value) {
            $(input_field).val(value);
        };

        var clear_config = function () {
            build_config.pipeline_url = "";
            build_config.credentials.username = "";
            build_config.credentials.password = "";
        };


        var config_handler = function (command, term) {

            if (build_config.pipeline_url === "") {
                build_config.pipeline_url = validate_url(command, term);
                insert_input_data('.url', build_config.pipeline_url);
                term.set_prompt('Is authentication required (y/n) > ');
            }
            else if (!is_authentication_required) {
                command = command.toLowerCase();
                if (command === "y" || command === "yes") {
                    is_authentication_required = true;
                    term.set_prompt('Username > ');
                }
                else {
                    insert_input_data('.username', "");
                    insert_input_data('.password', "");
                    $('.form').submit();
                    term.echo("Getting builds");
                    term.set_prompt("");
                }
            }
            else if (build_config.credentials.username === "") {
                build_config.credentials.username = command;
                insert_input_data('.username', command);
                term.set_prompt('Password > ');
                term.set_mask(true);
            }
            else if (build_config.credentials.password === "") {
                build_config.credentials.password = command;
                insert_input_data('.password', command);
                $('.form').submit();
                term.echo("Getting builds");
                term.set_prompt("");

            }
        };

        $('#config_form').terminal(config_handler, term_config);
    }
);