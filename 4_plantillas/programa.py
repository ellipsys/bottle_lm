from bottle import Bottle,route,run,request,template
@route('/hello')
@route('/hello/')
@route('/hello/<name>')
def hello(name='Mundo'):
    return template('template_hello.tpl', nombre=name)
@route('/suma/<num1>/<num2>')
def suma(num1,num2):
    return template('template_suma.tpl',numero1=num1,numero2=num2)
@route('/lista')
def lista():
    lista=["Manzana","Platano","Naranja"]
    return template('template_lista',lista=lista)
run(host='0.0.0.0', port=8080)

