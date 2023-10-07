const slider = document.querySelector("#slider");
let slidersection = document.querySelectorAll(".slider_section");
let slidersectionLast = slidersection[slidersection.length-1];

const btnLeft = document.querySelector("#btn-left");
const btnRight = document.querySelector("#btn-right");

slider.insertAdjacentElement('afterbegin',slidersectionLast);
//mover boton a la de recha
function next(){
    let slidersectionFirst = document.querySelectorAll(".slider_section")[0];
    slider.style.marginleft = "-200%";
    slider.style.transition = "all 0.5s";
    setTimeout(function(){
        slider.style.transition = "none";
        slider.insertAdjacentElement('beforeend',slidersectionFirst);
        slider.style.marginleft = "-100%";
    },500);
}
//mover boton a la izquierda
function prev(){
    let slidersection = document.querySelectorAll(".slider_section");
    let slidersectionLast = slidersection[slidersection.length-1];
    
    slider.style.marginleft = "0%";
    slider.style.transition = "all 0.5s";
    setTimeout(function(){
        slider.style.transition = "none";
        slider.insertAdjacentElement('afterbegin',slidersectionLast);
        slider.style.marginleft = "-100%";
    },500);
}

btnRight.addEventListener('click',function(){
    next();
});

btnLeft.addEventListener('click',function(){
    prev();
});