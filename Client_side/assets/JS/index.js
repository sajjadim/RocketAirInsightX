let btn = document.querySelector(".LaunchButton");
let FuelTypeInput = document.querySelector("#fuels")
let LaunchSiteInputInput = document.querySelector(".launchsite")
let PropellantMassInput = document.querySelector(".propellantMass")
let MaxaltitudeInput = document.querySelector(".maxaltitude")
let FuelMassInput = document.querySelector(".fuelmass")


function error(err) {
    alert(err)
}

function DeactiveLanding(){
    var landing  =  document.getElementById("landing")
    var result  =  document.getElementById("result")
    var timeforfade = 1
    landing.style.animation = `fadeLanding  ${timeforfade}s 1`;
    
    setTimeout(()=>{
        landing.style.display = "none";
        result.style.animation = `faderesult ${timeforfade}s 1`
        result.display = "flex"
        document.body.style.overflowY = "auto"
    },timeforfade *1000)
}



function SendHttpRequest(FuelType, Maxaltitude, FuelMass, PropellentMass, LaunchSite) {
    var xhr = new XMLHttpRequest();
    xhr.onload = () => {
        var response = JSON.parse(xhr.responseText)
        console.log(response)
        document.querySelector(".Pollution-title").innerHTML = `Estimated pollution produced ${response.pollution} KG`
        document.querySelector(".chatgptresult").innerHTML = `Estimated pollution by launching ${response.chat_result.choices[0].text}`
        document.querySelector(".ice_data").innerHTML = `${response.pollution} KG can melt ${response.pollution * 650} KG ice`
         

    }   
    xhr.open("POST", "http://localhost:5000/predict")
    xhr.setRequestHeader("Content-Type", "application/json");
    var payload = {
        fuel_type: FuelType,
        total_propellant_mass: PropellentMass,
        max_altitude: Maxaltitude,
        total_fuel_mass: FuelMass,
        launch_site: LaunchSite,
        chat_suggestion_request_status: true,
        chat_overview_request_status: true,
        chat_suggestion_template: 0,
        chat_suggestion_data: [FuelType, PropellentMass, Maxaltitude, FuelMass, LaunchSite],
        chat_overview_template: 0,
        chat_overview_data: [FuelType, PropellentMass, Maxaltitude, FuelMass, LaunchSite]
    }


    xhr.send(JSON.stringify(payload))

}
btn.onclick = () => {
    let FuelTypeValue = FuelTypeInput.value;

    if (MaxaltitudeInput.value.trim() === "" || !parseInt(MaxaltitudeInput.value.trim())) {
        error("please enter a valid value (Number) in Maxaltitude ")
        return
    }


    if (FuelMassInput.value.trim() === "" || !parseInt(FuelMassInput.value.trim())) {
        error("please enter a valid value (Number) in FuelMass")
        return
    }

    if (PropellantMassInput.value.trim() === "" || !parseInt(PropellantMassInput.value.trim())) {
        error("please enter a valid value (Number) in PropellantMassInput")
        return
    }


    if (LaunchSiteInputInput.value.trim() === "") {
        error("please enter a value in LaunchSiteInputInput ")
        return
    }

    
    DeactiveLanding()

    SendHttpRequest( parseInt(FuelTypeValue) , parseInt(MaxaltitudeInput.value.trim()) ,parseInt(FuelMassInput.value.trim()) ,parseInt(PropellantMassInput.value.trim()) , LaunchSiteInputInput.value.trim())
   
}

