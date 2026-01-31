document.addEventListener('DOMContentLoaded', () => {

    // State Management
    let currentStep = parseInt(localStorage.getItem('openlock_step')) || 1;
    const totalSteps = 4;

    // DOM Elements
    const steps = document.querySelectorAll('.mission-card');
    const indicators = document.querySelectorAll('.step-indicator');
    const progressFill = document.querySelector('.progress-fill');

    // Initialize UI
    updateUI();

    // Event Listeners for "Next" buttons
    document.querySelectorAll('.btn-next').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const nextStepId = parseInt(e.target.dataset.next);
            if (nextStepId > currentStep) {
                currentStep = nextStepId;
                saveState();
                updateUI();
                scrollToTop();
            }
        });
    });

    // Reset Progress (hidden feature or footer link)
    window.resetProgress = function () {
        localStorage.removeItem('openlock_step');
        location.reload();
    };

    function updateUI() {
        // Update Steps Visibility
        steps.forEach(step => {
            const stepId = parseInt(step.dataset.step);

            // Logic: Show only current active step? 
            // Or show all previous as completed? 
            // User requested "Tabs" look logic. Let's show CURRENT step prominently.

            if (stepId === currentStep) {
                step.classList.add('active-card');
                step.style.display = 'block';
            } else {
                step.classList.remove('active-card');
                step.style.display = 'none';
            }
        });

        // Update Indicators
        indicators.forEach(ind => {
            const indStep = parseInt(ind.dataset.step);
            if (indStep < currentStep) {
                ind.classList.add('completed');
                ind.classList.remove('active');
                ind.innerHTML = '✓';
            } else if (indStep === currentStep) {
                ind.classList.add('active');
                ind.classList.remove('completed');
                ind.innerHTML = indStep;
            } else {
                ind.classList.remove('active', 'completed');
                ind.innerHTML = indStep;
            }
        });

        // Update Progress Bar
        const progressPercent = ((currentStep - 1) / (totalSteps - 1)) * 100;
        if (progressFill) progressFill.style.width = `${progressPercent}%`;
    }

    function saveState() {
        localStorage.setItem('openlock_step', currentStep);
    }

    function scrollToTop() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

});
