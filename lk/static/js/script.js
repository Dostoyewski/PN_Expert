let unassignedButtons = document.querySelectorAll('.unassigned');

for (let each of unassignedButtons) {
    each.addEventListener('mousedown', e => {
        M.toast({html: 'Ой, но это пока не готово!'})
    })
}
