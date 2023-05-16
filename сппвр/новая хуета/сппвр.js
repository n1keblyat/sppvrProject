var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("hs").style.top = "0";
  } else {
    document.getElementById("hs").style.top = "-200px";
  }
  prevScrollpos = currentScrollPos;}