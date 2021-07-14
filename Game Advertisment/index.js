const left = document.getElementById('left-flash')
const right = document.getElementById('right-flash')
const img = document.getElementById('image')
const title = document.getElementById('showcase-title')

let imageIndex = 0
const image = ['arma3', 'minecraft', 'red-dead-2']
const titles = ['Arma 3', 'Minecraft', 'Red Dead Redemption 2']

loadImg(image[imageIndex])

function loadImg(Image) {
    img.src = `images/${Image}.png`
    title.textContent = titles[imageIndex]

}

function prevImg() {
    imageIndex--
    if(imageIndex < 0) {
        imageIndex = image.length - 1
    }

    loadImg(image[imageIndex])
}

function nextImg() {
    imageIndex++
    if(imageIndex > image.length - 1) {
        imageIndex = 0
    }

    loadImg(image[imageIndex])

}

left.addEventListener('click', prevImg)
right.addEventListener('click', nextImg)