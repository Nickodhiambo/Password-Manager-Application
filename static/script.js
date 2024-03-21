const generatePasswordBtn = document.getElementById('generatePasswordBtn');
const passwordInput = document.getElementById('id_password');
if(generatePasswordBtn) {
    generatePasswordBtn.addEventListener('click', function () {
        const newPassword = generateStrongPassword();
        passwordInput.value = newPassword;
    });
    
}

function generateStrongPassword(length = 12) {
    const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+{}:<>?";
    let password = "";
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * charset.length);
        password += charset[randomIndex];
    }
    return password;
}

document.addEventListener('DOMContentLoaded', function () {
    // Copy functionality
    var copyIcon = document.querySelectorAll('.copy');
    copyIcon.forEach((icon) => {
        icon.addEventListener('click', function (event) {
            const input = event.target.parentNode.querySelector('input')
            navigator.clipboard.writeText(input.value).then(function () {
                event.target.innerText = "check"
                setTimeout(() => {
                    event.target.innerText = 'content_copy'
                }, 1000)
            }, function (err) {
                console.error('Could not copy text: ', err);
            });
        });
    })
    var toggleVisibilityIcon = document.getElementById('toggleVisibility');
        toggleVisibilityIcon.addEventListener('click', function () {
            var passwordInput = document.getElementById('passwordInput');
            if (passwordInput.type === "password") {
                passwordInput.type = "text";
                toggleVisibilityIcon.innerText = "visibility_off";
            } else {
                passwordInput.type = "password";
                toggleVisibilityIcon.innerText = "visibility";
            }
        });
});
