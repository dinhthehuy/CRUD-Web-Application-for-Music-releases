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
