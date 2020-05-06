function load_feed(tags=[])
{
    var element = document.getElementById("feed");
    var last_post = document.getElementById("last");
    /*if (last_post != null)
    {
        var last_id = last_post.getAttribute('db_id');
    }
    else
    {
        var last_id = '-1';
    }*/
    if (last_post == null) //поменять на undefined есчо
    {
        last_id = "";
    }
    else
    {
        last_id = 'post_id=' + last_post.getAttribute('db_id');
    }
    var new_posts = jQuery.ajax('/api/v01/posts?' + 'tags=' + tags + '&' + last_id, {
        success: function(){
                                element.innerHTML = element.innerHTML + new_posts.responseJSON; //innerhtml - то что написано внутри тега
                                last_post.id = '';
                            }
    });
    }