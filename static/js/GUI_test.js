canvasObj = {};

class diagram {
    constructor(g)
    //
}

class line{
    //
}

class cricle{
    //
}


function Clickbox()
{
    var message = document.getElementById("input-message").value;
    message = "input message: " + message;
    document.getElementById("output-message").innerHTML = message;
}



function Draw()
{
    var mousedown_check = false;
    var X = 0, Y = 0;
    var offset = canvasObj.canvas.offset();
    console.log(canvasObj.graph);
    canvasObj.ctx.beginPath();
    $(document).ready(function ()
    {
        canvasObj.canvas.mousedown(function(e)
        {
            switch(canvasObj.graph)
            {
                case "line":
                    offset = canvasObj.canvas.offset();
                    //console.log("canvas position is " + offset.top + ", " + offset.left + canvasObj.graph);
                    X = (e.clientX - offset.left) + window.pageXOffset;
                    Y = (e.clientY - offset.top) + window.pageYOffset;
                    //console.log("mouse location: x " + X + " , y " + Y);
                    //console.log("osffset position " + offset.top + ", " + offset.left);
                    canvasObj.ctx.beginPath();
                    canvasObj.ctx.moveTo(X, Y);
                    mousedown_check = true;
                    return ;
                    break;
                case "circle":
                    console.log("inside cricle");
                    break;
                default:
                    //alert("hello");
            }

        });
        canvasObj.canvas.mousemove(function(e)
        {
            if (mousedown_check)
            {
                switch(canvasObj.graph)
                {
                    case "line":
                        //console.log("mouse location: x " + e.clientX + " , y " + e.clientY);
                        X = (e.clientX - offset.left) + window.pageXOffset;
                        Y = (e.clientY - offset.top) + window.pageYOffset;
                        $("#spam_mouse_location").text((X + ", " + Y));
                        canvasObj.ctx.lineTo(X, Y);
                        canvasObj.ctx.stroke();
                        break;
                    case "circle":
                        //console.log("inside cricle");
                        break;
                    default:
                        //console.log("hello");
                }
                
            }
        });
        canvasObj.canvas.mouseup(function(e)
        {
            mousedown_check = false;
            return ;
        });
    });
}

function canvas_main()
{
    var canvas2 = $("#GUI_window_navbar .canvas_test");
      var ctx2 = canvas2[0].getContext("2d");
      var graph = "line";//line
      canvasObj = {
        canvas : canvas2,
        ctx : ctx2,
        graph : graph
    };
      console.log("canvas obj " + canvasObj.graph);
      canvas2.attr("width", window.innerWidth);
      canvas2.attr("height", window.innerHeight);
      $("document").ready(function()
      {
        $("#navbarNav2 #nav_Canvas").on("click", function()
        {
          $("#GUI_window_navbar").css("display", "grid");
          Draw();
        });
        $(".close").on("click", function()
        {
          $("#GUI_window_navbar").css("display", "none");
        });
        $("#circle").on("click", function()
        {
          console.log("click event triggle");
          canvasObj.graph = "circle";
        });
        $("#line").on("click", function()
        {
          console.log("click event triggle");
          canvasObj.graph = "line";
        });
      });
}