// Function to trigger the animation of the dog image
function toggleAnimation() {
  const dogImg = document.getElementById('dog-img');
  dogImg.classList.toggle('animated');
}


// Functions to add mouseover and mouseout events to change text on an element for the let's chat button
function mOver(obj) {
  obj.innerHTML = "Start!";
}

function mOut(obj) {
  obj.innerHTML = "Let's chat!";
}


// Function to check if the passwords match and display a message if not
function checkPasswords(prefix) {
  // Get the password input elements
  const passwordInput = document.getElementById(`${prefix}-password`);
  const confirmPasswordInput = document.getElementById(`confirm-${prefix}-password`);

  // Get the message element
  const passwordMessage = document.getElementById(`${prefix}-password-message`);

  if (passwordInput.value !== confirmPasswordInput.value) {
    passwordMessage.style.display = "block";
    passwordMessage.textContent = "Passwords do not match!";
  } else {
    passwordMessage.style.display = "none";
    passwordMessage.textContent = "";
  }
}



// Function to verify user input when the "Verify!" button is clicked
function clickVerify(prefix) {
  // Get the input elements
  const username = document.getElementById(`${prefix}-username`);
  const password = document.getElementById(`${prefix}-password`);
  const confirmPassword = document.getElementById(`confirm-${prefix}-password`);
  const email = document.getElementById(`${prefix}-email`);

  // Get the warning message element
  const verifyMessage = document.getElementById(`${prefix}-verify-message`);

  // Check if all required input fields have values
  if (!username.value || !password.value || !confirmPassword.value || !email.value) {
    // If any input field is empty, show the warning message
    verifyMessage.style.display = "block";
    verifyMessage.textContent = "Please fill out all required fields.";
  } else {
    // If all input fields are filled, hide the warning message
    verifyMessage.style.display = "none";
    verifyMessage.textContent = "";
  }
}

// Function to scroll to the bottom of the chat window
function scrollToBottom() {
  var mainchat = document.getElementById("mainchat");
  mainchat.scrollTop = mainchat.scrollHeight;
}

function bindEmailCaptchaClick() {
  $("#captcha-btn").click(function (event) {
    $this = $(this);
    event.preventDefault();
    //get the user's input email
    var email = $("input[name='email']").val();
    //use ajax to send the input email to flask.
    $.ajax({
      url: "/send?email=" + email,
      method: "GET",
      success: function (result) {
        var code = result["code"];
        console.log(result);
        if (code == 200) {
          var countdown = 60;
          // set the 60 second countdown. during the countdown, remove the click function and make the button not clickable until count down finished.
          $this.off("click");
          $this.prop("disabled", true);
          var timer = setInterval(function () {
            $this.text(countdown);
            countdown -= 1;
            // when the count down equal 0, make the button content change back to verify and enable the button. reactivate the whole function.
            if (countdown <= 0) {
              clearInterval(timer);
              $this.text("verify!");
              $this.prop("disabled", false);
              bindEmailCaptchaClick();
            }
          }, 1000);
          alert("Sucessfully send the code!");
        } else if (code == 500) {
          alert("The email address is already used!");
        } else if (code == 300) {
          alert("The email address does not exist");
        }
      },
      fail: function (error) {
        console.log(error);
      },
    });
  });
}
// this function is very similiar to the above function, only modified some variable from html to flask.
function updateEmailCaptchaClick() {
  $("#captcha-btnr").click(function (event) {
    $this = $(this);
    event.preventDefault();
    var email = $("input[name='email']").val();
    var username = $("input[name='username']").val();
    $.ajax({
      url:
        "/reset/update?email=" +
        encodeURIComponent(email) +
        "&username=" +
        encodeURIComponent(username),
      method: "GET",
      success: function (result) {
        var code = result["code"];
        console.log(result);
        if (code == 200) {
          var countdown = 60;
          $this.off("click");
          $this.prop("disabled", true);
          var timer = setInterval(function () {
            $this.text(countdown);
            countdown -= 1;
            if (countdown <= 0) {
              clearInterval(timer);
              $this.text("verify!");
              $this.prop("disabled", false);
              bindEmailCaptchaClick();
            }
          }, 1000);
          alert("Successfully send the code!");
        } else if (code == 500) {
          alert("The email address not correct");
        } else if (code == 300) {
          alert("The email address not correct");
        } else if (code == 400) {
          alert("The username and email not match");
        }
      },
      fail: function (error) {
        console.log(error);
      },
    });
  });
}

