document.addEventListener('DOMContentLoaded', function() {
  // Copy functionality
  var copyIcon = document.querySelectorAll('.copy');
  copyIcon.forEach((icon) => {
    icon.addEventListener('click', function(event) {
        const input = event.target.parentNode.querySelector('input')
        navigator.clipboard.writeText(input.value).then(function() {
            event.target.innerText = "check"
            setTimeout(() => {
                event.target.innerText = 'content_copy'
            }, 1000)
        }, function(err) {
            console.error('Could not copy text: ', err);
        });
    });
  })

  // Toggle password visibility
  var toggleVisibilityIcon = document.getElementById('toggleVisibility');
  toggleVisibilityIcon.addEventListener('click', function() {
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
