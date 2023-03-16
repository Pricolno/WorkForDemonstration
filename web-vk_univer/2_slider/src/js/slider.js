const sliderWrapper = document.querySelector('.slider-wrapper');
const leftArrow = document.querySelector('#slide-arrow-prev');
const rightArrow = document.querySelector('#slide-arrow-next');
const slidesContainer = document.querySelector('.slides-container');

const sliderPointer = document.querySelector('.slider-pointer');
const sliderPointerChildren = document.querySelector('.slider-pointer').children;


const MaxNumberSlide = sliderPointerChildren.length;
let lastNumberSlide = 0;
let currentNumberSlide = 0;


function renderImage(){
    slidesContainer.scrollLeft = currentNumberSlide * sliderWrapper.offsetWidth;
}

function renderSelectButton(){
    sliderPointerChildren[lastNumberSlide].querySelector('input').checked = false;
    sliderPointerChildren[currentNumberSlide].querySelector('input').checked = true;
}

function rengerSlide() {
    renderImage();
    renderSelectButton();
};

leftArrow.addEventListener('click', ()=>{
    console.log("Click leftArrow! " + currentNumberSlide);
    if (currentNumberSlide === 0) {
        return;
    };
    lastNumberSlide = currentNumberSlide;
    currentNumberSlide -= 1;
    rengerSlide();
    console.log(slidesContainer.scrollLeft + " " + sliderWrapper.offsetWidth);
});

rightArrow.addEventListener('click', ()=>{
    console.log("Click rightArrow! " + currentNumberSlide);
    if (currentNumberSlide === (MaxNumberSlide - 1)){
        return;
    };
    lastNumberSlide = currentNumberSlide;
    currentNumberSlide += 1;
    rengerSlide();
    console.log(slidesContainer.scrollLeft + " " + sliderWrapper.offsetWidth);

});


sliderPointer.addEventListener('click', (e) => {
    // Наверное, лучше слушатели повесить сразу на кнопки, НО пока пофиг
    let isChange = false;
    for (i = 0; i < MaxNumberSlide; i++){
        if (sliderPointerChildren[i].querySelector('input').checked){
            lastNumberSlide = currentNumberSlide;
            currentNumberSlide = i;
            isChange = true;
            break;
        };
    };

    if (isChange){
        rengerSlide();
    };

});


