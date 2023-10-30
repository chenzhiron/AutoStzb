const { contextBridge, ipcRenderer } = require('electron')

const data = {}
ipcRenderer.on('process-args', (event, args) => {
  data.args = args
});

contextBridge.exposeInMainWorld('proargs', {
  args: () => data.args
})
