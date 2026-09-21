const menuButton = document.querySelector('.menu-button');
const menu = document.querySelector('#main-nav');
function closeMenu(){if(!menuButton)return;menu.classList.remove('open');menuButton.setAttribute('aria-expanded','false');menuButton.textContent='Menu';}
if(menuButton && menu){
 menuButton.addEventListener('click',()=>{const open=menuButton.getAttribute('aria-expanded')!=='true';menuButton.setAttribute('aria-expanded',String(open));menu.classList.toggle('open',open);menuButton.textContent=open?'Close':'Menu';});
 menu.addEventListener('click',event=>{if(event.target.closest('a'))closeMenu();});
 document.addEventListener('keydown',event=>{if(event.key==='Escape'&&menuButton.getAttribute('aria-expanded')==='true'){closeMenu();menuButton.focus();}});
}
const filterButtons=document.querySelectorAll('[data-filter]');
document.querySelectorAll('a[href="/#projects"], a[href="/#work"]').forEach(link=>link.addEventListener('click',()=>{
 const all=document.querySelector('[data-filter="all"]');
 if(all)all.click();
}));
filterButtons.forEach(button=>button.addEventListener('click',()=>{
 const filter=button.dataset.filter;
 filterButtons.forEach(item=>item.setAttribute('aria-pressed',String(item===button)));
 let count=0;
 document.querySelectorAll('[data-project]').forEach(project=>{const visible=filter==='all'||project.dataset.category.split(' ').includes(filter);project.hidden=!visible;if(visible)count++;});
 const projects=document.querySelector('#projects');
 if(projects)projects.hidden=!Array.from(projects.querySelectorAll('[data-project]')).some(item=>!item.hidden);
 document.querySelector('.filter-count').textContent=`${count} project${count===1?'':'s'} shown`;
}));
