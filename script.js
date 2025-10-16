// script.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('signupForm');
    form.addEventListener('submit', function(event) {
        confirmusername = requestAnimationFrame.form['username']
        confirmemail = requestAnimationFrame.form['email']
        confirmPassword = requestAnimationFrame.form['password']
        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm_password').value;
        const confirmUsername = document.getElementById('confirm_username').value;
        const confirmEmail = document.getElementById('confirm_email').value;

        if (username == confirm_username) {
            alert('Username is taken')
            event.preventDefault();
        }

        if (email == confirm_email) {
            alert('Email is already registered')
            event.preventDefault();
        }

//        if (password !== confirmPassword) {
//            alert('Passwords do not match!');
//            event.preventDefault(); // Prevent form submission
//        }
        // Add more client-side validation as needed (e.g., email format regex)
    });
});




