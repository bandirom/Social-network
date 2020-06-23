$.ajaxSetup({
    headers: { "X-CSRFToken": getCookie("csrftoken") }
});

function like_icon(is_liked, is_disliked){
    var icon_tag_add =  $("i[id='like']")
    var icon_tag_rm = $("i[id='dislike']")
    if (is_liked){
        update_class(icon_tag_add, "fas", "far")
    }
    else {
        update_class(icon_tag_add, "far", "fas")
    }
    if (is_disliked){
        update_class(icon_tag_rm, "fas", "far")
    }
    else {
        update_class(icon_tag_rm, "far", "fas")
    }
}

function dislike_icon(is_liked, is_disliked){
    var icon_tag_add =  $("i[id='dislike']")
    var icon_tag_rm =  $("i[id='like']")
    if (is_disliked){
        update_class(icon_tag_add, "fas", "far")
    }
    else {
        update_class(icon_tag_add, "far", "fas")
    }
    if (is_liked) {
        update_class(icon_tag_rm, "fas", "far")
    }
    else {
        update_class(icon_tag_rm, "far", "fas")
    }

}

function update_class(icon_tag, add_class, rm_class) {
        icon_tag.removeClass(rm_class)
        icon_tag.addClass(add_class)
}

function like()
{
    var like = $(this);
    var action = like.data('action');
    var dislike = like.next();
    var href = like.data('href')
    var slug = like.data('slug')
    $.ajax({
        url : href,
        type : 'POST',
        data : {
            'obj' : slug
        },
        success : function (json) {
            like.find("[data-count='like']").text(json.like_count);
            dislike.find("[data-count='dislike']").text(json.dislike_count);
            like_icon(json.is_liked, json.is_disliked)
        },
        error: function (json) {
            console.log(json)
            console.log("error")
        },
    })
    return false;
}

function dislike()
{
    var dislike = $(this);
    var action = dislike.data('action');
    var like = dislike.prev();
    var href = dislike.data('href')
    var slug = dislike.data('slug')
    $.ajax({
        url : href,
        type : 'POST',
        data : {
            'obj' : slug
        },
        success : function (json) {
            dislike.find("[data-count='dislike']").text(json.dislike_count);
            like.find("[data-count='like']").text(json.like_count);
            dislike_icon(json.is_liked, json.is_disliked)
        },
        error: function (json) {
            console.log("error")
            console.log(json)
        }
    });

    return false;
}

// Подключение обработчиков
$(function() {
    $('[data-action="like"]').click(like);
    $('[data-action="dislike"]').click(dislike);
});


// Получение переменной cookie по имени
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}