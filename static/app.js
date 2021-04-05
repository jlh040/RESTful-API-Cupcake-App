const BASE_URL = '/api/cupcakes';
const submitButton = $('#submit-button');

putCardsOnPage(getCupcakeArr());

submitButton.click(async function(e) {
    e.preventDefault();
    await sendDataToApi(getDataFromForm());
    $('#cupcakes-list').empty()
    putCardsOnPage(await getCupcakeArr());
    emptyInputs();
})

async function getCupcakeArr() {
    resp = await axios.get(BASE_URL);
    return resp.data.cupcakes;
}

function createCardHtml(flavor, size, rating, image_url) {
    return  `
            <div class="card d-inline-block ms-3 mt-3" style="width: 18rem;">
                <img src="${image_url}" class="card-img-top">
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">Flavor: ${flavor}</li>
                    <li class="list-group-item">Size: ${size}</li>
                    <li class="list-group-item">Rating: ${rating}</li>
                </ul>
            </div>
            `
};

async function putCardsOnPage(arrOfCupcakes) {
    const $cupcakeList = $('#cupcakes-list')
    $cupcakeList.empty()

    for (let obj of await arrOfCupcakes) {
        $cupcakeList.append(
            createCardHtml(obj.flavor, obj.size, obj.rating, obj.image)
        )
    };
};

function getDataFromForm() {
    const flavor = $('#flavor').val();
    const size = $('#size').val();
    const rating = $('#rating').val();
    const image = $('#image').val() ? $('#image').val() : null;

    return {
        flavor,
        size,
        rating,
        image
    }
}

function emptyInputs() {
    $('#flavor').val('');
    $('#size').val('');
    $('#rating').val('');
    $('#image').val('')

    return
}

async function sendDataToApi(obj) {
    await axios.post(
        BASE_URL,
        obj
    )
}










