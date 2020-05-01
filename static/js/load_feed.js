function load_feed()
{
    var element = document.getElementById("feed");
    var last_post = document.getElementById("last");
    if (last_post != null)
    {
        var last_id = last_post.db_id;
        delete last_post.id;
    }
    else
    {
        var last_id = '10';
    }

    var btn = document.getElementById("btn");
    delete btn;

    var new_posts = jQuery.ajax('/api/v01/posts/' + last_id); //todo: Ilyaaaaa help
    //new_posts = JSON.parse(new_posts);
    alert(new_posts)

    element.innerHTML = element.innerHTML + new_posts["message"]; //innerhtml - то что написано внутри тега
    element.innerHTML = element.innerHTML + "<button id='btn' onclick='load_feed()'>Загрузить еще</button>";
}