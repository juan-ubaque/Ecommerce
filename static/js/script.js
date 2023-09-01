// julian
const burger = document.querySelector(".burger");
const navMenu = document.querySelector(".nav-menu");

burger.addEventListener("click", () => {
    burger.classList.toggle("activate");
    navMenu.classList.toggle("activate");
})

document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () => {
    burger.classList.remove("active")
    navMenu.classList.remove("active")

}))