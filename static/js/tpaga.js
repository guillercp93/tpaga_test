function buyProduct(id) {
    let csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    let amount = document.getElementById(`amount_${id}`).value || 1;
    $.post(`/buy_product/${id}/`, {
        amount,
        csrfmiddlewaretoken: encodeURI(csrfToken)
    }, (result, status) => {
        response = JSON.parse(result);
        if (status === 'success'){
            window.location.replace(response['url']);
        } else {
            alert(response['message']);
        }
    });
}