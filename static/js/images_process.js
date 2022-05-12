delay_in_seconds = 1000;
MAX_count = 10;

async function images_loop(Json_img_dir)
{
    console.log(Json_img_dir);
    var IMGArray = new Array();
    var i = 0, count = 0;

    
    for (i = 0; i < Json_img_dir.length; i++)
    {
        var str = "/Media/";
        console.log("len: " + Json_img_dir.length);
        console.log("i: " + i + " " + str + Json_img_dir[i]);
        //await new Promise(resolve => setTimeout(resolve, delay_in_seconds));
        IMGArray[i] = new Image();
        IMGArray[i].src = str + Json_img_dir[i];
        console.log("img array src: " + IMGArray[i].src);
    }
    i = 0;
    for (y = 0; y < 10; y++)
    {
        IMG_laying(IMGArray, i, count);
        await new Promise(resolve => setTimeout(resolve, delay_in_seconds));
        i += 1;
        count += 1;
        if (i > IMGArray.length-1) i = 0;
        if (count > MAX_count) count = 0;
    }
}

async function IMG_laying(IMGArray, i, count)
{
    console.log("inside IMG_laying " + count);
    $("#IMGarray img.top").toggleClass("transparent");
    if (count % 2 == 0)
    {
        console.log("trans top");
        await new Promise(resolve => setTimeout(resolve, delay_in_seconds));
        $("#IMGarray img.top").attr("src", IMGArray[i].src);
        console.log("top img src: " + $("#IMGarray img.top").attr("src"));
    }
    else
    {
        console.log("trans bottom");
        await new Promise(resolve => setTimeout(resolve, delay_in_seconds));
        $("#IMGarray img.bottom").attr("src", IMGArray[i].src);
        console.log("bottom img src: " + $("#IMGarray img.bottom").attr("src"));
    }
}