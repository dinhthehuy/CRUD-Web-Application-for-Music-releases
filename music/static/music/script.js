function hideListItems() {
    const button = document.querySelector('#EditView')
    let listItems = document.querySelectorAll('li');
    if(button.value === 'Edit') {
        listItems.forEach(function(item) {
            item.style.display = 'none';
        });
        button.value = 'View'
    } else {
        listItems.forEach(function(item) {
            item.style.display = 'block';
        });
        button.value = 'Edit'
    }

}