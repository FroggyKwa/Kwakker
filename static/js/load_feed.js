function load_feed(tags=[])
{
    var element = document.getElementById("feed");
    var last_post = document.getElementById("last");
    console.log(element);
    if (last_post == null)
    {
        last_id = "";
    }
    else
    {
        last_id = '&post_id=' + last_post.getAttribute('db_id');
    }
    var new_posts = jQuery.ajax('/api/v01/posts?' + 'tag=' + tags + last_id, {
        success: function(){
          console.log(Boolean(tags));
          if (tags == false)
          {
            $(last_post).removeAttr("id");
            element.innerHTML = element.innerHTML + new_posts.responseJSON;
            $(last_post).remove()
          }
          else
          {
            element.innerHTML = new_posts.responseJSON;
          }

                                //innerhtml - то что написано внутри тега
                            }
    });
    }
