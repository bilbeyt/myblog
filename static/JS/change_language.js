$(document).ready(function() {
    $("#language-button").on('click', function() {
        $("#language-form-submit").trigger('click');
    });
});
$(document).ready(function() {
    $("#language-button").on('click', function(e) {
        e.preventDefault();
        $("#language-form-submit").trigger('click');
    });
});
