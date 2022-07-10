// Scroll to top
const scrollBtn = document.querySelector('.scroll-top');

window.onscroll = function() {
  scrollFunction()
}

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    scrollBtn.style.display = 'block';
  } else {
    scrollBtn.style.display = 'none';
  }
}

scrollBtn.addEventListener('click', function() {
  window.scrollTo(0, 0);
})