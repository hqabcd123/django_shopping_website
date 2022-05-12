function Clickbox()
{
    var message = document.getElementById("input-message").value;
    message = "input message: " + message;
    document.getElementById("output-message").innerHTML = message;
}

function check_window_offset(Xoffset, Yoffset)
//true => window is offseted
{
    if (window.pageXOffset == 0 && window.pageYOffset == 0) return false;
    else return true;
}

function Draw(canvas, ctx)
{
    var mousedown_check = false;
    var X = 0, Y = 0;
    var offset = canvas.offset();
    console.log("cnavas position is " + offset.top + ", " + offset.left);
    ctx.beginPath();
    $(document).ready(function ()
    {
        canvas.mousedown(function(e)
        {
            //get mouse position and draw a graph
            X = (e.clientX - offset.left) + window.pageXOffset;
            Y = (e.clientY - offset.top) + window.pageYOffset;
            console.log("mouse location: x " + (e.clientX + window.pageXOffset) + " , y " + (e.clientY + window.pageYOffset));
            console.log("osffset position " + offset.top + ", " + offset.left);
            ctx.beginPath();
            ctx.moveTo(X, Y);
            mousedown_check = true;
        });
        canvas.mousemove(function(e)
        {
            if (mousedown_check)
            {
                console.log("mouse location: x " + e.clientX + " , y " + e.clientY);
                X = (e.clientX - offset.left) + window.pageXOffset;
                Y = (e.clientY - offset.top) + window.pageYOffset;
                $("#spam_mouse_location").text((X + ", " + Y));
                ctx.lineTo(X, Y);
                ctx.stroke();
            }
        });
        canvas.mouseup(function(e)
        {
            mousedown_check = false;
        });
    });
}