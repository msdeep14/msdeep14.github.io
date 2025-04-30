document.addEventListener('DOMContentLoaded', function() {
  let slideIndex = 0;
  const slides = document.querySelector('.giveaway-slides');
  const slideItems = document.querySelectorAll('.giveaway-slide');
  const totalSlides = slideItems.length;

  // Set initial position
  updateSlidePosition();

  // Add event listeners to buttons
  document.querySelector('.giveaway-prev').addEventListener('click', function() {
    slideIndex = (slideIndex - 1 + totalSlides) % totalSlides;
    updateSlidePosition();
  });

  document.querySelector('.giveaway-next').addEventListener('click', function() {
    slideIndex = (slideIndex + 1) % totalSlides;
    updateSlidePosition();
  });

  // Auto slide every 4 seconds
  setInterval(function() {
    slideIndex = (slideIndex + 1) % totalSlides;
    updateSlidePosition();
  }, 4000);

  function updateSlidePosition() {
    slides.style.transform = 'translateX(-' + (slideIndex * 100) + '%)';
  }
});