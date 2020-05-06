function load_feed()
{
    var element = document.getElementById("feed");
    var last_post = document.getElementById("last");
    if (last_post != undefined)
    {
        var last_id = last_post.getAttribute("db_id");
        console.log(last_id);
    }
    else
    {
        var last_id = '-1';
    }
    if (last_id != undefined)
    {
    var new_posts = jQuery.ajax('/api/v01/posts' + '?post_id=' + last_id, {
        success: function(){
                                element.innerHTML = element.innerHTML + new_posts.responseJSON; //innerhtml - то что написано внутри тега
                                last_post.id = '';
                            }
    }); //todo: Ilyaaaaa help
  }
    }
