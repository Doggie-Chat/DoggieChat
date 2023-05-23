// Function to trigger the animation of the dog image
function toggleAnimation() {
  const dogImg = document.getElementById("dog-img");
  dogImg.classList.toggle("animated");
}

// Functions to add mouseover and mouseout events to change text on an element for the let's chat button
function mOver(obj) {
  obj.innerHTML = "Start!";
}

function mOut(obj) {
  obj.innerHTML = "Let's chat!";
}

// Function to display a message if the username exists (used for register page)
function checkUsernameRegister() {
  const usernameInput = document.getElementById(`register-username`);
  const username = usernameInput.value;
  const users = JSON.parse(document.getElementById(`register-username-list`).textContent);

  const usernameMessage = document.getElementById(`register-username-message`);

  if (users.includes(username)) {
    usernameMessage.style.display = "block";
    usernameMessage.textContent = "Username already exists!";
  } else {
    usernameMessage.style.display = "none";
    usernameMessage.textContent = "";
  }
}

// Function to display a message if the username does NOT exist (used for reset page)
function checkUsernameReset() {
  const usernameInput = document.getElementById(`reset-username`);
  const username = usernameInput.value;
  const users = JSON.parse(document.getElementById(`reset-username-list`).textContent);

  const usernameMessage = document.getElementById(`reset-username-message`);

  if (!users.includes(username)) {
    usernameMessage.style.display = "block";
    usernameMessage.textContent = "Username does not exist!";
  } else {
    usernameMessage.style.display = "none";
    usernameMessage.textContent = "";
  }
}


// Function to display a message if passwords are invalid and not match (used for register and reset page)
function checkPasswords(prefix) {
  // Get the password input elements
  const passwordInput = document.getElementById(`${prefix}-password`);
  const confirmPasswordInput = document.getElementById(
    `confirm-${prefix}-password`
  );

  // Get the message element
  const passwordMessage = document.getElementById(`${prefix}-password-message`);
  const password = passwordInput.value;
  const confirmPassword = confirmPasswordInput.value;

  if (password !== confirmPassword) {
    passwordMessage.style.display = "block";
    passwordMessage.textContent = "Passwords do not match!";
  } else if (password.length < 7 || password.length > 15) {
    passwordMessage.style.display = "block";
    passwordMessage.textContent = "Password must be between 7 and 15 characters!";
  } else {
    passwordMessage.style.display = "none";
    passwordMessage.textContent = "";
  }
}

// Function to verify user input when the "Verify!" button is clicked (used for register and reset page)
function clickVerify(prefix) {
  // Get the input elements
  const username = document.getElementById(`${prefix}-username`);
  const password = document.getElementById(`${prefix}-password`);
  const confirmPassword = document.getElementById(`confirm-${prefix}-password`);
  const email = document.getElementById(`${prefix}-email`);

  // Get the warning message element
  const verifyMessage = document.getElementById(`${prefix}-verify-message`);

  // Check if all required input fields have values
  if (
    !username.value ||
    !password.value ||
    !confirmPassword.value ||
    !email.value
  ) {
    // If any input field is empty, show the warning message
    verifyMessage.style.display = "block";
    verifyMessage.textContent = "Please fill out all required fields.";
  } else {
    // If all input fields are filled, hide the warning message
    verifyMessage.style.display = "none";
    verifyMessage.textContent = "";
  }
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
  // Get the #mainchat element
  var mainchat = document.getElementById('mainchat');

  // Function to scroll the #mainchat element to the bottom
  function scrollToBottom() {
    mainchat.scrollTop = mainchat.scrollHeight;
  }
  // This function get the users input and send it to flask via ajax. Then get the reply from chatgpt in flask. It will automatically add a <div> in the main chat div to show the user's input and chatgpt's reply.
  $("#enter").click(function (event) {
    // get the user's input question and add it to a div with class Que and a div with current time. show it in the mainchat div.
    event.preventDefault();
    var question = $("input[name='Chat']").val();
    var newqe = $("<div>").text(question).addClass("Que");
    var currentTimeQ = new Date().toLocaleTimeString("en-AU", {
      timeZone: "Australia/Perth",
    });
    var qtime = $("<div>").text(currentTimeQ).addClass("qtime");
    $("#mainchat").append(newqe);
    $("#mainchat").append(qtime);
    // use ajax to send the question to flask via GET.
    $.ajax({
      url: "/chat/answer?question=" + question,
      type: "GET",
      // get the response from flask which includes the answer from chatgpt. then add it to a div with class Ans and a div with current time. show it in the mainchat div.
      success: function (data) {
        rp = data["response"];
        console.log(rp);
        var newans = $("<div>").text(rp).addClass("Ans");
        var currentTimeA = new Date().toLocaleTimeString("en-AU", {
          timeZone: "Australia/Perth",
        });
        var atime = $("<div>").text(currentTimeA).addClass("atime");
        $("#mainchat").append(newans);
        $("#mainchat").append(atime);
        $("input[name='Chat']").val("");
        scrollToBottom(); // Scroll to the bottom of the chat
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
  // This function get the user's choice of the dogs and switch the dog and print appropriate response to the switch.
  $("#Luna,#Jack,#Bob,#Ruby,#Rosie,#Zeus").click(function (event) {
    $this = $(this);
    // get the id of the button
    var name = $this.attr("id");
    event.preventDefault();
    // use ajax to send the dog name to flask. The flask will change the prompt to chatgpt.
    $.ajax({
      url: "/chat/switch?dog=" + name,
      type: "GET",
      // once success, add the first reply to a div with class Ans and show it in the mainchat div.
      success: function (data) {
        code = data["code"];
        if (code == 200) {
          console.log("success");
          var ans = $("<div>")
            .text(
              "Woof woof! Hello there, I'm " +
                name +
                ". How can I assist you today?"
            )
            .addClass("Ans");

          var currentTimeA = new Date().toLocaleTimeString("en-AU", {
            timeZone: "Australia/Perth",
          });
          var atime = $("<div>").text(currentTimeA).addClass("atime");
          $("#mainchat").empty();
          $("#mainchat").append(ans);
          $("#mainchat").append(atime);
        }
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
  //This function send the user's chosen date and dogname to flask. The response from flask is the related chatting history. It will add the response to a table consist of dogname, chatting date and histories.
  $("#Search").click(function (event) {
    $this = $(this);
    //get the dogname and input from user's input and send it to flask via Ajax.
    $("#search-result").empty();
    var dogname = $("#dogname").val();
    var date = $("#date-input").val();
    event.preventDefault();
    $.ajax({
      url: "/history/search",
      type: "POST",
      data: { dogname: dogname, date: date },
      // once get the response, which is three lists, add a table with 3 columns and use $each to loop the lists. then add the content to the table.
      success: function (data) {
        date = data.date;
        dog = data.dog;
        content = data.content;
        var table = $("<table>");
        headerRow = $("<tr>");
        headerRow.append($("<th>").addClass("date-col").text("Date"));
        headerRow.append($("<th>").addClass("name-col").text("Name"));
        headerRow.append($("<th>").addClass("content-col").text("Content"));
        table.append(headerRow);
        $.each(date, function (index, value) {
          var item1 = value;
          var item2 = dog[index];
          var item3 = content[index];
          var dataRow = $("<tr>").addClass("table-content");
          dataRow.append($("<td>").text(item1));
          dataRow.append($("<td>").text(item2));
          dataRow.append($("<td>").text(item3));
          table.append(dataRow);
        });
        // show the table to search-result div.
        $("#search-result").empty();
        $("#search-result").html(table);
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
});
