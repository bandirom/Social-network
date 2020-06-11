var readURL = function(input) {
    console.log('here')
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('.avatar').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
        upload_image(input);
    }
}
$(".file-upload").on('change', function(e){
    readURL(this);
});

$('#id_ajax_upload_form').submit(function(e){
        e.preventDefault();
        $form = $(this)
        var formData = new FormData(this);
        $.ajax({
            url: $form.attr('action'),
            type: 'POST',
            data: formData,
            success: function (response) {
                $('.error').remove();
                console.log(response)
                if(response.error){
                    $.each(response.errors, function(name, error){
                        error = '<small class="text-muted error">' + error + '</small>'
                        $form.find('[name=' + name + ']').after(error);
                    })
                }
                else{

                    window.location = ""
                }
            },
            cache: false,
            contentType: false,
            processData: false
        });
    });

function extendObj(obj1, obj2){
    for (var key in obj2){
        if(obj2.hasOwnProperty(key)){
            obj1[key] = obj2[key];
        }
    }
    return obj1;
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
