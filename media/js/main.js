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
        document.getElementById("imgTemp").classList.add("e-hidden");
    }
}

function upload(event) {
    event.preventDefault();
    document.getElementById("results-table").classList.remove("e-hidden");
    document.getElementById("table").innerHTML = "";
    if(document.getElementById("image").files.length == 0){
        document.getElementById("table").innerHTML = "<p class='text-center'> Seleccione una imagen </p>";
        return false;
    }
    document.getElementById('class-btn').disabled = true;
    document.getElementById("loading").classList.remove("e-hidden");
    var data = new FormData($('#myImage').get(0));
    console.log($('#myImage').get(0))
    $.ajax({
        url: $(this).attr('action'),
        type: $(this).attr('method'),
        data: data,
        cache: false,
        processData: false,
        contentType: false,
        error: function(){
            document.getElementById("table").innerHTML = "<p class='text-center'> La imagen no pudo ser clasificada </p>";
            document.getElementById('class-btn').disabled = false;
            document.getElementById("loading").classList.add("e-hidden");
        },
        success: function(data) {
            print(data);
            document.getElementById('class-btn').disabled = false;
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
                <td>${data['certainty']} %</td>
            </tr>
        </tbody>
        `;
        document.getElementById("table").innerHTML = html;
        document.getElementById("loading").classList.add("e-hidden");
    }

    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
      })

function p(){
    document.getElementById('no').classList.remove('e-hidden');
    setTimeout(function() {
        document.getElementById('no').classList.add('e-hidden');
     }, 1000);
}