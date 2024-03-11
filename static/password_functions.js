// Toggle Show/Hide Password
document.addEventListener("DOMContentLoaded", function() {
  var togglePasswordButton = document.getElementById("togglePassword");
  if (togglePasswordButton) {
      togglePasswordButton.addEventListener("click", function() {
          var password = document.getElementById("password");
          var type = password.getAttribute("type") === "password" ? "text" : "password";
          password.setAttribute("type", type);
          this.textContent = type === "password" ? "Show" : "Hide";
      });
  }

  // Copy Password to Clipboard
  var copyPasswordButton = document.getElementById("copyPassword");
  if (copyPasswordButton) {
      copyPasswordButton.addEventListener("click", function() {
          var password = document.getElementById("password");
          password.select();
          password.setSelectionRange(0, 99999); // For mobile devices
          document.execCommand("copy");
          alert("Password copied to clipboard!");
      });
  }
});
