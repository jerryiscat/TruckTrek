document.addEventListener('DOMContentLoaded', function() {
    // Function to show the route planner
    function showRoutePlanner() {
        var routePlanner = document.getElementById('routePlanner');
        if (routePlanner) {
            routePlanner.style.display = 'block'; // Change display to 'block' to show it
        }
    }

    // Getting the button element
    var saveTruckTypeButton = document.getElementById('saveTruckType');
    
    // Adding a click event listener to the button
    if (saveTruckTypeButton) {
        saveTruckTypeButton.addEventListener('click', function() {
            showRoutePlanner();
        });
    }
});
