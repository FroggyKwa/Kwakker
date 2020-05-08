function like_btn_js(id)
{
    let user = document.getElementById('profile_link');
        user = user.getAttribute('href');
        user = user.slice(1);
        user = jQuery.ajax('/api/v01/users?' + user,
                           {
                                success: function()
                                {
                                    user = user.responseJSON;
                                    let user_id = user['users'][0]['id'];
                                    let btn = document.getElementById(id);
                                    let likes = btn.parentNode;
                                    if (btn.getAttribute('liked') == 'false')
                                    {
                                        jQuery.ajax('/api/v01/like?' + 'post_id=' + id + '&user_id=' + user_id,
                                                    {
                                                        method:'POST',
                                                        success: function()
                                                        {
                                                            btn.setAttribute('liked', 'true');
                                                            btn.childNodes[1].setAttribute('src', "/static/img/like_filled.png");
                                                            let n = Number(likes.getAttribute('value'));
                                                            console.log(likes);
                                                            console.log(n);
                                                            n = n + 1;
                                                            console.log(n);
                                                            likes.setAttribute('value', n);
                                                            likes.childNodes[1].innerHTML = "Лайки: " + n;
                                                        }
                                                    });
                                    }
                                    else
                                    {
                                        jQuery.ajax('/api/v01/like?' + 'post_id=' + id + '&user_id=' + user_id,
                                                    {
                                                        method:'DELETE',
                                                        success: function()
                                                        {
                                                            btn.setAttribute('liked', 'false');
                                                            btn.childNodes[1].setAttribute('src', "/static/img/like.png");
                                                            let n = Number(likes.getAttribute('value'));
                                                            n = n - 1;
                                                            likes.setAttribute('value', n);
                                                            likes.childNodes[1].innerHTML = "Лайки: " + n;
                                                            }
                                                    });
                                    }
                                }
                            });

};
