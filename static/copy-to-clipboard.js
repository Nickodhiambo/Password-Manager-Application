document.addEventListener('DOMContentLoaded', function() {
  var copyButton = document.getElementById('copy');

  copyButton.addEventListener('click', function() {
      var usernameInput = document.getElementById('usernameInput');

      navigator.clipboard.writeText(usernameInput.value).then(function() {
          console.log('Copying to clipboard was successful!');
          // Optionally, provide user feedback that copying was successful
      }, function(err) {
          console.error('Could not copy text: ', err);
          // Optionally, inform the user that copying failed
      });
  });
});
