// const toggles = document.querySelectorAll(".faq-toggle");

// toggles.forEach((toggle) => {
//     toggle.addEventListener("click", () => {
//         // Targets the .faq container directly and reliably
//         const faqItem = toggle.closest(".faq");
//         if (faqItem) {
//             faqItem.classList.toggle("active");
//         }
//     });
// });

document.addEventListener('DOMContentLoaded', () => {
    const faqButtons = document.querySelectorAll('.faq-question');

    faqButtons.forEach(button => {
        button.addEventListener('click', () => {
    const isExpanded = button.getAttribute('aria-expanded') === 'true';

      // Optional: Close other items (accordion behavior)
    faqButtons.forEach(otherButton => {
        if (otherButton !== button) {
            otherButton.setAttribute('aria-expanded', 'false');
        }
    });

    // Toggle current item
            button.setAttribute('aria-expanded', !isExpanded);
        });
    });
});