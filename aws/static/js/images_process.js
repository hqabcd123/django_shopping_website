function images_loop2()
{
    var result = [];
    console.log("Hello world");
    alert("hello");
}

function images_loop(Json_img_dir)
{
    var result = [];
    delay_in_seconds = 1000;
    console.log("Hello world");
    alert("hello");
    //change Json to array
    for (const i in Json_img_dir)
    {
        console.log(Json_img_dir[i]);
        if (Object.hasOwnProperty.call(Json_img_dir, i))
        {
            result.push(i, Json_img_dir[i]);
            alert(result[i]);
        }
    }
    for (var i = 0; i < result.length; i++)
    {
        setTimeout(function()
        {
            var img = new Image(300, 300);
            img.src = result[i];
            var src = document.getElementById("images_container");
            src.appendChild(img)
        }, delay_in_seconds * 5);
    }
    //document.getElementById("images_container").innerHTML += ""
}

window.onload = images_loop();