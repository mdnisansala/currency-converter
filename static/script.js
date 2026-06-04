$(document).ready(function () {
    $('#from').select2();
    $('#to').select2();
});

function swapCurrencies() {

    let from = document.getElementById("from");
    let to = document.getElementById("to");

    let temp = from.value;
    from.value = to.value;
    to.value = temp;

    $('#from').trigger('change');
    $('#to').trigger('change');
}