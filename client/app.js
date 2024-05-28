// Function to load locations and area types
function onPageLoad(){
//     var url = "http://127.0.0.1:5000/get_location_names";  // url through which we are loading location names
    var url = "/api/get_location_names";  // for nginx
    $.get(url,function(data,status){
        if(data){
            var locations = data.locations;  // gets all the locations names
            var location = document.getElementById('location');  // referencing through id
            $(location).empty();  // initially no locations
            for(var l in locations){
                var opt = new Option(locations[l]);  // create new option for every locations
                $(location).append(opt);  // keep appending the new options
            }
        }
    });

//     var url1 = "http://127.0.0.1:5000/get_area_types";  // url through which we are loading area_types
    var url1 = "/api/get_area_types";
    $.get(url1,function(data,status){
        if(data){
            var area_types = data.area_types;
            var area= document.getElementById('area');
            $(area).empty();
            for(var a in area_types){
                var opt = new Option(area_types[a]);
                $(area).append(opt);
            }
        }
    });
}

// Function to get BHK value
function getBHKValue(){
    var size = document.getElementById('size');
    return parseInt(size.value);
}

// Function to get bathroom value
function getBathroomValue(){
    var bathroom = document.getElementById('bathroom');
    return parseInt(bathroom.value);
}

// Function to get balcony value
function getBalconyValue(){
    var balcony = document.getElementById('balcony');
    return parseInt(balcony.value);
}

// Function to predict price
function predictPrice(){
    var locationDropdown = document.getElementById('location'); 
    var areaDropdown = document.getElementById('area');
    var sqftInput = document.getElementById('total_sqft');
    var size = getBHKValue();
    var bath = getBathroomValue();
    var balcony = getBalconyValue();
    var predicted_price = document.getElementById('predicted_price')

    var location = locationDropdown.value;
    var area = areaDropdown.value;
    var sqft = parseFloat(sqftInput.value);

    console.log("Location name:", location);
    console.log("Area Type:", area);
    console.log("Size :",size);
    console.log("Square Feet value:", sqft);
    console.log("Bathroom :",bath);
    console.log("Balcony :",balcony);

//     var url = "http://127.0.0.1:5000/predict_price";
    var url = "/api/predict_price";
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            location: location,
            area_type: area,
            size: size,
            total_sqft: sqft,
            bath: bath,
            balcony: balcony
        },
        contentType: 'application/x-www-form-urlencoded',
        success: function(data) {
            predicted_price.value = data.predicted_price.toString() + " Lakhs";
        }
    });
}



document.addEventListener('DOMContentLoaded', function() {
    // Initialize page load function
    onPageLoad();
});

window.onload = onPageLoad;  // call the function when loading the page
