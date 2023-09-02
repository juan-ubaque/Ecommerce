const carouselContainer = document.querySelector('.carousel-container');
const carouselSlides = document.querySelectorAll('.carousel-slide');

let currentIndex = 0;

function updateCarousel() {
    const slideWidth = carouselSlides[0].clientWidth;
    carouselContainer.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
}

function nextSlide() {
    if (currentIndex < carouselSlides.length - 1) {
        currentIndex++;
        updateCarousel();
    }
}

function prevSlide() {
    if (currentIndex > 0) {
        currentIndex--;
        updateCarousel();
    }
}

updateCarousel();

setInterval(nextSlide, 3000); // Cambiar de slide automáticamente cada 3 segundos