// The main Jquery
$(function () {
  bindEmailCaptchaClick();
  updateEmailCaptchaClick();
  // this function aims to verify the user's input. it check the user's input each time when user presses a key.
/*   $("#register-password").keyup(function () {
    var password1 = $("#register-password").val();
    if (password1.length <= 6) {
      $("#register-password-message").text("Characters should be more than 6");
    } else if (password1.length >= 16) {
      $("#register-password-message").text("Characters should be less than 16");
    } else {
      $("#register-password-message").text("");
    }

  });
  $("#confirm-register-password").keyup(function () {
    var password2 = $("#confirm-register-password").val();
    var password1 = $("#register-password").val();
    if (password1 != password2) {
      $("#register-password-message").text("Password do not match");
    } else {
      $("#register-password-message").text("");
    }

  }); */
  // this function do the same function as above. for the reset page.
  /* $("#rpwdr,#reppwdr,#v1r").keyup(function () {
    var password1 = $("#rpwdr").val();
    var password2 = $("#reppwdr").val();
    var username = $("#rnr").val();
    var email = $("#email1").val();
    var code = $("#v1r").val();
    if (password1 != password2) {
      $("#warning1").show();
      $("#rpwdr,#reppwdr").css("background-color", "pink");
    } else {
      $("#rpwdr,#reppwdr").css("background-color", "skyblue");
      $("#warning1").hide();
    }
    if (password1.length <= 6 || password1.length >= 16) {
      $("#warningl1").show();
      $("#rpwdr,#reppwdr").css("background-color", "pink");
    } else {
      $("#warningl1").hide();
    }
    if (password1.length > 6 && password1.length < 16 && username.length!=0 && email.length!=0 && code!=0){
      $("#submitreset").prop("disabled", false);
    }
  }); */
  // This function get the users input and send it to flask via ajax. Then get the reply from chatgpt in flask. It will automatically add a <div> in the main chat div to show the user's input and chatgpt's reply.
  $("#enter").click(function (event) {
    event.preventDefault();
    var question = $("input[name='Chat']").val();
    var newqe = $("<div>").text(question).addClass("Que");
    $("#mainchat").append(newqe);
    $.ajax({
      url: "/chat/answer?question=" + question,
      type: "GET",
      success: function (data) {
        rp = data["response"];
        console.log(rp);
        var newans = $("<div>").text(rp).addClass("Ans");
        $("#mainchat").append(newans);
        $("input[name='Chat']").val("")
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
  $("#checkin").click(function (event) {
    $this=$(this);
    event.preventDefault();
    $.ajax({
      url: "/chat/check",
      type: "GET",
      success: function (data) {
        count = data["counts"];
        $this.text("Checked in " + count+" day");
        $this.prop("disabled", true);
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
  $("#Luna,#Jack,#Bob").click(function (event) {
    $this=$(this);
    var name = $this.attr('id');
    event.preventDefault();
    $.ajax({
      url: "/chat/switch?dog="+name,
      type: "GET",
      success: function (data) {
        code=data["code"];
        if (code == 200) {
          console.log("success");
          var ans = $("<div>").text("Woof woof! Hello there, I'm "+name+". How can I assist you today?").addClass("Ans");
          $("#mainchat").empty();
          $("#mainchat").append(ans);
        }
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
});
