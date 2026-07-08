// Data containers
let brandModels = {};
let modelDetails = {};
let latestPrediction = {};

// Dropdowns
const brandSelect = document.getElementById("brand");
const modelSelect = document.getElementById("model");

// Input fields
const mileageInput = document.getElementById("mileage");
const engineInput = document.getElementById("engine");
const powerInput = document.getElementById("max_power");
const seatsInput = document.getElementById("seats");

// Loading animation while predicting

const form = document.getElementById("predictionForm");
const predictBtn = document.getElementById("predictBtn");
const buttonText = document.getElementById("buttonText");

const data = await response.json();
latestPrediction = data;


function highlightField(input) {

    input.style.backgroundColor = "#e8f5e9";

    // setTimeout(() => {
    //     input.style.backgroundColor = "";
    // }, 1000);

}

// Load brand -> models
fetch("/static/brand_models.json")
    .then(response => response.json())
    .then(data => {
        brandModels = data;
    });

// Load model details
fetch("/static/model_details.json")
    .then(response => response.json())
    .then(data => {
        modelDetails = data;
    });

// Populate models when brand changes
brandSelect.addEventListener("change", function () {

    const brand = this.value;

    modelSelect.innerHTML =
        '<option value="">Select Model</option>';

    if (!brandModels[brand]) return;

    brandModels[brand].forEach(model => {

        const option = document.createElement("option");

        option.value = model;
        option.textContent = model;

        modelSelect.appendChild(option);

    });

    // Clear previous values
    mileageInput.value = "";
    engineInput.value = "";
    powerInput.value = "";
    seatsInput.value = "";

});

// Autofill specifications when model changes
modelSelect.addEventListener("change", function () {

    const brand = brandSelect.value;
    const model = this.value;

    if (!modelDetails[brand]) return;
    if (!modelDetails[brand][model]) return;

    const details = modelDetails[brand][model];

    mileageInput.value = details.mileage;
    highlightField(mileageInput);

    engineInput.value = details.engine;
    highlightField(engineInput);

    powerInput.value = details.max_power;
    highlightField(powerInput);

    seatsInput.value = details.seats;
    highlightField(seatsInput);

});


form.addEventListener("submit", async function (e) {

    e.preventDefault();

    // Loading state
    predictBtn.disabled = true;
    buttonText.innerHTML = `
        <span class="spinner-border spinner-border-sm"></span>
        Predicting...
    `;

    const formData = new FormData(form);

    try {

        const response = await fetch("/predict", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        // Price
        document.getElementById("modalPrice").textContent = data.prediction;

        // Vehicle Details
        document.getElementById("mBrand").textContent = data.brand;
        document.getElementById("mModel").textContent = data.model;
        document.getElementById("mAge").textContent = data.vehicle_age + " Years";
        document.getElementById("mKm").textContent = data.km_driven + " km";
        document.getElementById("mFuel").textContent = data.fuel_type;
        document.getElementById("mTransmission").textContent = data.transmission_type;
        document.getElementById("mMileage").textContent = data.mileage + " km/l";
        document.getElementById("mEngine").textContent = data.engine + " cc";
        document.getElementById("mPower").textContent = data.max_power + " bhp";
        document.getElementById("mSeats").textContent = data.seats;
        document.getElementById("mSeller").textContent = data.seller_type;

        // Show Modal
        const modal = new bootstrap.Modal(
            document.getElementById("predictionModal")
        );

        modal.show();

    } catch (error) {

        alert("Something went wrong!");

        console.error(error);

    } finally {

        predictBtn.disabled = false;

        buttonText.textContent = "Predict Selling Price";

    }

});

document
.getElementById("downloadReport")
.addEventListener("click", async () => {

    const response = await fetch("/download-report",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify(latestPrediction)

    });

    const blob = await response.blob();

    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;

    a.download = "Used_Car_Valuation_Report.pdf";

    a.click();

    window.URL.revokeObjectURL(url);

});