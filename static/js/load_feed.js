var element = document.getElementById("feed");
var last_post = element.getElementById("last");
var last_id = last_post.db_id;
delete last_post.id;

var new_posts = jQuery.ajax('localhost:5000/api/v01/posts/' + last_id); //todo: Ilyaaaaa help
new_posts = JSON.parse(new_posts)

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
