function buyProduct(id) {
    swal("Starting the transaction...", "", "info");
    let csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    let amount = document.getElementById('amount_'+id).value || 1;
    $.post('/buy_product/'+id+'/', {
        amount: amount,
        csrfmiddlewaretoken: encodeURI(csrfToken)
    }).done(function (result, status) {
        response = JSON.parse(result);
        if (status === 'success'){
            swal("Will be redirected to the application", "", "info");
            setTimeout(function() {
                window.location.replace(response['url']);
            }, 2000)
        } else {
            swal(response['message'], "", "error");
        }
    }).fail(function (result, status) {
        response = JSON.parse(result);
        swal(response['message'], "", "error");
    });
}