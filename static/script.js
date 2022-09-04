//animação do código
const item = document.querySelectorAll("[data-anime]");
const animeScroll = () => {
    // a partir de 0.85 a tela pode fazer animação
    const windowTop = window.pageYOffset + window.innerHeight * 0.85 ;
// para cada elemento adiciona e remove a animação
    item.forEach((element) => {
        if (windowTop > element.offsetTop) {
            element.classList.add("animate");
        } else{
            element.classList.remove("animate");
        }
    });
};

animeScroll();

window.addEventListener("scroll", ()=>{
    animeScroll();
})

// animação do botão enviar e do botão enviando
const btnEnviar = document.querySelector('#btn-enviar')
const btnEnviarLoader = document.querySelector('#btn-enviar-loader')

btnEnviar.addEventListener("click",()=>{
    btnEnviarLoader.style.display = "block";
    btnEnviar.style.display = "none"

})
//tempo que o alerta de mensagem enviada fica na tela
setTimeout(()=> {
    document.querySelector('#alerta').style.display = "none"
}, 4000) //em milissegundo