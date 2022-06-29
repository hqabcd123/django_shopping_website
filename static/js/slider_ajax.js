

$(".item").click(function(){
    let csrf_token = getCookie("csrftoken");
    $.ajax({
        method:"POST",
        url: "adv_page/",
        data: {
            value: $(this).children("img").attr("alt"),
        },
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        },
        success: function(data){
            window.location.href = "adv_page/";
            console.log(data);
        },
        error: function(data){
            alert("error");
        },
    });
})