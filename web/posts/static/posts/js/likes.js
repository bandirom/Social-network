
function updateLikes(btn, newCount){
    if (newCount == 1) {
        btn.text(newCount + ' Like')
    }
    else {
        btn.text(newCount + ' Likes')
    }
}

$('.like-btn').click(function(e){
    e.preventDefault()
    var this_ = $(this)
    var likeUrl = this_.attr('data-href')
    $.ajax({
        url: likeUrl,
        method: "GET",
        data: {},
        success: function(data){
            $icon_tag =  $("i[name^='like']")
            if (data.liked){
                updateLikes(this_, data.likecount)
                $icon_tag.removeClass('far fa-heart')
                $icon_tag.addClass('fas fa-heart')
            } else {
                updateLikes(this_, data.likecount)
                $icon_tag.removeClass('fas fa-heart')
                $icon_tag.addClass('far fa-heart')
            }
        },
        error: function(error){
            console.log(error);
        },
    })
});