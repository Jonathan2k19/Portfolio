/**
 * Lets the mobile nav-menu slide in when pressing mobile menu symbol (burger)
 */
const navSlide = () => {
    window.onload=function(){
        const burger = document.querySelector('.burger');
        const nav = document.querySelector('.nav-links');
        const navLinks = document.querySelectorAll('.nav-links li');
        
        burger.addEventListener('click', () => {
            // toggle nav
            nav.classList.toggle('nav-active');
            // animate links flying in
            navLinks.forEach((link,index) => {
                if (link.style.animation){
                    link.style.animation = '';
                } else {
                    link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.25}s`;
                }
            });
            // burger symbol animation
            burger.classList.toggle('toggle');
        });
    }
}

navSlide();



/**
 * Smooth scroll behavior for sections
 * -> supported cross-platform
 */
$('.nav-links a').on('click', function(e){
    if(this.hash !== ''){
        e.preventDefault();

        const hash = this.hash;

        $('html, body').animate({
            scrollTop: $(hash).offset().top
        }, 800);
    }
});


