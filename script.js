document.addEventListener('DOMContentLoaded', () => {
    
    // Accordion Logic
    const accordions = document.querySelectorAll('.accordion-header');

    accordions.forEach(acc => {
        acc.addEventListener('click', function() {
            // Toggle active class
            this.classList.toggle('active');

            // Toggle panel visibility
            const panel = this.nextElementSibling;
            if (this.classList.contains('active')) {
                panel.style.maxHeight = panel.scrollHeight + "px";
            } else {
                panel.style.maxHeight = null;
            }
        });
    });

    // Dynamic Copyright Year
    const yearSpan = document.getElementById('current-year');
    if(yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    // Smooth Scroll for specific anchor limits? 
    // Browser default scroll-behavior: smooth in CSS handles most, 
    // but we can add specific handlers if needed for the 'Start' button.
    
    const startBtn = document.querySelector('.btn-start');
    if(startBtn) {
        startBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const firstStep = document.getElementById('step-1');
            if(firstStep) {
                firstStep.scrollIntoView({ behavior: 'smooth', block: 'start' });
                // Optional: Auto open first step
                const header = firstStep.querySelector('.accordion-header');
                if(header && !header.classList.contains('active')) {
                    header.click();
                }
            }
        });
    }

    // Mailto Handler with Pre-filled body (Optional enhancement)
    const mailBtn = document.querySelector('.btn-mail');
    if(mailBtn) {
        mailBtn.addEventListener('click', (e) => {
            // Logic to grab some status if we wanted to be fancy, 
            // but simple href in HTML is usually more robust for 'mailto'.
            console.log('Opening mail client...');
        });
    }
});
