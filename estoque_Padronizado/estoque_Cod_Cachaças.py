print("\nSenhor, faça-me sorrir em extrema Alegria de Ser Somente Seu. É bom ser Feliz, Senhor? Sei que a Felicidade é Cristo, por isso, Jesus, esteja e sempre permaneça em mim através de Teu Espírito Santo que me ajuda seguir o Teu Caminho que certamente leva a Deus, o Pai, nosso Pai.")

"""📌 O que foi incluído:
✅ Códigos superiores e inferiores: DXXX para produtos principais e TDXXX para variações, com TDXXX.X se necessário
✅ Estrutura clara e rastreável: Marca, embalagem, peso, unidade e vencimento organizados corretamente
✅ Função de exibição para facilitar consultas futuras
✅ Preparação para futura integração com SQLite
Se quiser conferir antes da versão final, posso te apresentar um resumo ou validar ajustes. Seguimos estruturando com excelência!
"""

estoque = {
    "Bebidas": {
        "Cachaças": [
            {
                "Código": "Ch001",
                "Marca": "Cachaça 51",
                "Tipos": [
                    {
                        "Código_Tipo": "TCh001",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 965,
                        "Unidade": "ml",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 30.00,
                        "Vencimento": "01/12/2025"

                    },
                    {
                        "Código_Tipo": "TCh001.1",
                        "Tipo_Embalagem": "Lata",
                        "Volume": 350,
                        "Unidade": "ml",
                        "Quantidade_Total": 24,
                        "Preço_Unitário": 5.00,
                        "Vencimento": "01/12/2025"

                    }
                ]
            },
            {
                "Código": "Ch002",
                "Marca": "Cachaça 51 Ice 3 Limões Zero",
                "Tipos": [
                    {
                        "Código_Tipo": "TCh002",
                        "Tipo_Embalagem": "Lata",
                        "Volume": 275,
                        "Unidade": "ml",
                        "Quantidade_Total": 12,
                        "Preço_Unitário": 8.33,
                        "Vencimento": "01/12/2025"

                    }
                ]
            },
            {
                "Código": "Ch003",
                "Marca": "Cachaça 51 - Mel e Limão",
                "Tipos": [
                    {
                        "Código_Tipo": "TCh003",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 740,
                        "Unidade": "ml",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 23.74,
                        "Vencimento": "01/12/2025"

                    }
                ]
            },
            {
                "Código": "Ch004",
                "Marca": "Cachaça 51 Ouro",
                "Tipos": [
                    {
                        "Código_Tipo": "TCh004",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 965,
                        "Unidade": "ml",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 16.06,
                        "Vencimento": "01/12/2025"

                    }
                ]
            },
            {
                "Código": "Ch005",
                "Marca": "Cachaça Velho Barreiro",
                "Tipos": [
                    {
                        "Código_Tipo": "TCh005",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 910,
                        "Unidade": "ml",
                        "Quantidade_Total": 15,
                        "Preço_Unitário": 30.00,
                        "Vencimento": "01/12/2025"

                    },
                ]
            },
            {
                "Código": "Ch006",
                "Marca": "Cachaça Kariri",
                "Tipos": [
                    {
                        "Código_Tipo": "TCh006",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 960,
                        "Unidade": "ml",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 40.00,
                        "Vencimento": "01/12/2025"

                    }
                ]
            },
            {
                "Código": "Ch007",
                "Marca": "Cachaça Ypióca",
                "Tipos": [
                    {
                        "Código_Tipo": "TCh007",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 965,
                        "Unidade": "ml",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 60,
                        "Vencimento": "01/12/2025"

                    }
                ]
            },
            {
                "Código": "Ch008",
                "Marca": "Cachaça Seleta",
                "Tipos": [
                    {
                        "Código_Tipo": "TCh008",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 700,
                        "Unidade": "ml",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 60,
                        "Vencimento": "01/12/2025"

                    }
                ]
            },
            {
                "Código": "Ch009",
                "Marca": "Cachaça Salinas",
                "Tipos": [
                    {
                        "Código_Tipo": "TCh009",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 700,
                        "Unidade": "ml",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 63.00,
                        "Vencimento": "01/12/2025"

                    }
                ]
            },
            {
                "Código": "Ch010",
                "Marca": "Contini",
                "Tipos": [
                    {
                        "Código_Tipo": "TCh010",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 900,
                        "Unidade": "ml",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 40.00,
                        "Vencimento": "01/12/2025"

                    }
                ]
            },
            {
                "Código": "Ch011",
                "Marca": "Conhaque Dreher",
                "Tipos": [
                    {
                        "Código_Tipo": "TCh011",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 900,
                        "Unidade": "ml",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 20.00,
                        "Vencimento": "01/12/2025"

                    }
                ]
            },
            {
                "Código": "Ch012",
                "Marca": "Corote - Do Barril",
                "Tipos": [
                    {
                        "Código_Tipo": "TCh012",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 500,
                        "Unidade": "ml",
                        "Quantidade_Total": 30,
                        "Preço_Unitário": 4.00,
                        "Vencimento": "01/12/2025"

                    }
                ]
            },
            {
                "Código": "Ch013",
                "Marca": "Corote - Do Barril Sabores",
                "Tipos": [
                    {
                        "Código_Tipo": "TCh013",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 500,
                        "Unidade": "ml",
                        "Quantidade_Total": 30,
                        "Preço_Unitário": 4.00,
                        "Vencimento": "01/12/2025"

                    },
                ]
            }
        ]
    }
}


def estoque_Cachaça():
    """Aqui se cria uma função que tem por objetivo iterar com for sobre o dicionario percorrendo sua estrutura que contem outros dicts e list."""
    for categoria, cachacas in estoque['Bebidas'].items():
        print(f"\n\U0001f943 ► Categoria: {categoria} ◄")

        for pinga in cachacas:
            print(
                f"\n\U0001f525 Código do Produto: {pinga['Código']}\n\U0001f7e2 {pinga['Marca']}")

            for tipo in pinga['Tipos']:
                print(f"\U0001f535 - {tipo['Tipo_Embalagem']} ({tipo['Volume']} {tipo['Unidade']})\n"

                      f"Quantidade: {tipo['Quantidade_Total']} | Vencimento: {tipo['Vencimento']}\n"

                      f"--> \U0001f4b0 Preço: R$ {tipo['Preço_Unitário']: .2f} <--\n" + "*" * 40 + "\n"if tipo['Preço_Unitário'] else "\n\U0001f7e2 Preço: Não Informado.\n")


estoque_Cachaça()
