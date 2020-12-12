$(function () {
    $(window).on('scroll', function () {
        if ( $(window).scrollTop() > 10 ) {
            $('.navbar').addClass('active');
        } else {
            $('.navbar').removeClass('active');
        }
    });
});

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#tmpimg')
                .attr('src', e.target.result)
                .width(e.target.width)
                .height(e.target.height);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

function upload(event) {
    document.getElementById("loading").classList.remove("e-hidden");
    document.getElementById("table").innerHTML = "";
    event.preventDefault();
    var data = new FormData($('#myImage').get(0));
    console.log($('#myImage').get(0))
    $.ajax({
        url: $(this).attr('action'),
        type: $(this).attr('method'),
        data: data,
        cache: false,
        processData: false,
        contentType: false,
        success: function(data) {
            print(data)
        }
    });
    return false;
    }

    $(function() {
        $('#myImage').submit(upload);
    });

    function print(data){
        var html = `
        <thead>
        <tr class="text-center">
            <th colspan="2">Resultados</th>
        </tr>
        </thead>
        <tbody>
            <tr>
                <th scope="row" class="text-right">Clase</th>
                <td>${data['result']}</td>
            </tr>
            <tr>
                <th scope="row" class="text-right">Certeza</th>
                <td>${data['certainty']}</td>
            </tr>
        </tbody>
        `;
        document.getElementById("table").innerHTML = html;
        document.getElementById("loading").classList.add("e-hidden");
    }