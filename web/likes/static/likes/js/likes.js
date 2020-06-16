function like()
{

    var like = $(this);
    var action = like.data('action');
    var dislike = like.next();
    var href = dislike.data('href')
    var csrf = dislike.data('csrf')
    var slug = dislike.data('slug')

    $.ajax({
        url : href,
        type : 'POST',
        data : {
            'csrfmiddlewaretoken': csrf,
            'obj' : slug
            },

        success : function (json) {
            like.find("[data-count='like']").text(json.like_count);
            dislike.find("[data-count='dislike']").text(json.dislike_count);
        }
    });

    return false;
}

function dislike()
{
    var dislike = $(this);
    var action = dislike.data('action');
    var like = dislike.prev();
    var href = dislike.data('href')
    var csrf = dislike.data('csrf')
    var slug = dislike.data('slug')

    $.ajax({
        url : href,
        type : 'POST',
        data : {
            'csrfmiddlewaretoken': csrf,
            'obj' : slug
        },

        success : function (json) {
            dislike.find("[data-count='dislike']").text(json.dislike_count);
            like.find("[data-count='like']").text(json.like_count);
        }
    });

    return false;
}

// Подключение обработчиков
$(function() {
    $('[data-action="like"]').click(like);
    $('[data-action="dislike"]').click(dislike);
});