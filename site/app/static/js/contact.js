$(document).ready(function() {
    $("#contact-form").submit(function(event) {
        event.preventDefault();
        values = {
            "user_name": $(this).find("#user-name").val(),
            "user_email": $(this).find("#user-email").val(),
            "user_phone": $(this).find("#user-phone").val(),
            "user_topic": $(this).find("#user-topic").val(),
            "user_mesage": $(this).find("#user-message").val()
        };

        $.ajax({
            url: "/contact",
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(values),
            success: function() {
                location.reload();
            },
            error: function(err) {
                console.log("Error");
            }
        });
    });
});
