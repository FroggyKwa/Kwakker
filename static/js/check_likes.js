function check_likes()
{
    let feed = document.getElementById('feed');
    let user = document.getElementById('profile_link');
    user = user.getAttribute('href');
    user = user.slice(1);
    user = jQuery.ajax('/api/v01/users?' + user,
                        {
                            success: function()
                            {
                                user = user.responseJSON;
                                let user_id = user['users'][0]['id'];
                                feed.childNodes.forEach(function(item, i, arr)
                                {
                                    if (item.className != 'post')
                                    {
                                        return;
                                    }
                                    let post_id = item.getAttribute('db_id');
                                    let like = jQuery.ajax('/api/v01/like?' + 'user_id=' + user_id + '&post_id=' + post_id,
                                    {
                                                        success: function()
                                                        {
                                                            like = like.responseJSON
                                                            console.log(post_id);
                                                            console.log(like);
                                                            console.log(item.childNodes);
                                                            let like_btn = item.childNodes[7].childNodes[3];
                                                            console.log(like_btn.childNodes);
                                                            if (like['like'])
                                                            {
                                                                like_btn.setAttribute('liked', "true");
                                                                console.log(like_btn.childNodes[3]);
                                                                like_btn.childNodes[1].setAttribute('src', "/static/img/like_filled.png");
                                                            }
                                                            like_btn.addEventListener('click', function(){
                                                            like_btn_js(post_id);
                                                            })
                                                        }
                                    });
                                });
                            }
                        })
}