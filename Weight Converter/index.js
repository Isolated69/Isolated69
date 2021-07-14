let input = document.getElementById('gramsIn')
const btn = document.getElementById('random')
const resetBtn = document.getElementById('reset')

let oz = document.getElementById('ouncesOut')
let kg = document.getElementById('kiloOut')
let lbs = document.getElementById('poundsOut')

w = [' kg', ' oz', ' lbs']

input.addEventListener('input', function(e){
	let grams = e.target.value
	oz.innerHTML = (grams / 28.35).toFixed(2) + w[1]
	kg.innerHTML = (grams / 1000).toFixed(2) + w[0]
	lbs.innerHTML = (grams / 454).toFixed(2) + w[2]	

})

btn.addEventListener('click', function(e){
	let grams = Math.floor(Math.random() * 10000000000)
	input.value = grams
	oz.innerHTML = (grams / 28.35).toFixed(2) + w[1]
	kg.innerHTML = (grams / 1000).toFixed(2) + w[0]
	lbs.innerHTML = (grams / 454).toFixed(2) + w[2]	
})

resetBtn.addEventListener('click', function(e){
	let grams = 0
	input.value = grams.toFixed(2)
	oz.innerHTML = grams.toFixed(2) + w[1]
	kg.innerHTML = grams.toFixed(2) + w[0]
	lbs.innerHTML = grams.toFixed(2) + w[2]	
})
