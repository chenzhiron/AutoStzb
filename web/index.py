from bottle import Bottle, route

app = Bottle()



@app.route('/')
def hello():
    return """
    <script>
        function demo(){
            console.log(1234)
        }
    </script>
    <button onclick='demo()'>启动</button>
    <select name="color">
    <option value="1">1</option>
    <option value="2">2</option>
    <option value="3">3</option>
  </select>
  <div>
    <div> 次数 <input></input>
    </div>
 
    """

def app_start(port):
    app.run(host='localhost', port=port,reloader=True)



if __name__ == '__main__':
    app_start(22678)
