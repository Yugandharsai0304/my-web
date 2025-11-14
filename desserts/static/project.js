// Example interactivity: Alert message when ordering
document.querySelectorAll('.swiggy').forEach(button => {
    button.addEventListener('click', () => {
      alert('Ordering on Swiggy...');
    });
  });
  
  document.querySelectorAll('.zomato').forEach(button => {
    button.addEventListener('click', () => {
      alert('Ordering on Zomato...');
    });
  });


  // Toggle dropdown visibility
document.getElementById('availabilityToggle').addEventListener('click', () => {
    const menu = document.getElementById('availabilityMenu');
    menu.classList.toggle('active');
  });
  // Toggle dropdown visibility
document.getElementById('priceToggle').addEventListener('click', () => {
    const menu = document.getElementById('priceMenu');
    menu.classList.toggle('active');
  });
  
  // Reset selection in dropdown
  document.querySelector('.reset-button').addEventListener('click', () => {
    const checkboxes = document.querySelectorAll('.filter-option');
    checkboxes.forEach(checkbox => checkbox.checked = false);
    alert('Filters reset');
  });
  
  // Close dropdown when clicking outside
  window.addEventListener('click', (event) => {
    const menu = document.getElementById('availabilityMenu');
    const toggle = document.getElementById('availabilityToggle');
    if (!menu.contains(event.target) && event.target !== toggle) {
      menu.classList.remove('active');
    }
    const price = document.getElementById('priceMenu');
    const ptoggle = document.getElementById('priceToggle');
    if (!price.contains(event.target) && event.target !== ptoggle) {
      price.classList.remove('active');
    }
  });

  

  function resetPriceRange() {
    document.getElementById('priceFrom').value = '';
    document.getElementById('priceTo').value = '';
  }
  
