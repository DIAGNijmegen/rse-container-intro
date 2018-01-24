from sanic import Sanic
from sanic.response import html

app = Sanic()

@app.route('/')
async def home(request):
    return html('<h1>Welcome to cube-as-a-service</h1>')

@app.route('/<i:number>')
async def cube(request, i):
    return html(f'<h1>{i} cubed is {i ** 3}</h1>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

