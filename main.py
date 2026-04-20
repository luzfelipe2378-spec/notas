from flask import Flask, request

app = Flask(__name__)

# Rotas
@app.route('/')
def homepage():
    return 'bem-vindo à homepage, digite "/notas" para começar.'

@app.route('/notas')
def notas():
    nota_str = request.args.get('valor')
    
    if not nota_str:
        return 'Informe a nota assim: /notas?valor=7'
    
    try:
        nota = float(nota_str)
    except ValueError:
        return 'Nota inválida. Use números. Ex: /notas?valor=6.5'
    
    if nota >= 7:
        return 'Apv - Aprovado'
    elif nota >= 5:
        return 'Avf - Avaliação Final'
    elif nota <= 3:
        return 'Rpv - Reprovado'
    else:  
        falta = 5 - nota
        return f'Rpv - Reprovado. Faltou {falta:.1f} pra Avf'

if __name__ == '__main__':
    app.run(debug=True)
