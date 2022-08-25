$(document).ready(function(){
    $(window).scroll(function(){
        // sticky navbar on scroll script
        if(this.scrollY > 20){
            $('.navbar').addClass("sticky");
        }else{
            $('.navbar').removeClass("sticky");
        }
        
        // scroll-up button show/hide script
        if(this.scrollY > 500){
            $('.scroll-up-btn').addClass("show");
        }else{
            $('.scroll-up-btn').removeClass("show");
        }
    });

    // slide-up script
    $('.scroll-up-btn').click(function(){
        $('html').animate({scrollTop: 0});
        // removing smooth scroll on slide-up button click
        $('html').css("scrollBehavior", "auto");
    });

    $('.navbar .menu li a').click(function(){
        // applying again smooth scroll on menu items click
        $('html').css("scrollBehavior", "smooth");
    });

    // toggle menu/navbar script
    $('.menu-btn').click(function(){
        $('.navbar .menu').toggleClass("active");
        $('.menu-btn i').toggleClass("active");
    });

    // typing text animation script
    var typed = new Typed(".typing", {
        strings: [ "Full Stack Developer", "Backend Developer"],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });

    var typed = new Typed(".typing-2", {
        strings:[ "Full Stack Developer", "Backend Developer"],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });

    // owl carousel script
    $('.carousel').owlCarousel({
        margin: 20,
        loop: true,
        // autoplay: true,
        // autoplayTimeOut: 2000,
        // autoplayHoverPause: true,
        responsive: {
            0:{
                items: 1,
                nav: false
            },
            // 300:{
            //     items: 2,
            //     nav: false
            // },
            // 1000:{
            //     items: 3,
            //     nav: false
            // }
        }
    });
    var form = document.getElementById("contact-form");
    form.addEventListener("submit", function (event) {
        event.preventDefault();
        var XHR = new XMLHttpRequest();
        var form_data = new FormData(form);

        // on success
        XHR.addEventListener("load", on_success);

        // on error
        XHR.addEventListener("error", on_error);

        // set up request
        XHR.open("POST", "/contact_api");

        // Form data is sent with request
        XHR.send(form_data);

    });

    // function corresponding to success ajax request
    var on_success = function (event) {
        // document.getElementById("loading").style.display = 'none';
        var response = JSON.parse(event.target.responseText);
        if (response.success) {
            alert(response.message);
            form.reset()
            // window.location.href = "index.php";
        } else {
            alert(response.message);
        }
    };

    // function corresponding to unsuccess ajax request
    var on_error = function (event) {
        alert('Oops! Something went wrong.');
    };
})