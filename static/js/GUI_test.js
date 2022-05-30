canvasObj = {};

diagramObj = {
    line: [],
    circle: [],
    rectengle: [],
};

/* 
clearrect can't clean all circle
is the thickness's problem or is something wrong at the clip or clearrect
 */

class diagram {
    constructor(g)
    {
        //
    }
    get_center(point)
    {
        var X = point.X;
        var Y = point.Y;
        console.log("X: " + X + ", Y: " + Y);
    }
}

class circle
{
    constructor(point){
        /*using 3point to count area surface and build 3dmodel*/
        this.first_point = {X: point[0].X, Y: point[0].Y};
        this.second_point = {X: point[1].X, Y: point[1].Y};
        this.final_point = {X: point[2].X, Y: point[2].Y};
        this.cal_circle();
    }

    cal_circle()
    {
        /*calculate X, Y position and calculate radius of this circle*/
        var x12 = this.first_point.X - this.second_point.X;
        var y12 = this.first_point.Y - this.second_point.Y;
        var x13 = this.first_point.X - this.final_point.X;
        var y13 = this.first_point.Y - this.final_point.Y;
        var powx = [Math.pow(this.first_point.X, 2), Math.pow(this.second_point.X, 2), Math.pow(this.final_point.X, 2)];
        var powy = [Math.pow(this.first_point.Y, 2), Math.pow(this.second_point.Y, 2), Math.pow(this.final_point.Y, 2)];
        
        var det_x12 = ((powx[0]-powx[1])-(powy[1]-powy[0]))/2;
        var det_x13 = ((powx[0]-powx[2])-(powy[2]-powy[0]))/2;
        var det = (y12*x13) - (x12*y13)

        this.x0 = -((y13*det_x12)-(y12*det_x13))/det;
        this.y0 = -((x12*det_x13)-(x13*det_x12))/det;

        this.r0 = Math.pow((this.final_point.X-this.x0), 2) + Math.pow((this.final_point.Y-this.y0), 2);
        this.r0 = Math.sqrt(this.r0);
    }

    set_final_point(final_point)
    {
        this.final_point = final_point;
        this.cal_circle();
    }

    clear_circle(ctx)
    {
        ctx.clearRect(this.x0-this.r0-1, this.y0-this.r0-1, (this.r0*2)+2, (this.r0*2)+2);
        ctx.restore();
    }

    get_x0()
    {
        return this.x0;
    }
}

// csrf_tokenの取得に使う
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function Send_data()
{
    var csrf_token = getCookie("csrftoken");
    $.ajax({
        method:"POST",
        url: "Save_canvas/",
        data: diagramObj,
        datatype: "json",
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        },
        success: function(data){
            console.log("success");
            console.log(data);
        },
        error: function(data){
            alert("error");
        },
    })
}


function Clickbox()
{
    var message = document.getElementById("input-message").value;
    message = "input message: " + message;
    document.getElementById("output-message").innerHTML = message;
}

function draw_circle(ctx, crl)
{
    ctx.beginPath();
    ctx.arc(crl.x0, crl.y0, crl.r0, 0, 2 * Math.PI);
    ctx.stroke();
}

function Draw()
{
    var mousedown_check = false;
    var X = 0, Y = 0;
    var offset = canvasObj.canvas.offset();
    var count = 0;
    var point = [];
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
                    console.log("mouse location: x " + X + " , y " + Y);
                    //console.log("osffset position " + offset.top + ", " + offset.left);
                    canvasObj.ctx.beginPath();
                    canvasObj.ctx.moveTo(X, Y);
                    point.push({X: X, Y: Y});
                    mousedown_check = true;
                    //return ;
                    break;
                case "circle":
                    console.log("inside circle");
                    offset = canvasObj.canvas.offset();
                    X = (e.clientX - offset.left) + window.pageXOffset;
                    Y = (e.clientY - offset.top) + window.pageYOffset;
                    point.push({X: X, Y: Y});
                    count++;
                    if(count == 3)
                    {
                        var crl = new circle(point);
                        console.log(point);
                        console.log(crl.x0 + " " + crl.y0 + " " + crl.r0);
                        draw_circle(canvasObj.ctx, crl);
                        diagramObj.circle.push(crl);
                        point = [];
                        mousedown_check = true;
                    }
                    break;
                case "delete":
                    mousedown_check = true;
                    offset = canvasObj.canvas.offset();
                    X = (e.clientX - offset.left) + window.pageXOffset;
                    Y = (e.clientY - offset.top) + window.pageYOffset;
                    canvasObj.ctx.clearRect(X, Y, 10, 10);
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
                        point.push({X: X, Y: Y});
                        break;
                    case "circle":
                        if (count == 3)
                        {
                            var i = diagramObj.circle.length-1;
                            X = (e.clientX - offset.left) + window.pageXOffset;
                            Y = (e.clientY - offset.top) + window.pageYOffset;
                            diagramObj.circle[i].clear_circle(canvasObj.ctx);
                            diagramObj.circle[i].set_final_point({X: X, Y: Y});
                            draw_circle(canvasObj.ctx, diagramObj.circle[i]);
                        }
                        else console.log("not = 3");
                        break;
                    case "delete":
                        X = (e.clientX - offset.left) + window.pageXOffset;
                        Y = (e.clientY - offset.top) + window.pageYOffset;
                        canvasObj.ctx.clearRect(X, Y, 10, 10);
                        break;
                    default:
                        //console.log("hello");
                }
                
            }
        });
        canvasObj.canvas.mouseup(function(e)
        {
            switch (canvasObj.graph)
                {
                    case "line":
                        diagramObj.line.push(point);
                        point = []
                        break;
                    case "circle":

                        break;
                    default:
                        break;
                }
            mousedown_check = false;
            if (count == 3) count = 0;
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
      canvas2.attr("height", window.innerHeight-75);
      $("document").ready(function()
      {
        //create a grid canvas
        $("#navbarNav2 #nav_Canvas").on("click", function()
        {
            $("#GUI_window_navbar").css("display", "grid");
            Draw();
        });
        //close the grid block
        $(".close").on("click", function()
        {
            canvasObj.ctx.clearRect(0, 0, $(canvas2).attr("width"), $(canvas2).attr("height"));
            $("#GUI_window_navbar").css("display", "none");
        });
        //change diagram to circle
        $("#circle").on("click", function()
        {
            canvasObj.graph = "circle";
        });
        //change diagram to line
        $("#line").on("click", function()
        {
            canvasObj.graph = "line";
        });
        //delete element
        $("#delete").on("click", function()
        {
            canvasObj.graph = "delete";
        });
        //clear canvas
        $("#clear").on("click", function()
        {
            canvasObj.ctx.clearRect(0, 0, $(canvas2).attr("width"), $(canvas2).attr("height"));
        });
        $("#Save").on("click", function()
        {
            Send_data();
            //alert("circle: " + diagramObj.circle[0].get_x0());
        });
      });
}