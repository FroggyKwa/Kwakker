function load_feed()
{
    var element = document.getElementById("feed");
    var last_post = document.getElementById("last");
    if (last_post != null)
    {
        var last_id = last_post.db_id;

    }
    else
    {
        var last_id = '-1';
    }

    var new_posts = jQuery.ajax('/api/v01/posts/' + last_id, {
        success: function(){
                                element.innerHTML = element.innerHTML + new_posts.responseJSON; //innerhtml - то что написано внутри тега
                                last_post.id = '';
                            }
    }); //todo: Ilyaaaaa help
    }
