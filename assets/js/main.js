// Mobile menu + current year. That's all the JS the site needs.
document.addEventListener('DOMContentLoaded',()=>{
  const b=document.querySelector('.menu-btn'),m=document.getElementById('menu')||document.querySelector('.nav > ul');
  if(b&&m)b.addEventListener('click',()=>{const o=m.classList.toggle('open');b.setAttribute('aria-expanded',o)});
  document.querySelectorAll('[data-year]').forEach(e=>e.textContent=new Date().getFullYear());
});
