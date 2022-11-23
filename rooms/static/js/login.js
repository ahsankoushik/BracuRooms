(function() {
    "use strict"; // Start of use strict
  
    var mainNav = document.querySelector('#mainNav');
  
    if (mainNav) {
  
      // Collapse Navbar
      var collapseNavbar = function() {
  
        var scrollTop = (window.pageYOffset !== undefined) ? window.pageYOffset : (document.documentElement || document.body.parentNode || document.body).scrollTop;
  
        if (scrollTop > 100) {
          mainNav.classList.add("navbar-shrink");
        } else {
          mainNav.classList.remove("navbar-shrink");
        }
      };
      // Collapse now if page is not at top
      collapseNavbar();
      // Collapse the navbar when page is scrolled
      document.addEventListener("scroll", collapseNavbar);
    }
  
  })(); // End of use strict

nav_hider = () =>{
    btn = document.getElementById('logoutbutton')
    btn.innerHTML = `<a id="logoutbutton" class="btn btn-primary shadow" role="button" href="#">Sign Up</a>`
    elements = document.getElementsByClassName('log-b');
    for(i =0; i < elements.length; i++){
        elements[i].style.display = 'none';
    }
}

nav_hider()