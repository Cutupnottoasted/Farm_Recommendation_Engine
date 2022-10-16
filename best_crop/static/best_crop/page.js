document.addEventListener('DOMContentLoaded', function(){
    submit = document.querySelector(".submit")
    submit.addEventListener("click", () => {
        nitrogen = document.querySelector("#nitro").value
        phosphorus = document.querySelector("#phos").value
        potassium = document.querySelector("#pot").value
        temperature = document.querySelector("#temp").value
        humidity = document.querySelector("#hum").value
        ph = document.querySelector("#ph").value
        rain = document.querySelector("#rain").value
        find_best_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rain)
        nitrogen, phosphorus, potassium, temperature, humidity, ph, rain
    })
})

function find_best_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rain){
    fetch('/find_best', {
        method: 'POST',
        body: JSON.stringify({
            nitro: nitrogen,
            phos: phosphorus,
            pot: potassium,
            temp: temperature,
            hum: humidity,
            ph_value: ph,
            rainfall: rain
        })
    })
    .then(response => response.json())
    .then(value => {
        console.log(value)
    })
}