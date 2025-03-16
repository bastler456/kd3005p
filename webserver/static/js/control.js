async function sendData(url, method, data) {
    let result; 
    
    try {
        const response = await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            },
            body: data
        });
        console.log('Response from Flask:', response);

        const jsonData = await response.json();
        console.log('Received data:', jsonData);

        result = jsonData;

    } catch (error) {
        console.error('Error sending data:', error);
    }

    return result ? result.data : undefined; 
}


const voltage_setting = document.getElementById("voltage");
const current_setting = document.getElementById("current");
const power_on = document.getElementById("power");
const set = document.getElementById("set");
const error_current = document.getElementById("error_current")
const error_voltage = document.getElementById("error_voltage")
const ident = document.getElementById("identification")


set.addEventListener("click", function() {
    let voltage = parseFloat(voltage_setting.value);
    let current = parseFloat(current_setting.value)
    let error = false
    if (voltage > 31 || voltage < 0){
        error_voltage.innerHTML = "voltage invalid"
        error = true
    }
    else{
        error_voltage.innerHTML = ""
    }
    if (current > 5 || current < 0) {
        error_current.innerHTML = "current invalid"
        error = true
    }
    else{
        error_current.innerHTML = ""
    }
    if (error != true){
        let data = JSON.stringify({"voltage": voltage, "current": current})
        sendData('/set', 'POST', data);
    }
});


power_on.addEventListener("click", function() {
    if (power_on.innerHTML== "Power ON"){
        power_on.innerHTML = "Power OFF"
    }
    else{
        power_on.innerHTML = "Power ON"
    }
    let data = JSON.stringify({power: power_on.innerHTML})
    sendData('/power', 'POST', data);
});

sendData('/ident', 'GET').then(result => {
    ident.innerHTML = result
})

            