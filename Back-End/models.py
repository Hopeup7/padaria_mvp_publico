print("Deus, abençoe este meu primeiro sisteminha, pois preciso desta forma para poder cuidar da minha família.")
class Pedido:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

    def __str__(self):
        return f"Pedido: {self.produto}, Quantidade: {self.quantidade}, Valor: {self.valor}"

class Padaria: 
    def __init__(self, nome, endereco): 
        self.nome = nome 
        self.endereco = endereco 
        self.funcionarios = [] 
        self.setores = []  
        self.estoque = {} 
        self.pedidos = [] 

        self.formas_pagamento = ["Dinheiro", "Cartão de Crédito", "Pix"] # formas aceitas de pagamento. 

        self.lucro_diario = 0.0 

        self.lucros_semanais = 0.0
        self.lucro_mensal = 0.0 

    def registrar_pedido(self, pedido: Pedido): 
        print(f"\nPedido: {pedido.produto}\nQuantidade: {pedido.quantidade}\nValor: {pedido.valor}")

        confirmacao = input(f"\nSeu pedido está correto?\nproduto: {pedido.produto}, quantidae: {pedido.quantidade}, valor: {pedido.valor}?\nSe sim, aperte 'Enviar', senão cancele com 'Cancelar'\n\U0001f525 ").strip().upper()

        if confirmacao == 'ENVIAR':
            self.pedidos.append(pedido)

        else:
            print(f"O que gostaria de mudar, Sr.?") 

        self.lucro_diario += pedido.valor

        return f"\nPedido: {pedido.produto}, quantidade: {pedido.quantidade}, valor: {pedido.valor}"

padaria = Padaria("Padaria & Martins", "Rua dos Buenos, 328")  

novo_pedido = Pedido("Coca", 1, 5.00)

print(f"{padaria.registrar_pedido(novo_pedido)}")
print(f"Pedido registrado:")
for pedido in padaria.pedidos:
    print(f"\nEste é o seu pedido:\n{pedido}")