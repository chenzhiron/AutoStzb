import { readFileSync } from 'fs'

export default  function read_task(path) {
    const jsonData = readFileSync(path, 'utf-8')
    const data = JSON.parse(jsonData)
    return data
}