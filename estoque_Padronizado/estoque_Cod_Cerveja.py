print("\n -->  Deus, cuide de meu sisteminha, para que a partir deste, grandes projetos possam surgir, Meu Senhor!!!  <--")


"""📌 O que foi incluído:
✅ Códigos superiores e inferiores: DXXX para produtos principais e TDXXX para variações, com TDXXX.X se necessário
✅ Estrutura clara e rastreável: Marca, embalagem, peso, unidade e vencimento organizados corretamente
✅ Função de exibição para facilitar consultas futuras
✅ Preparação para futura integração com SQLite
Se quiser conferir antes da versão final, posso te apresentar um resumo ou validar ajustes. Seguimos estruturando com excelência!
"""
estoque = {
    "Bebidas": {
        "Cervejas": [
            {
                "Código": "CJ001",
                "Marca": "Skol",
                "Tipos": [
                    {
                        "Código_Tipo": "TCJ001",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 600,
                        "Unidade": "ml",
                        "Quantidade_Total": 72,
                        "Preço_Unitário": 12.00,
                        "Vencimento": "22/11/2025"
                    },

                    {
                        "Código_Tipo": "TCJ001.1",
                        "Tipo_Embalagem": "Lata",
                        "Volume": 350,
                        "Unidade": "ml",
                        "Quantidade_Total": 36,
                        "Preço_Unitário": 5.00,
                        "Vencimento": "22/08/2025"
                    },

                    {   
                        "Código_Tipo": "TCJ001.2",  
                        "Tipo_Embalagem": "Latão",
                        "Volume": 473,
                        "Unidade": "ml",
                        "Quantidade_Total": 36,
                        "Preço_Unitário": 8.00,
                        "Vencimento": "22/10/2025"
                    }
                ]
            },
            {
                "Código": "CJ002",
                "Marca": "Skol Beats Senses",
                "Tipos": [
                    {
                        "Código_Tipo": "TCJ002",
                        "Tipo_Embalagem": "Long Neck", 
                        "Volume": 269, 
                        "Unidade": "ml", 
                        "Quantidade_Total": 12, 
                        "Preço_Unitário": 8.00, 
                        "Vencimento": "17/08/2025"
                    }                   
                ]
            },
            {
                "Código": "CJ003",
                "Marca": "Skol Beats Secret",
                "Tipos": [
                    {
                        "Código_Tipo": "TCJ003",
                        "Tipo_Embalagem": "Long Neck", 
                        "Volume": 269, 
                        "Unidade": "ml", 
                        "Quantidade_Total": 12, 
                        "Preço_Unitário": 8.00, 
                        "Vencimento": "17/08/2025"
                    }                   
                ]
            },              
            {
                "Código": "CJ004",
                "Marca": "Brahma",
                "Tipos": [
                    {
                        "Código_Tipo": "TCJ004",    
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 600,
                        "Unidade": "ml",
                        "Quantidade_Total": 72,
                        "Preço_Unitário": 12.00,
                        "Vencimento": "10/12/2025"
                    },
                    

                    {
                        "Código_Tipo": "TCJ004.1",
                        "Tipo_Embalagem": "Lata",
                        "Volume": 350,
                        "Unidade": "ml",
                        "Quantidade_Total": 36,
                        "Preço_Unitário": 5.00,
                        "Vencimento": "12/10/2025"
                    },

                    {
                        "Código_Tipo": "TCJ004.2",
                        "Tipo_Embalagem": "Latão",
                        "Volume": 473,
                        "Unidade": "ml",
                        "Quantidade_Total": 36,
                        "Preço_Unitário": 8.00,
                        "Vencimento": "13/12/2025"
                    }
                ]
            },
            {
                "Código": "CJ005",
                "Marca": "Brahma MalzBier",
                "Tipos": [
                    {
                        "Código_Tipo": "TCJ005",
                        "Tipo_Embalagem": "Long Neck", 
                        "Volume": 330, 
                        "Unidade": "ml", 
                        "Quantidade_Total": 72, 
                        "Preço_Unitário": 8.00, 
                        "Vencimento": "17/08/2025"
                    }                   
                ]
            },
            {
                "Código": "CJ006",
                "Marca": "Heinekken",
                "Tipos": [
                    {
                        "Código_Tipo": "TCJ006",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 600,
                        "Unidade": "ml",
                        "Quantidade_Total": 72,
                        "Preço_Unitário": 12.00,
                        "Vencimento": "10/12/2025"
                    },

                    {
                        "Código_Tipo": "TCJ006.1",
                        "Tipo_Embalagem": "Lata",
                        "Volume": 350,
                        "Unidade": "ml",
                        "Quantidade_Total": 36,
                        "Preço_Unitário": 5.00,
                        "Vencimento": "12/10/2025"
                    },
                    
                    {
                        "Código_Tipo": "TCJ006.2",
                        "Tipo_Embalagem": "Long Neck",
                        "Volume": 330,
                        "Unidade": "ml",
                        "Quantidade_Total": 36,
                        "Preço_Unitário": 8.00,
                        "Vencimento": "12/10/2025"
                    },

                    {
                        "Código_Tipo": "TCJ006.3",
                        "Tipo_Embalagem": "Latão",
                        "Volume": 473,
                        "Unidade": "ml",
                        "Quantidade_Total": 36,
                        "Preço_Unitário": 8.00,
                        "Vencimento": "13/12/2025"
                    }
                ]
            },
            {
                "Código": "CJ007",
                "Marca": "Itaipava",
                "Tipos": [
                    {
                        "Código_Tipo": "TCJ007",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 600,
                        "Unidade": "ml",
                        "Quantidade_Total": 72,
                        "Preço_Unitário": 10.00,
                        "Vencimento": "15/10/2025"
                    },

                    {
                        "Código_Tipo": "TCJ007.1",
                        "Tipo_Embalagem": "Lata",
                        "Volume": 350, 
                        "Unidade": "ml", 
                        "Quantidade_Total": 72, 
                        "Preço_Unitário": 5.00, 
                        "Vencimento": "15/10/2024"
                    },

                    {
                        "Código_Tipo": "TCJ007.2",
                        "Tipo_Embalagem": "Latão", 
                        "Volume": 473, 
                        "Unidade": "ml", 
                        "Quantidade_Total": 72, 
                        "Preço_Unitário": 8.00, 
                        "Vencimento": "15/10/2024"
                    }
                ]
            },
            {
                "Código": "CJ008",
                "Marca": "Original",
                "Tipos": [
                    {
                        "Código_Tipo": "TCJ008",
                        "Tipo_Embalagem": "Garrafa", 
                        "Volume": 600, 
                        "Unidade": "ml", 
                        "Quantidade_Total": 72, 
                        "Preço_Unitário": 15.00, 
                        "Vencimento": "17/08/2025"
                    },

                    {
                        "Código_Tipo": "TCJ008.1",
                        "Tipo_Embalagem": "Lata",
                        "Volume": 350, 
                        "Unidade": "ml", 
                        "Quantidade_Total": 0, 
                        "Preço_Unitário": None, 
                        "Vencimento": None
                    },

                    {
                        "Código_Tipo": "TCJ008.2",
                        "Tipo_Embalagem": "Latão",
                        "Volume": 473, 
                        "Unidade": "ml", 
                        "Quantidade_Total": 0, 
                        "Preço_Unitário": None, 
                        "Vencimento": None
                    }
                ]
            },
            {
                "Código": "CJ009",
                "Marca": "Amstel",
                "Tipos": [
                    {
                        "Código_Tipo": "TCJ009",
                        "Tipo_Embalagem": "Garrafa", 
                        "Volume": 600, 
                        "Unidade": "ml", 
                        "Quantidade_Total": 72, 
                        "Preço_Unitário": 15.00, 
                        "Vencimento": "17/08/2025"
                    },

                    {
                        "Código_Tipo": "TCJ009.1",
                        "Tipo_Embalagem": "Lata",
                        "Volume": 350, 
                        "Unidade": "ml", 
                        "Quantidade_Total": 0, 
                        "Preço_Unitário": None, 
                        "Vencimento": None
                    },

                    {
                        "Código_Tipo": "TCJ009.2",
                        "Tipo_Embalagem": "Latão",
                        "Volume": 473, 
                        "Unidade": "ml", 
                        "Quantidade_Total": 0, 
                        "Preço_Unitário": None, 
                        "Vencimento": None
                    }
                ]
            },
            {
                "Código": "CJ010",
                "Marca": "Serra Malte",
                "Tipos": [
                    {
                        "Código_Tipo": "TCJ010",
                        "Tipo_Embalagem": "Garrafa", 
                        "Volume": 600, 
                        "Unidade": "ml", 
                        "Quantidade_Total": 72, 
                        "Preço_Unitário": 15.00, 
                        "Vencimento": "17/08/2025"
                    }                   
                ]
            },
            {
                "Código": "CJ011",
                "Marca": "Cerveja Caracu(Escura)",
                "Tipos": [
                    {
                        "Código_Tipo": "TCJ011",
                        "Tipo_Embalagem": "Garrafa", 
                        "Volume": 600, 
                        "Unidade": "ml", 
                        "Quantidade_Total": 72, 
                        "Preço_Unitário": 15.00, 
                        "Vencimento": "17/08/2025"
                    }                   
                ]
            }

        ]
    }
}

def estoque_cervejas():
    """Função para exibir as cervejas no estoque de maneira organizada e intuitiva."""
    for categoria, cervejas in estoque["Bebidas"].items():
        print(f"\n\U0001f37a ► Categoria: {categoria} ◄ ")

        for cerveja in cervejas:
            print(f"\n\U0001f525 Código do Produto: {cerveja['Código']}\n\U0001f7e2 {cerveja['Marca']}")

            for tipo in cerveja['Tipos']:
                print(f"\U0001f535 - {tipo['Tipo_Embalagem']} ({tipo['Volume']} {tipo['Unidade']})\n"
                      f" Quantidade: {tipo['Quantidade_Total']} | Vencimento: {tipo['Vencimento']}\n"

                      f"-->\U0001f4b0 Preço: R${tipo['Preço_Unitário']: .2f} <--\n" + "*" * 40 + "\n" if tipo['Preço_Unitário'] else "\n\U0001f7e2 Preço: Não informado.\n" + "*" *40)

estoque_cervejas()





