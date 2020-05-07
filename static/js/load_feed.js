function load_feed(tags=[])
{
    var element = document.getElementById("feed");
    var last_post = document.getElementById("last");
    if (last_post == null)
    {
        last_id = "";
    }
    else
    {
        last_id = 'post_id=' + last_post.getAttribute('db_id');
        console.log(last_id);
    }
    var new_posts = jQuery.ajax('/api/v01/posts?' + 'tags=' + tags + '&' + last_id, {
        success: function(){
                                $(last_post).removeAttr("id");
                                element.innerHTML = element.innerHTML + new_posts.responseJSON;
                                //innerhtml - то что написано внутри тега
                                console.log(last_post);
                                $(last_post).remove()
                            }
    });
    }
