function load_feed(tags=[])
{
    var element = document.getElementById("feed");
    var last_post = document.getElementById("last");
    if (last_post == null)
    {
        var last_id = "";
    }
    else
    {
        var last_id = '&post_id=' + last_post.getAttribute('db_id');
    }
    var new_posts = jQuery.ajax('/api/v01/posts?' + 'tag=' + tags + last_id, {
        success: function(){
          $(last_post).removeAttr("id");
          element.innerHTML = element.innerHTML + new_posts.responseJSON;
          last_post = document.getElementById('last')
          last_id = last_post.getAttribute('db_id');
          if (last_id == "1")
          {
              let btn = document.getElementById("btn");
              btn.parentNode.removeChild(btn);
          }
          check_likes();
                            }
    });
    }
