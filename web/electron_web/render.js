const info = document.getElementById('app')
const url = 'http://127.0.0.1:'
setTimeout(() => {
	info?.setAttribute('src', url + window.proargs.args().webport)
})


