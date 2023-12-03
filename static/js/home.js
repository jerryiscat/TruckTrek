// Get references to the button and the routePlanner div
const saveButton = document.getElementById('saveTruckType');
const routePlannerDiv = document.getElementById('routePlanner');

// Add a click event listener to the button
saveButton.addEventListener('click', function () {
    // Check the current display property of the routePlanner div
    if (routePlannerDiv.style.display === 'none' || routePlannerDiv.style.display === '') {
        // If it's hidden, show it
        routePlannerDiv.style.display = 'block';
    } else {
        // If it's visible, hide it
        routePlannerDiv.style.display = 'none';
    }
});
