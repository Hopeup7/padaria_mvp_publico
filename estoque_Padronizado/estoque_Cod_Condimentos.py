print("Senhor, leve a mim e a minha família até o Senhor, pois em Ti e Contigo seremos abundadntes em vida.")
"""📌 O que foi incluído:
✅ Códigos superiores e inferiores: DXXX para produtos principais e TDXXX para variações, com TDXXX.X se necessário
✅ Estrutura clara e rastreável: Marca, embalagem, peso, unidade e vencimento organizados corretamente
✅ Função de exibição para facilitar consultas futuras
✅ Preparação para futura integração com SQLite
Se quiser conferir antes da versão final, posso te apresentar um resumo ou validar ajustes. Seguimos estruturando com excelência!
"""

estoque = {
    "Alimentos": {
        "Condimentos - Açucares e Cafés": [
            {
                "Código": "Cd001",
                "Marca": "Café em Pó - Pilão",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd001",
                        "Tipo_Embalagem": "Pacote",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 39.90,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd002",
                "Marca": "Café Solúvel - Nescafé",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd002",
                        "Tipo_Embalagem": "Pote Plástico",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 2,
                        "Preço_Unitário": 89.90,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd003",
                "Marca": "Açucar Refinado - União",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd003",
                        "Tipo_Embalagem": "Pacote",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 11.90,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd004",
                "Marca": "Açucar Mascavo - Madoxx Natural",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd004",
                        "Tipo_Embalagem": "Pacote",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 2,
                        "Preço_Unitário": 11.90,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd005",
                "Marca": "Açucar Cristal - União",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd005",
                        "Tipo_Embalagem": "Pacote",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 6.49,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd006",
                "Marca": "Adoçante Dietético(Sachês) -Finn",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd006",
                        "Tipo_Embalagem": "Caixa",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 400,
                        "Preço_Unitário": 6.49,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd007",
                "Marca": "Adoçante Líquido - Zero Cal",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd007",
                        "Tipo_Embalagem": "Frasco",
                        "Volume": 100,
                        "Unidade": "ml",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 20.99,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd008",
                "Marca": "Adoçante Líquido - Adocyl",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd008",
                        "Tipo_Embalagem": "Frasco",
                        "Volume": 200,
                        "Unidade": "ml",
                        "Quantidade_Total": 2,
                        "Preço_Unitário": 9.37,
                        "Vencimento": "12/12/2025"
                    }
                ]
            }
        ],
        "Condimentos - Óleos e Azeites": [
            {
                "Código": "Cd009",
                "Marca": "Óleo de Soja - Liza",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd009",
                        "Tipo_Embalagem": "Garrafa Pet",
                        "Volume": 1,
                        "Unidade": "L",
                        "Quantidade_Total": 24,
                        "Preço_Unitário": 9.98,
                        "Vencimento": "12/12/2025"
                    },
                    {
                        "Código_Tipo": "TCd009.1",
                        "Tipo_Embalagem": "Latão",
                        "Volume": 18,
                        "Unidade": "L",
                        "Quantidade_Total": 1,
                        "Preço_Unitário": 448.58,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd010",
                "Marca": "Óleo de Girassol - Liza",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd010",
                        "Tipo_Embalagem": "Garrafa Pet",
                        "Volume": 1,
                        "Unidade": "L",
                        "Quantidade_Total": 24,
                        "Preço_Unitário": 25.71,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd011",
                "Marca": "Azeite de Oliva Extra Virgem - Gallo",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd011",
                        "Tipo_Embalagem": "Garrafa de Vidro",
                        "Volume": 1,
                        "Unidade": "L",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 139.98,
                        "Vencimento": "12/12/2025"
                    },
                    {
                        "Código_Tipo": "TCd011.1",
                        "Tipo_Embalagem": "Galão",
                        "Volume": 5,
                        "Unidade": "L",
                        "Quantidade_Total": 1,
                        "Preço_Unitário": 385.77,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd012",
                "Marca": "Azeite de Dendê - Arrifan",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd012",
                        "Tipo_Embalagem": "Garrafa Pet",
                        "Volume": 1,
                        "Unidade": "L",
                        "Quantidade_Total": 2,
                        "Preço_Unitário": 15.98,
                        "Vencimento": "12/12/2025"
                    }
                ]
            }
        ],
        "Condimentos - Temperos Secos": [
            {
                "Código": "Cd013",
                "Marca": "Sal Refinado - Cisne",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd013",
                        "Tipo_Embalagem": "Pacote",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 3.49,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd014",
                "Marca": "Sal Grosso - Lebre",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd014",
                        "Tipo_Embalagem": "Pacote",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 2.49,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd015",
                "Marca": "Pimenta do Reino - Cantagallo",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd015",
                        "Tipo_Embalagem": "Pacote",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 66.50,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd016",
                "Marca": "Páprica Picante - Premium",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd016",
                        "Tipo_Embalagem": "Pacote",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 36.60,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd017",
                "Marca": "Oregano Desidratado - Peruano",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd017",
                        "Tipo_Embalagem": "Pacote",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 30.95,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd018",
                "Marca": "Alecrim Seco - Niyati",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd018",
                        "Tipo_Embalagem": "Pacote",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 26.98,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd019",
                "Marca": "Alho em Pó - Premium",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd019",
                        "Tipo_Embalagem": "Pacote",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 34.90,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd020",
                "Marca": "Cebola Desidratada - Premium",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd020",
                        "Tipo_Embalagem": "Pacote",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 52.80,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd021",
                "Marca": "Chimichurri - Original",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd021",
                        "Tipo_Embalagem": "Pacote",
                        "Volume": 1,
                        "Unidade": "kg",
                        "Quantidade_Total": 5,
                        "Preço_Unitário": 65.45,
                        "Vencimento": "12/12/2025"
                    }
                ]
            }
        ],
        "Condimentos - Vinagres e Conservantes": [
            {
                "Código": "Cd022",
                "Marca": "Vinagre de Álcool - Castelo",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd022",
                        "Tipo_Embalagem": "Garrafa Pet",
                        "Volume": 1,
                        "Unidade": "L",
                        "Quantidade_Total": 15,
                        "Preço_Unitário": 17.39,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd023",
                "Marca": "Vinagre Balsâmico Tradicional - Castelo",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd023",
                        "Tipo_Embalagem": "Garrafa de Vidro",
                        "Volume": 1,
                        "Unidade": "L",
                        "Quantidade_Total": 10,
                        "Preço_Unitário": 17.26,
                        "Vencimento": "12/12/2025"
                    }
                ]
            }
        ],
        "Condimentos - Molhos": [
            {
                "Código": "Cd024",
                "Marca": "Molho de Tomate Tradicional - Heinz",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd024",
                        "Tipo_Embalagem": "Pouch Flexível",
                        "Volume": 5,
                        "Unidade": "kg",
                        "Quantidade_Total": 1,
                        "Preço_Unitário": 62.45,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd025",
                "Marca": "Molho Barbecue Original - Heinz",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd025",
                        "Tipo_Embalagem": "Squeeze Plástico",
                        "Volume": 5,
                        "Unidade": "kg",
                        "Quantidade_Total": 1,
                        "Preço_Unitário": 299.75,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd026",
                "Marca": "Molho Shoyu Tradicional - Sakura",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd026",
                        "Tipo_Embalagem": "Garrafa Pet",
                        "Volume": 5,
                        "Unidade": "L",
                        "Quantidade_Total": 1,
                        "Preço_Unitário": 143.90,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd027",
                "Marca": "Molho Madeira ao Vinho - Elegé",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd027",
                        "Tipo_Embalagem": "Caixa",
                        "Volume": 5,
                        "Unidade": "kg",
                        "Quantidade_Total": 1,
                        "Preço_Unitário": 107.00,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd028",
                "Marca": "Molho Pimenta-Vermelha Original - Tabasco",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd028",
                        "Tipo_Embalagem": "Vidro",
                        "Volume": 5,
                        "Unidade": "kg",
                        "Quantidade_Total": 1,
                        "Preço_Unitário": 1915.00,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd029",
                "Marca": "Molho Inglês Worcester Shire - Kenko",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd029",
                        "Tipo_Embalagem": "Garrafa Pet",
                        "Volume": 5,
                        "Unidade": "L",
                        "Quantidade_Total": 1,
                        "Preço_Unitário": 54.50,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd030",
                "Marca": "Mostarda Tradicional - Heinz",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd030",
                        "Tipo_Embalagem": "Pouch Flexível",
                        "Volume": 5,
                        "Unidade": "kg",
                        "Quantidade_Total": 1,
                        "Preço_Unitário": 89.90,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd031",
                "Marca": "Ketchup Tradicional - Heinz",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd031",
                        "Tipo_Embalagem": "Pouch Flexível",
                        "Volume": 5,
                        "Unidade": "kg",
                        "Quantidade_Total": 1,
                        "Preço_Unitário": 79.90,
                        "Vencimento": "12/12/2025"
                    }
                ]
            },
            {
                "Código": "Cd032",
                "Marca": "Maionese Tradicional - Hellman`s",
                "Tipos": [
                    {
                        "Código_Tipo": "TCd032",
                        "Tipo_Embalagem": "Balde Plástico",
                        "Volume": 5,
                        "Unidade": "kg",
                        "Quantidade_Total": 1,
                        "Preço_Unitário": 265.39,
                        "Vencimento": "12/12/2025"
                    }
                ]
            }
        ]
    }
}

def estoque_Condimentos():
    """aqui eu crio uma função que retornará um loop que percorrerá todo o estoque"""
    for categoria, condimentos in estoque['Alimentos'].items():
        print(f"\n\U0001f525 ► Categoria: {categoria} ◄ ")

        for condimento in condimentos:
            print(
                f"\n\U0001f525 Código do Produto: {condimento['Código']}\n\U0001f7e2 {condimento['Marca']}")

            for tipo in condimento['Tipos']:
                print(f"\U0001f535 - {tipo['Tipo_Embalagem']} ({tipo['Volume']} {tipo['Unidade']})\n"

                      f"Quantidade: {tipo['Quantidade_Total']} | Vencimento: {tipo['Vencimento']}\n"

                      f"--> \U0001f4b0 Preço: R$ {tipo['Preço_Unitário']: .2f} <--\n******************************************\n" if tipo['Preço_Unitário'] else "\n \U0001f7e2 Preço: Não Informado.\n*************************")


estoque_Condimentos()
