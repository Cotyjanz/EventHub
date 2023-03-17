 // Sharebutton.js
 //Author: Coty Janz

  var shareButton = document.getElementById('share_button');
  var confirmMessage = document.getElementById('confirm_message');

  shareButton.addEventListener('click', function(event) {
    var dummyElement = document.createElement('textarea');
    dummyElement.value = window.location.href;
    document.body.appendChild(dummyElement);
    dummyElement.select();
    document.execCommand('copy');
    document.body.removeChild(dummyElement);
    confirmMessage.style.display = 'inline-block';
  });
