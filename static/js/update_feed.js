function update_feed(){
    var element = document.getElementById("feed");

    //var new_posts = jQuery.ajax(url1? settings?);

    new_posts.forEach(
        function(item, i, arr) // item - элемент, i - номер, arr - перебираемый массив
        {
            var t = render_template(template, item);
            element.innerHTML = t + element.innerHTML;
        });
}