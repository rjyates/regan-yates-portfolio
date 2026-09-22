const menuButton = document.querySelector('.menu-button');
const menu = document.querySelector('#main-nav');
function closeMenu(){if(!menuButton)return;menu.classList.remove('open');menuButton.setAttribute('aria-expanded','false');menuButton.textContent='Menu';}
if(menuButton && menu){
 menuButton.addEventListener('click',()=>{const open=menuButton.getAttribute('aria-expanded')!=='true';menuButton.setAttribute('aria-expanded',String(open));menu.classList.toggle('open',open);menuButton.textContent=open?'Close':'Menu';});
 menu.addEventListener('click',event=>{if(event.target.closest('a'))closeMenu();});
 document.addEventListener('keydown',event=>{if(event.key==='Escape'&&menuButton.getAttribute('aria-expanded')==='true'){closeMenu();menuButton.focus();}});
}
