document.addEventListener('DOMContentLoaded', function() {
  // Copy functionality
  var copyIcon = document.getElementById('copy');
  copyIcon.addEventListener('click', function() {
      var passwordInput = document.querySelector('input[name="password"]');
      navigator.clipboard.writeText(passwordInput.value).then(function() {
          console.log('Copying to clipboard was successful!');
      }, function(err) {
          console.error('Could not copy text: ', err);
      });
  });

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
