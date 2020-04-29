var element = document.getElementById("feed");
var last_post = element.getElementById("last");
var last_id = last_post.db_id; //todo: Ilyaaaaa help
delete last_post.id;

var new_posts = jQuery.ajax(url? settings?); //todo: Ilyaaaaa help

new_posts.forEach(
    function(item, i, arr) // item - элемент, i - номер, arr - перебираемый массив
    {
        var t = render_template(template, item); //todo: Ilyaaaaa help
        if (item == arr[arr.length - 1])
        {
            t.id = "last";
        }
        element.innerHTML = element.innerHTML + t; //innerhtml - то что написано внутри тега
    });
