function rS() {
    a = $("#navbarcontainer").height() + 20;
    $("body").attr("style", "padding-top: " + a + "px");
}

function getImage() {
    c = {
        latitude: $('#latitude').val(),
        longitude: $('#longitude').val(),
        heading: $('#heading').val(),
        pitch: $('#pitch').val()
    };
    $.post('', c, function(data) {
        console.log(data);
        $("#picture").attr('src', data['address']);
    })

}
$(window).resize(rS);
$(function() {
    rS();
    // gL();
});