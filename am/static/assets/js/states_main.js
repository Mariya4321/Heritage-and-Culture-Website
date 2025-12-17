// Smooth Scroll for Navigation Links
document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href').substring(1);
        const targetSection = document.getElementById(targetId);
        targetSection.scrollIntoView({
            behavior: 'smooth',
            block: 'start',
        });
    });
});

// Image Slider Functionality
let currentIndex = 0;
const slides = document.querySelectorAll(".slides .slide");
const totalSlides = slides.length;

function showSlide(index) {
    slides.forEach((slide, i) => {
        slide.classList.toggle("active", i === index);
    });
    currentIndex = index;
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % totalSlides;
    showSlide(currentIndex);
}

function prevSlide() {
    currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
    showSlide(currentIndex);
}

// Auto-slide every 3 seconds
setInterval(nextSlide, 3000);


function toggleInfo(button) {
    const extraInfo = button.previousElementSibling; // Get the div with extra info
    const isHidden = extraInfo.style.display === "none";
    
    if (isHidden) {
        extraInfo.style.display = "block";  // Show the extra info
        button.textContent = "Read Less";   // Change button text
    } else {
        extraInfo.style.display = "none";   // Hide the extra info
        button.textContent = "Read More";   // Change button text back
    }
}

// Data for states and their places
const statePlaces = {
    karnataka: ["Bengaluru", "Mysuru", "Hampi", "Badami"],
    delhi: ["Red Fort", "Qutub Minar", "India Gate", "Lotus Temple"],
    up: ["Taj Mahal", "Agra Fort", "Varanasi", "Lucknow"],
    maharashtra: ["Shaniwar Wada", "Raigadh Fort", "Agakhan Palace", "Shirdi"],
    // Add more states and places as needed
};

// Function to update places dropdown based on selected state
function updatePlacesDropdown() {
    const stateDropdown = document.getElementById('state-dropdown');
    const placeDropdown = document.getElementById('place-dropdown');
    const selectedState = stateDropdown.value;

    // Clear current options
    placeDropdown.innerHTML = '<option value="">-- Select Place --</option>';

    // If a state is selected, populate the places
    if (selectedState) {
        const places = statePlaces[selectedState] || [];
        places.forEach(place => {
            const option = document.createElement('option');
            option.value = place.toLowerCase().replace(/\s+/g, '-'); // Format for URL or id purposes
            option.textContent = place;
            placeDropdown.appendChild(option);
        });
    }
}

// Function to handle search (for now, just log the selected state and place)
function search() {
    const state = document.getElementById('state-dropdown').value;
    const place = document.getElementById('place-dropdown').value;
    
    if (state && place) {
        console.log(`Searching for ${place} in ${state}`);
        // Add your actual search functionality here

    } else {
        alert("Please select both state and place");
    }
}
