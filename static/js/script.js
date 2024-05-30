let openEye = document.getElementById("open-eye")
let closeEye = document.getElementById("close-eye")
let userPassword = document.getElementById("user-password")

const toggleEye = ()=>{
    if (userPassword.type === "password"){
        userPassword.type = "text"
        closeEye.classList.toggle("hide-eye")
        openEye.classList.toggle("hide-eye")
        console.log("show pass")
    }else{
        userPassword.type = "password"
        closeEye.classList.toggle("hide-eye")
        openEye.classList.toggle("hide-eye")
        console.log("hide pass")
    }
}

openEye.addEventListener("click", toggleEye)
closeEye.addEventListener("click", toggleEye)