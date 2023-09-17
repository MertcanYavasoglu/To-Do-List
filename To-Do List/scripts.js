const mainBtn = document.querySelector('.addContainerBtn');
const mainContainer = document.querySelector('.Container')

mainBtn.addEventListener('click', () => {
    const clonedContainer = mainContainer.cloneNode(true);
    mainContainer.insertAdjacentElement('afterend', clonedContainer);
})