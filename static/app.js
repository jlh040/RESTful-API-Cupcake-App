const BASE_URL = '/api/cupcakes'

async function getCupcakeArr() {
    resp = await axios.get(BASE_URL);
    return resp.data.cupcakes;
}

function createCardHtml(flavor, size, rating, image_url) {
    return  `
            <div class="card d-inline-block ms-3" style="width: 18rem;">
                <img src="${image_url}" class="card-img-top">
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">Flavor: ${flavor}</li>
                    <li class="list-group-item">Size: ${size}</li>
                    <li class="list-group-item">Rating: ${rating}</li>
                </ul>
            </div>
            `
};

async function putCardOnPage(arrOfCupcakes) {
    const $cupcakeList = $('#cupcakes-list')
    for (let obj of await arrOfCupcakes) {
        $cupcakeList.append(
            createCardHtml(obj.flavor, obj.size, obj.rating, obj.image)
        )
    };
};

putCardOnPage(getCupcakeArr());

