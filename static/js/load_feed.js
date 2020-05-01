var element = document.getElementById("feed");
var last_post = element.getElementById("last");
var last_id = last_post.db_id;
delete last_post.id;

var new_posts = jQuery.ajax('localhost:5000/api/v01/posts/' + last_id); //todo: Ilyaaaaa help

element.innerHTML = element.innerHTML + new_posts; //innerhtml - то что написано внутри тега
