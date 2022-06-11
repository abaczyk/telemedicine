const slide = document.querySelector('.slide')
const images = document.querySelectorAll('.slide img')

//Przyciski
const prevBtn = document.querySelector('#prevBtn')
const nextBtn = document.querySelector('#nextBtn')

//Licznik
let counter = 1;
const size = images[0].clientWidth;

slide.style.transform = 'translateX(' + (-size * counter) + 'px)'

//Listenery dla przyciskow
nextBtn.addEventListener('click', () => {
    if(counter >= images.length - 1)
        return;
    slide.style.transition = "transform 0.3s ease-in-out";
    counter++;
    slide.style.transform = 'translateX(' + (-size * counter) + 'px)';
});

prevBtn.addEventListener('click', () => {
    if(counter <=0)
        return;
    slide.style.transition = "transform 0.3s ease-in-out";
    counter--;
    slide.style.transform = 'translateX(' + (-size * counter) + 'px)';
});

//Zapetlenie odtwarzania zdjec
slide.addEventListener('transitionend', () => {
    if(images[counter].id === 'lastClone'){
         slide.style.transition = "none";
         counter = images.length - 2;
         slide.style.transform = 'translateX(' + (-size * counter) + 'px)';
    }
    if(images[counter].id === 'firstClone'){
         slide.style.transition = "none";
         counter = images.length - counter;
         slide.style.transform = 'translateX(' + (-size * counter) + 'px)';
    }
});