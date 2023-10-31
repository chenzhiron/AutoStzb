const info = document.getElementById('app')
setTimeout(() => {
	info?.setAttribute('src',  window.proargs.args().webport)
})


