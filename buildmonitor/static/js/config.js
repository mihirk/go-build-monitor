$('.pipeline_wrapper').cssConsole({
    inputName:'pipeline_url',
    charLimit: 200,
    type: "text"
});
$('.username_wrapper').cssConsole({
    inputName:'username',
    charLimit: 200,
    type: "text"
});
$('.password_wrapper').cssConsole({
    inputName:'password',
    charLimit: 200,
    type: "password"
});
$("input[value='Submit']").cssConsole();
$(".errorlist").cssConsole();
$('#submit').on('click', function(){
    $('#config').submit();
});