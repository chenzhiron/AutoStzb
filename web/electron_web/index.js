const { app, BrowserWindow } = require('electron')
const path = require('path')
const createWindow = () => {
	const win = new BrowserWindow({
		width: 888,
		height: 750,
		resizable: false, // 禁止窗口大小调整
		 webPreferences: {
		  preload: path.join(__dirname, 'preload.js')
		}
	})
	win.setMenu(null)
	win.loadFile('index.html')
}

app.whenReady().then(() => {
	createWindow()
})
