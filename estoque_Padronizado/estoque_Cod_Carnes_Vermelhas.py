print("\n\"Senhor, não deixe faltar o alimento para ninguém, em especial para o meu lar e minha familia. Sei que posso contar Contigo. Obrigado, Senhor.\"\n")

"""📌 O que foi incluído:
✅ Códigos superiores e inferiores: DXXX para produtos principais e TDXXX para variações, com TDXXX.X se necessário
✅ Estrutura clara e rastreável: Marca, embalagem, peso, unidade e vencimento organizados corretamente
✅ Função de exibição para facilitar consultas futuras
✅ Preparação para futura integração com SQLite
Se quiser conferir antes da versão final, posso te apresentar um resumo ou validar ajustes. Seguimos estruturando com excelência!"""

estoque = {
    "Alimentos": {
        "Carnes Vermelhas": [
            {
                "Código": "C001",
                "Marca": "Picanha Maturatta - Friboi",
                "Tipos": [
                    {
                        "Código_Tipo": "TC001",
                        "Tipo_Embalagem": "Pacote Resfriado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 100.00,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C002",
                "Marca": "Filé Mignon Maturatta - Friboi",
                "Tipos": [
                    {
                        "Código_Tipo": "TC002",
                        "Tipo_Embalagem": "Pacote Resfriado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 129.29,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C003",
                "Marca": "Contrafilé - Friboi",
                "Tipos": [
                    {
                        "Código_Tipo": "TC003",
                        "Tipo_Embalagem": "Pacote a Vácuo",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 62.90,
                        "Vencimento": "15/12/2025"
                    }
                ]
            },
            {
                "Código": "C004",
                "Marca": "Acém - Swift",
                "Tipos": [
                    {
                        "Código_Tipo": "TC004",
                        "Tipo_Embalagem": "Pacote a Vácuo",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 37.90,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C005",
                "Marca": "Patinho - Swift",
                "Tipos": [
                    {
                        "Código_Tipo": "TC005",
                        "Tipo_Embalagem": "Pacote a Vácuo",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 49.90,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C006",
                "Marca": "Costela Bovina - Swift",
                "Tipos": [
                    {
                        "Código_Tipo": "TC006",
                        "Tipo_Embalagem": "Pacote Resfriado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 54.90,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C007",
                "Marca": "Coxão Duro - Swift",
                "Tipos": [
                    {
                        "Código_Tipo": "TC007",
                        "Tipo_Embalagem": "Pacote Resfriado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 48.99,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C008",
                "Marca": "Hamburguer - Friboi",
                "Tipos": [
                    {
                        "Código_Tipo": "TC008",
                        "Tipo_Embalagem": "Caixa Congelada",
                        "Volume": 4,
                        "Unidade": "kg",
                        "Quantidade_Total": 1,
                        "Preço_Unitário": 130.99,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C009",
                "Marca": "Carne Moída - Swift",
                "Tipos": [
                    {
                        "Código_Tipo": "TC009",
                        "Tipo_Embalagem": "Pacote Congelado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 38.99,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C010",
                "Marca": "Mocóto Bovino - Swift",
                "Tipos": [
                    {
                        "Código_Tipo": "TC010",
                        "Tipo_Embalagem": "Pacote Congelado",
                        "Volume": 1.3,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 18.99,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C011",
                "Marca": "Carne Seca - Swift",
                "Tipos": [
                    {
                        "Código_Tipo": "TC011",
                        "Tipo_Embalagem": "Pacote a Vácuo",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 55.99,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
        ],
        "Carnes Suínas": [
            {
                "Código": "C012",
                "Marca": "Bisteca Suína - Swift",
                "Tipos": [
                    {
                        "Código_Tipo": "TC012",
                        "Tipo_Embalagem": "Pacote Resfriado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 23.99,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C013",
                "Marca": "Pernil Suíno - Swift",
                "Tipos": [
                    {
                        "Código_Tipo": "TC013",
                        "Tipo_Embalagem": "Pacote Resfriado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 25.99,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C014",
                "Marca": "Lombo Suíno - Swift",
                "Tipos": [
                    {
                        "Código_Tipo": "TC014",
                        "Tipo_Embalagem": "Pacote Resfriado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 29.99,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C015",
                "Marca": "Costelinha Suína - Swift",
                "Tipos": [
                    {
                        "Código_Tipo": "TC015",
                        "Tipo_Embalagem": "Pacote Resfriado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 27.99,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C016",
                "Marca": "Torresmo - Porco Feliz",
                "Tipos": [
                    {
                        "Código_Tipo": "TC016",
                        "Tipo_Embalagem": "Pacote Resfriado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 14.99,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C017",
                "Marca": "Pé de Porco - Porco Feliz",
                "Tipos": [
                    {
                        "Código_Tipo": "TC017",
                        "Tipo_Embalagem": "Pacote Resfriado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 12.99,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C018",
                "Marca": "Orelha de Porco - Porco Feliz",
                "Tipos": [
                    {
                        "Código_Tipo": "TC018",
                        "Tipo_Embalagem": "Pacote Resfriado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 14.89,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C019",
                "Marca": "Rabo de Porco - Porco Feliz",
                "Tipos": [
                    {
                        "Código_Tipo": "TC019",
                        "Tipo_Embalagem": "Pacote Resfriado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 13.59,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
        ],
        "Aves": [
            {
                "Código": "C020",
                "Marca": "Peito de Frango - Sadia",
                "Tipos": [
                    {
                        "Código_Tipo": "TC020",
                        "Tipo_Embalagem": "Pacote Resfriado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 25.99,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C021",
                "Marca": "Coxa e Sobrecoxa - Sadia",
                "Tipos": [
                    {
                        "Código_Tipo": "TC021",
                        "Tipo_Embalagem": "Pacote Resfriado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 16.99,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C022",
                "Marca": "Frango Inteiro - Perdigão",
                "Tipos": [
                    {
                        "Código_Tipo": "TC022",
                        "Tipo_Embalagem": "Pacote Congelado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 13.00,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C023",
                "Marca": "Frango a Passarinho - Swift",
                "Tipos": [
                    {
                        "Código_Tipo": "TC023",
                        "Tipo_Embalagem": "Pacote Congelado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 14.90,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C024",
                "Marca": "Frango Desfiado - Sadia",
                "Tipos": [
                    {
                        "Código_Tipo": "TC024",
                        "Tipo_Embalagem": "Pacote Resfriado",
                        "Volume": 400,
                        "Unidade": "g",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 22.89,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C025",
                "Marca": "Peito de Peru(Fresco) - Perdigão",
                "Tipos": [
                    {
                        "Código_Tipo": "TC025",
                        "Tipo_Embalagem": "Pacote Resfriado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 20.00,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C026",
                "Marca": "Chester - Perdigão",
                "Tipos": [
                    {
                        "Código_Tipo": "TC026",
                        "Tipo_Embalagem": "Pacote Resfriado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 6,
                        "Preço_Unitário": 30.00,
                        "Vencimento": "12/12/2025"
                    }
                ]
            }
        ],
        "Peixes e Frutos do Mar": [
            {
                "Código": "C027",
                "Marca": "Filé de Tilápia - Swift",
                "Tipos": [
                    {
                        "Código_Tipo": "TC027",
                        "Tipo_Embalagem": "Pacote a Vácuo",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 59.90,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C030",
                "Marca": "Filé de Merluza - Swift",
                "Tipos": [
                    {
                        "Código_Tipo": "TC030",
                        "Tipo_Embalagem": "Pacote a Vácuo",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 59.90,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C028",
                "Marca": "Filé de Salmão - Swift",
                "Tipos": [
                    {
                        "Código_Tipo": "TC028",
                        "Tipo_Embalagem": "Porcionado",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 89.00,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "C029",
                "Marca": "Camarão Descascado - Swift",
                "Tipos": [
                    {
                        "Código_Tipo": "TC029",
                        "Tipo_Embalagem": "Pacote Congelado",
                        "Volume": 400,
                        "Unidade": "g",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 36.00,
                        "Vencimento": "12/12/2025"
                    }
                ]
            }
        ]
    }
}


def estoque_Carnes():
    """Aqui eu crio uma função que itera no dict com list atraves de for acessando suas propriedades."""
    for categoria, carnes in estoque['Alimentos'].items():
        print(f"\n\U0001f969  ► Categoria: {categoria} ◄\n")

        for carne in carnes:
            print(
                f"\U0001f525 Código do Produto: {carne['Código']}\n\U0001f7e2 {carne['Marca']}")

            for tipo in carne['Tipos']:
                print(f"\U0001f535 - {tipo['Tipo_Embalagem']} ({tipo['Volume']} {tipo['Unidade']}) \n"

                      f"Quantidade: {tipo['Quantidade_Total']} |Vencimento: {tipo['Vencimento']}\n"

                      f"--> \U0001f4b0 Preço: R$ {tipo['Preço_Unitário']: .2f} <--\n" + "*" * 40 if tipo['Preço_Unitário'] else
                      "\n\U0001f7e2 Preço: Não Informado.")


estoque_Carnes()
