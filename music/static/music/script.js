function editAlbumInfo() {
    const button = document.querySelector('#edit-button')
    let viewCells = document.querySelectorAll('.view-cell')
    let editCells = document.querySelectorAll('.edit-cell')
    const imageUrlCell = document.querySelector('#image-url-cell')
    const updateButton = document.querySelector('#update-info-button')
    if(button.value === 'Edit') {
        button.value = 'View'
        editCells.forEach(function (item) {
            item.style.display = 'table-row'
        })

        viewCells.forEach(function (item) {
            item.style.display = 'none'
        })
        imageUrlCell.style.display = 'table-row'
        updateButton.style.display = 'block'
    } else {
        button.value = 'Edit'
        editCells.forEach(function (item) {
            item.style.display = 'none'
        })

        viewCells.forEach(function (item) {
            item.style.display = 'table-cell'
        })
        imageUrlCell.style.display = 'none'
        updateButton.style.display = 'none'
    }
}

function updateSearchResultImage() {
    const imageUrl = document.getElementById('image_url').value
    const background = document.getElementById('background-image')
    const coverArt = document.getElementById('found-album-cover-art')
    setTimeout(function () {
        background.src = imageUrl
        coverArt.src = imageUrl
    }, 500)
}

function updateAlbumInfoCoverArt() {
    const imageUrl = document.getElementById('cover-art-url').value
    const background = document.getElementById('background-image')
    const coverArt = document.getElementById('album-cover')
    setTimeout(function () {
        background.src = imageUrl
        coverArt.src = imageUrl
    }, 500)
}

function saveNote() {
    const note = document.getElementById('user-note').value
    fetch('http://localhost:5000/music/save-note', {
        headers: {
            "X-Requested-With": 'XMLHttpRequest',
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie('csrftoken'),
        },
        mode: 'cors',
        method: 'POST',
        credentials: "include",
        body: JSON.stringify({'user-note': note})
    })
        .then(response => console.log(response.status))
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function changeInputType() {
    const filterSelect = document.getElementById('filter-select')
    const filterInput = document.getElementById('filter-input')
    if (filterSelect.value === 'release-year') {
        filterInput.type = 'number'
        filterInput.name = 'year'
    } else {
        filterInput.type = 'text'
        filterInput.name = 'release'
    }

}
