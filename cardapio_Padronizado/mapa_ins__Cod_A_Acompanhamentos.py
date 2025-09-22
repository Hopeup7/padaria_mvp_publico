print(f"\n\U0001f535 Senhor, sei que És a Luz e que Tua Luz Ilumine a mim de mim mesmo, Meu Senhor.\U0001f7e2\n")

cardapio_ins = {
    "Opção Vendas Comida": {
        "Acompanhamentos - Ovos": [
            {
                "Código": "Ac001",
                "Nome": "Ovo Frito",
                "Variações": [
                    {
                        "Código_Tipo": "TAc001",
                        "Nome": "Tradicional",
                        "Preço": 3.00,
                        "Insumos": [

                            {"Código_Sup": "Of001", "Volume": 1,
                                "Unidade": "un"},  # Ovo

                            {"Características": "Um ovo Frito"}
                        ]
                    },
                    {
                        "Código_Tipo": "TAc001.1",
                        "Nome": "Com Orégano",
                        "Preço": 3.00,
                        "Insumos": [

                            {"Código_Sup": "Of001", "Volume": 1,
                                "Unidade": "un"},  # Ovo

                            {"Código_Sup": "Cd017", "Volume": 5,
                                "Unidade": "g"},  # Orégano

                            {"Características": "Um ovo Frito, Orégano"}
                        ]
                    },
                    {
                        "Código_Tipo": "TAc001.2",
                        "Nome": "Com Presunto",
                        "Preço": 3.00,
                        "Insumos": [

                            {"Código_Sup": "Of001", "Volume": 1,
                                "Unidade": "un"},  # Ovo

                            {"Código_Sup": "E005", "Volume": 25,
                                "Unidade": "g"},  # Presunto

                            {"Código_Sup": "L007", "Volume": 25,
                                "Unidade": "g"},  # Queijo Prato

                            {"Características": "Um ovo Frito, Presunto, Queijo"}
                        ]
                    },
                    {
                        "Código_Tipo": "TAc001.3",
                        "Nome": "Monster",
                        "Preço": 3.00,
                        "Insumos": [

                            {"Código_Sup": "Of001", "Volume": 3,
                                "Unidade": "un"},  # Ovo

                            {"Código_Sup": "E005", "Volume": 25,
                                "Unidade": "g"},  # Presunto

                            {"Código_Sup": "L007", "Volume": 25,
                                "Unidade": "g"},  # Queijo Prato

                            {"Código_Sup": "E003", "Volume": 40,
                                "Unidade": "g"},  # Bacon

                            {"Características": "Três ovos Fritos, Presunto, Queijo, Bacon"}
                        ]
                    },
                    {
                        "Código_Tipo": "TAc001.4",
                        "Nome": "Ovo Cozido",
                        "Preço": 1.00,
                        "Insumos": [

                            {"Código_Sup": "Of001", "Volume": 1,
                                "Unidade": "un"},  # Ovo

                            {"Características": "Ovo Cozido"}
                        ]
                    }
                ]
            }
        ],
        "Acompanhamentos - Saladas": [
            {
                "Código": "Ac002",
                "Nome": "Mix de Legumes Grelhados",
                "Variações": [
                    {
                        "Código_Tipo": "TAc002",
                        "Nome": "Mix de Legumes Grelhados",
                        "Preço": 5.00,
                        "Insumos": [

                            {"Código_Sup": "H007", "Volume": 25,
                                "Unidade": "g"},  # Abobrinha

                            {"Código_Sup": "H014", "Volume": 20,
                                "Unidade": "g"},  # Berinjela

                            {"Código_Sup": "H013", "Volume": 20,
                                "Unidade": "g"},  # Cenoura

                            {"Código_Sup": "H037", "Volume": 10,
                                "Unidade": "g"},  # Pimentão-Vermelho

                            {"Características": "Abobrinha, Berinjela, Cenoura, Pimentão-Vermelho, Cebola Roxa, Grelhados"}
                        ]
                    }
                ]
            },
            {
                "Código": "Ac003",
                "Nome": "Vinagrete",
                "Variações": [
                    {
                        "Código_Tipo": "TAc003",
                        "Nome": "Vinagrete",
                        "Preço": 5.00,
                        "Insumos": [

                            {"Código_Sup": "H017", "Volume": 15,
                                "Unidade": "g"},  # Tomate

                            {"Código_Sup": "H018", "Volume": 25,
                                "Unidade": "g"},  # Cebola

                            {"Código_Sup": "H033", "Volume": 20,
                                "Unidade": "g"},  # Cheiro-Verde

                            {"Código_Sup": "H001", "Volume": 10,
                                "Unidade": "ml"},  # Limão

                            {"Características": "Tomate, Cebola, Cheiro-Verde(Salsinha e Cebolinha), Limão"}
                        ]
                    }
                ]
            },
            {
                "Código": "Ac004",
                "Nome": "Salada Padrão(1)",
                "Variações": [
                    {
                        "Código_Tipo": "TAc004",
                        "Nome": "Saladinha",
                        "Preço": 5.00,
                        "Insumos": [

                            {"Código_Sup": "H020", "Volume": 15,
                                "Unidade": "g"},  # Alface

                            {"Código_Sup": "H017", "Volume": 15,
                                "Unidade": "g"},  # Tomate

                            {"Código_Sup": "H018", "Volume": 15,
                                "Unidade": "g"},  # Cebola

                            {"Características": "Alface, Tomate, Cebola"}
                        ]
                    }
                ]
            },
            {
                "Código": "Ac005",
                "Nome": "Salada Padrão(2)",
                "Variações": [
                    {
                        "Código_Tipo": "TAc005",
                        "Nome": "Repolho Fatiadinho",
                        "Preço": 5.00,
                        "Insumos": [

                            {"Código_Sup": "H010", "Volume": 15,
                                "Unidade": "g"},  # Repolho Verde

                            {"Características": "Repolho"}
                        ]
                    }
                ]
            }
        ],
        "Acompanhamentos - Maioneses/Molhos Caseiros": [
            {
                "Código": "Ac006",
                "Nome": " Maionese Verde Caseira (Base com Leite)",
                "Variações": [
                    {
                        "Código_Tipo": "TAc006",
                        "Nome": "Maionese Verde",
                        "Preço": 5.00,
                        "Insumos": [

                            {"Código_Sup": "L001", "Volume": 100,
                                "Unidade": "ml"},  # Leite Integral

                            {"Código_Sup": "Cd009", "Volume": 200,
                                "Unidade": "ml"},  # Óleo de Soja

                            {"Código_Sup": "H019", "Volume": 5,
                                "Unidade": "g"},  # Alho

                            {"Código_Sup": "H033", "Volume": 15,
                                "Unidade": "g"},  # Cheiro-Verde

                            {"Código_Sup": "Cd013", "Volume": 2,
                                "Unidade": "ml"},  # Sal

                            {"Código_Sup": "H001", "Volume": 5,
                                "Unidade": "g"},  # Limão

                            {"Características": "Leite integral (gelado), Óleo de soja, Alho, Cheiro-verde (salsa + cebolinha), Sal, Suco de limão, Rendimento: ~ 300g"}
                        ]
                    }
                ]
            },
            {
                "Código": "Ac007",
                "Nome": " Molho Churrasco Caseiro (Estilo Barbecue))",
                "Variações": [
                    {
                        "Código_Tipo": "TAc007",
                        "Nome": "Molho Churrasco Caseiro",
                        "Preço": 5.00,
                        "Insumos": [

                            {"Código_Sup": "Cd031", "Volume": 240,
                                "Unidade": "g"},  # Ketchup

                            {"Código_Sup": "Cd004", "Volume": 90,
                                "Unidade": "g"},  # Açucar Mascavo

                            {"Código_Sup": "Cd033", "Volume": 60,
                                "Unidade": "ml"},  # Vinagre de Maça

                            {"Código_Sup": "Cd029", "Volume": 60,
                                "Unidade": "ml"},  # Molho Inglês

                            {"Código_Sup": "Cd030", "Volume": 30,
                                "Unidade": "g"},  # Mostarda

                            {"Código_Sup": "Cd026", "Volume": 60,
                                "Unidade": "g"},  # Shoyu

                            {"Código_Sup": "Cd019", "Volume": 3,
                                "Unidade": "g"},  # Alho em Pó

                            {"Código_Sup": "Cd034", "Volume": 3,
                                "Unidade": "g"},  # Cebola em Pó

                            {"Código_Sup": "Cd015", "Volume": 1,
                                "Unidade": "g"},  # Pimenta do Reino

                            {"Código_Sup": "Ag001", "Volume": 120,
                                "Unidade": "ml"},  # Água

                            {"Características": "Ketchup, Açúcar mascavo, Vinagre de maçã, Molho inglês, Mostarda amarela, Shoyu, Alho em pó, Cebola em pó, Pimenta-do-reino, Água, Rendimento: ~ 400g"}
                        ]
                    }
                ]
            },
            {
                "Código": "Ac008",
                "Nome": "Molho Costela",
                "Variações": [
                    {
                        "Código_Tipo": "TAc008",
                        "Nome": "Molho Costela",
                        "Preço": 5.00,
                        "Insumos": [
                            {"Código_Sup": "Cd031", "Volume": 240,
                                "Unidade": "g"},  # Ketchup

                            {"Código_Sup": "Cd033", "Volume": 60,
                                "Unidade": "ml"},  # Vinagre de Maça

                            {"Código_Sup": "Cd004", "Volume": 36,
                                "Unidade": "g"},  # Açucar Mascavo

                            {"Código_Sup": "Cd026", "Volume": 45,
                                "Unidade": "ml"},  # Shoyu

                            {"Código_Sup": "H019", "Volume": 5,
                                "Unidade": "g"},  # Alho

                            {"Código_Sup": "H018", "Volume": 80,
                                "Unidade": "g"},  # Cebola

                            {"Código_Sup": "H001", "Volume": 15,
                                "Unidade": "ml"},  # Limão

                            {"Código_Sup": "Cd011", "Volume": 30,
                                "Unidade": "ml"},  # Azeite


                            {"Características": "Ketchup, Vinagre de maçã, Açúcar mascavo, Shoyu, Alho batido, Cebola picada, Suco de limão, Azeite,  Rendimento: ~ 350g"}
                        ]
                    }
                ]
            },
            {
                "Código": "Ac009",
                "Nome": "Molho de Alho Cremoso",
                "Variações": [
                    {
                        "Código_Tipo": "TAc009",
                        "Nome": "Molho de Alho Cremoso",
                        "Preço": 5.00,
                        "Insumos": [

                            {"Código_Sup": "L001", "Volume": 100,
                                "Unidade": "ml"},  # Leite Integral

                            {"Código_Sup": "Cd009", "Volume": 200,
                                "Unidade": "ml"},  # Óleo de soja

                            {"Código_Sup": "H019", "Volume": 5,
                                "Unidade": "g"},  # Alho

                            {"Código_Sup": "Cd013", "Volume": 2,
                                "Unidade": "g"},  # Sal

                            {"Código_Sup": "H001", "Volume": 5,
                                "Unidade": "ml"},  # Limão


                            {"Características": "Leite integral, Óleo de soja, Alho, Sal, Suco de limão, Rendimento: ~ 300g"}
                        ]
                    }
                ]
            },
            {
                "Código": "Ac010",
                "Nome": "Molho de Mostarda e Mel",
                "Variações": [
                    {
                        "Código_Tipo": "TAc010",
                        "Nome": "Molho de Mostarda e Mel",
                        "Preço": 5.00,
                        "Insumos": [

                            {"Código_Sup": "Cd030", "Volume": 60,
                                "Unidade": "g"},  # Mostarda

                            {"Código_Sup": "D055", "Volume": 85,
                                "Unidade": "g"},  # Mel

                            {"Código_Sup": "Cd032", "Volume": 30,
                                "Unidade": "g"},  # Maionese

                            {"Código_Sup": "Cd033", "Volume": 15,
                                "Unidade": "ml"},  # Vinagre de Maça

                            {"Código_Sup": "Cd013", "Volume": 2,
                                "Unidade": "g"},  # Sal

                            {"Código_Sup": "Cd015", "Volume": 2,
                                "Unidade": "g"},  # Pimenta do Reino


                            {"Características": "Mostarda amarela, Mel, Maionese (opcional), Vinagre de maçã, Sal, Pimenta do Reino, Rendimento: ~ 180g"}
                        ]
                    }
                ]
            },
            {
                "Código": "Ac011",
                "Nome": " Molho Verde Chimichurri Cremoso",
                "Variações": [
                    {
                        "Código_Tipo": "TAc011",
                        "Nome": "Molho Verde Chimichurri Cremoso",
                        "Preço": 5.00,
                        "Insumos": [

                            {"Código_Sup": "H029", "Volume": 20,
                                "Unidade": "g"},  # Salsinha Fresca

                            {"Código_Sup": "H019", "Volume": 5,
                                "Unidade": "g"},  # Alho Natural

                            {"Código_Sup": "Cd035", "Volume": 60,
                                "Unidade": "ml"},  # Vinagre de Vinho

                            # Azeite de Oliva Extra Virgem
                            {"Código_Sup": "Cd011", "Volume": 100, "Unidade": "ml"},

                            {"Código_Sup": "Cd017", "Volume": 2,
                                "Unidade": "g"},  # Oregano

                            {"Código_Sup": "Cd037", "Volume": 1,
                                "Unidade": "g"},  # Pimenta Calabresa

                            {"Código_Sup": "Cd013", "Volume": 2,
                                "Unidade": "g"},  # Sal

                            {"Características": "Salsinha fresca, Alho, Vinagre de vinho, Azeite de oliva, Orégano seco, Pimenta calabresa, Sal, Rendimento: ~ 250g"}
                        ]
                    }
                ]
            },
            {
                "Código": "Ac012",
                "Nome": " Molho de Pimenta Artesanal ",
                "Variações": [
                    {
                        "Código_Tipo": "TAc012",
                        "Nome": "Molho de Pimenta Artesanal",
                        "Preço": 5.00,
                        "Insumos": [

                            {"Código_Sup": "Cd038", "Volume": 100,
                                "Unidade": "g"},  # Pimenta Dedo-de-Moça

                            {"Código_Sup": "Cd022", "Volume": 100,
                                "Unidade": "ml"},  # Vinagre de Álcool

                            {"Código_Sup": "H019", "Volume": 10,
                                "Unidade": "ml"},  # Alho

                            {"Código_Sup": "Cd011", "Volume": 50,
                                "Unidade": "ml"},  # Azeite

                            {"Código_Sup": "Cd013", "Volume": 2,
                                "Unidade": "ml"},  # Sal

                            {"Características": "Pimenta dedo-de-moça (sem semente), Vinagre de álcool, Alho, Azeite, Sal, Rendimento: ~ 300g"}
                        ]
                    }
                ]
            }
        ],
        "Acomapanhamentos - Grelhados": [
        {
                "Código": "Ac013",
                "Nome": "Berinjela Grelhada",
                "Variações": [
                    {
                        "Código_Tipo": "TAc013",
                        "Nome": "Berinjela Grelhada",
                        "Preço": 5.00,
                        "Insumos": [

                            {"Código_Sup": "H014", "Volume": 80,
                                "Unidade": "g"},  # Berinjela

                            {"Código_Sup": "Cd014", "Volume": 2,
                                "Unidade": "g"},  # Sal Grosso

                            {"Código_Sup": "Cd011", "Volume": 5,
                                "Unidade": "ml"},  # Azeite

                            {"Código_Sup": "H036", "Volume": 1,
                                "Unidade": "g"},  # Orégano

                            {"Características": "Berinjela, Sal Grosso, Azeite, Orégano, Rendimento: ~ 300g"}
                        ]
                    }
                ]
            }
        ]
    } 
} 