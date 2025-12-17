// JavaScript source code

document.addEventListener('DOMContentLoaded', () => {
    const readMoreButtons = document.querySelectorAll('.read-more-btn');

    readMoreButtons.forEach((button) => {
        button.addEventListener('click', () => {
            const extraContent = button.previousElementSibling;
            if (extraContent.style.display === 'none' || extraContent.style.display === '') {
                extraContent.style.display = 'inline';
                button.textContent = 'Read Less';
            } else {
                extraContent.style.display = 'none';
                button.textContent = 'Read More';
            }
        });
    });
});
