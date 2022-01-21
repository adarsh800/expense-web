const usernameField = document.querySelector("#usernameField");
const feedBackArea = document.querySelector(".invalid_feedback");
const submitBtn = document.querySelector("#submitBtn")
const usernameSuccessOutput = document.querySelector(".usernameSuccessOutput");
const emailField = document.querySelector("#emailField");
const passwordField = document.querySelector("#passwordField");
const Email_feedBackArea = document.querySelector(".emailFeedBackArea");
const showPasswordToggle = document.querySelector("#eye");
let data_copy = "";
let state = false;


const handleToggleInput = (e) => {
 
  if(state)
    {
      passwordField.setAttribute("type","password") ;
      showPasswordToggle.style.color = "grey"; 
      state = false;
} 
  else {
    passwordField.setAttribute("type","text") ;
    showPasswordToggle.style.color = "#EC407A";  
    state = true;
  }
};
showPasswordToggle.addEventListener("click", handleToggleInput)






emailField.addEventListener("keyup", (e) => {
  const emailVal = e.target.value;
  let mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  
  
  emailField.classList.remove("is-invalid");
  Email_feedBackArea.style.display = "none";

  if (emailVal.length > 0) {
    
    fetch('validate-email/', {
      method: 'post',
      body: JSON.stringify({ email: emailVal })
      
    })
      .then((res) => res.json())
      .then((data) => {
        data_copy = data;
        console.log("data", data);
        data_copy = data.email_error;
        console.log(data_copy);
      });
  }
  if (data_copy) {
          console.log(emailVal)
          submitBtn.disabled = true;
          emailField.classList.add("is-invalid");
          Email_feedBackArea.style.display = "block";
          
          Email_feedBackArea.innerHTML = `<p>${data_copy}</p>`;
          submitBtn.disabled = true;
        } 
        else {
          submitBtn.removeAttribute("disabled");
        }
      


});


usernameField.addEventListener("keyup", (e) => {
  
  const usernameVal = e.target.value;

  usernameSuccessOutput.style.display = "block";

  usernameField.classList.remove("is-invalid");
  feedBackArea.style.display = "none";

  if (usernameVal.length > 0) {

    usernameSuccessOutput.textContent = `Checking  ${usernameVal}`;
    fetch('validate-username/', {
      method: 'post',
      body: JSON.stringify({ username: usernameVal })
      
    })
      .then((res) => res.json())
      .then((data) => {
        usernameSuccessOutput.style.display = "none";
        if (data.username_error) {
          usernameField.classList.add("is-invalid");
          feedBackArea.style.display = "block";
          feedBackArea.innerHTML = `<p>${data.username_error}</p>`;
          submitBtn.disabled = true;
        } else {
          submitBtn.removeAttribute("disabled");
        }
      });
  }
});