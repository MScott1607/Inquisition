const toggles = document.querySelectorAll(".faq-toggle");

toggles.forEach((toggle) => {
    toggle.addEventListener("click", () => {
        // Targets the .faq container directly and reliably
        const faqItem = toggle.closest(".faq");
        if (faqItem) {
            faqItem.classList.toggle("active");
        }
    });
});


let slideIndex = 0;
const slides = document.querySelectorAll(".advisorslides");
const carousel = document.getElementById("advisor-images");
let timer;


function slideShow(index) {
    slides.forEach((slide) => {
        slide.style.display = "none";
    });

    slideIndex = (index + slides.length) % slides.length;
    slides[slideIndex].style.display = "block";
}

function startAutoPlay() {
    clearTimeout(timer);
    timer = setTimeout(() => {
        slideShow(slideIndex + 1);
        startAutoPlay();
    }, 2000);
}

function pauseAutoPlay() {
    clearTimeout(timer);
}

carousel.addEventListener("mouseenter", pauseAutoPlay);
carousel.addEventListener("mouseleave", startAutoPlay);


slideShow(slideIndex);
startAutoPlay();

