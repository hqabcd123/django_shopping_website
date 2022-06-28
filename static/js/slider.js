let slider_index = 0;
show_slider(slider_index);

function next_slider(n)
{
    show_slider(slider_index += n);
}

function current_index(n)
{
    show_slider(slider_index = n);
}

function show_slider(n)
{
    let slides = $(".advertise");
    let dot = $(".dot");
    if (n > slides.lenght)
    {
        slider_index = 0;
    }
    for (let i = 0; i < slides.lenght; i++)
    {
        slides[i]
    }
    for (let i = 0; i < dot.lenght; i++)
    {
        slides[i].className
    }
}