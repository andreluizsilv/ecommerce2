import mercadopago

public_key = "TEST-2cb4e79a-a12f-4286-b708-572b4650e3a6"
token = "TEST-6244779549547304-011715-156e0551b52ade4d706a7687e9c700fb-144516549"


def criar_pagamento(itens_pedido, link_base):
    # Configure as credenciais
    sdk = mercadopago.SDK(token)

    # Crie um item na preferência
    itens = []
    for item in itens_pedido:
        quantidade = int(item.quantidade)
        nome_produto = item.item_estoque.produto.nome
        preco_unitario = float(item.item_estoque.produto.preco)
        itens.append({
            "title": nome_produto,
            "quantity": quantidade,
            "unit_price": preco_unitario,
        })

    # Configurar as URLs de retorno para cada status
    back_urls = {
        "success": f"{link_base}?status=success",
        "pending": f"{link_base}?status=pending",
        "failure": f"{link_base}?status=failure",
    }

    # Dados da preferência de pagamento
    preference_data = {
        "items": itens,
        "auto_return": "all",
        "back_urls": back_urls,
    }

    # Criação da preferência de pagamento
    resposta = sdk.preference().create(preference_data)
    link_pagamento = resposta["response"]["init_point"]
    id_pagamento = resposta["response"]["id"]

    return link_pagamento, id_pagamento
