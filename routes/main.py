from flask import Blueprint, render_template, request,jsonify
from database.inventory_db import INVENTARIO

inventario_route = Blueprint('inventario', __name__)



@inventario_route.route('/')
def listar_inventario():
    # listar itens
    return render_template('inventory.html', inventario = INVENTARIO)



@inventario_route.route('/', methods=['POST'])
def inserir_item_inventario():
    # Inserir dados do item
    data = request.json
    
    # Criar novo item
    novo_item = { 
        "id": len(INVENTARIO) + 1,  # Gera um ID único
        "nome": data['nome'],        # Nome do recurso
        "tipo": data['tipo'],        # Tipo do recurso
    }

    # Adiciona o novo item ao inventário
    INVENTARIO.append(novo_item)

    # Renderiza o template para exibir o item adicionado e o inventário
    return render_template('item_inventario.html', item=novo_item, inventario=INVENTARIO)



@inventario_route.route('/new_item')
def form_new_item():
    # Formulário para cadastrar item
    return render_template('form_new_item.html') 



# @inventario_route.route('/<int:item_id>')
# def detalhe_item(item_id):
#     # detalhar item especifico
#     return render_template('detail_item.html')

@inventario_route.route('/<int:item_id>/edit')
def edit_item(item_id):
   # editar item
    item = None
    for c in INVENTARIO:
        if c['id'] == item_id:
            item = c

    return render_template('form_new_item.html', item = item)

@inventario_route.route('/<int:item_id>/update', methods = ['PUT'])
def atualizar_item(item_id):
    # atualizar item
    item_editado = None
    data = request.json
    for c in INVENTARIO:
        if c['id'] == item_id:
            c['nome'] = data['nome']
            c['tipo'] = data['tipo']
            item_editado = c
    return render_template('item_inventario.html', item = item_editado)

@inventario_route.route('/<int:item_id>/delete', methods= ['DELETE'])
def deletar_item(item_id):
    # deletar item
    global INVENTARIO
    INVENTARIO = [ c for c in INVENTARIO if c['id'] != item_id ]

    return {'deleted': 'ok'}