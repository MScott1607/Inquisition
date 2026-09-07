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