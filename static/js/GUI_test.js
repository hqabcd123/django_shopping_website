canvasObj = {};

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

class cricle
{
    constructor(point){
        /*using 3point to count area surface and build 3dmodel*/
        this.first_point = {X: point[0].X, Y: point[0].Y};
        this.second_point = {X: point[1].X, Y: point[1].Y};
        this.final_point = {X: point[2].X, Y: point[2].Y};
        this.draw_cricle();
    }

    draw_cricle()
    {
        /*calculate X, Y position and calculate radius of this cricle*/
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
                    mousedown_check = true;
                    //return ;
                    break;
                case "circle":
                    console.log("inside cricle");
                    offset = canvasObj.canvas.offset();
                    X = (e.clientX - offset.left) + window.pageXOffset;
                    Y = (e.clientY - offset.top) + window.pageYOffset;
                    point.push({X: X, Y: Y});
                    count++;
                    if(count == 3)
                    {
                        var crl = new cricle(point);
                        console.log(point);
                        console.log(crl.x0 + " " + crl.y0 + " " + crl.r0);
                        canvasObj.ctx.beginPath();
                        canvasObj.ctx.arc(crl.x0, crl.y0, crl.r0, 0, 2 * Math.PI);
                        canvasObj.ctx.stroke();
                        count = 0;
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
                        break;
                    case "circle":
                        //console.log("inside cricle");
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
        $("#delete").on("click", function()
        {
          console.log("click event triggle");
          canvasObj.graph = "delete";
        });
      });
}