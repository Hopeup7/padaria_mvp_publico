print(f"\n\U0001f525 Senhor, abençoe meu irmão e filha com toda a Sua extrema Graça de Bondade. Ajude-os em tudo no tudo com tudo.\U0001f525\n")


"""📌 O que foi incluído:
✅ Códigos superiores e inferiores: DXXX para produtos principais e TDXXX para variações, com TDXXX.X se necessário
✅ Estrutura clara e rastreável: Marca, embalagem, peso, unidade e vencimento organizados corretamente
✅ Função de exibição para facilitar consultas futuras
✅ Preparação para futura integração com SQLite
Se quiser conferir antes da versão final, posso te apresentar um resumo ou validar ajustes. Seguimos estruturando com excelência!
"""


estoque = {
    "Bebidas": {
        "Águas": [
            {
                "Código": "Ag001",
                "Marca": "Água Mineral Sem Gás - Lindoya",
                "Tipos": [
                    {
                        "Código_Tipo": "TAg001",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 1,
                        "Unidade": "L",
                        "Quantidade_Total": 24,
                        "Preço_Unitário": 5.00,
                        "Vencimento": "07/12/2025"
                    },
                    {
                        "Código_Tipo": "TAg001.1",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 600,
                        "Unidade": "ml",
                        "Quantidade_Total": 24,
                        "Preço_Unitário": 2.50,
                        "Vencimento": "07/10/2025"
                    }
                ]
            },
            {
                "Código": "Ag002",
                "Marca": "Água Mineral Com Gás - Lindoya",
                "Tipos": [
                    {
                        "Código_Tipo": "TAg002",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 1,
                        "Unidade": "L",
                        "Quantidade_Total": 24,
                        "Preço_Unitário": 5.00,
                        "Vencimento": "07/12/2025"
                    },
                    {
                        "Código_Tipo": "TAg002.1",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 600,
                        "Unidade": "ml",
                        "Quantidade_Total": 24,
                        "Preço_Unitário": 2.50,
                        "Vencimento": "07/10/2025"
                    }
                ]
            },
            {
                "Código": "Ag003",
                "Marca": "Água Mineral Sem Gás - Serra Azul",
                "Tipos": [
                    {
                        "Código_Tipo": "TAg003",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 1,
                        "Unidade": "L",
                        "Quantidade_Total": 24,
                        "Preço_Unitário": 5.00,
                        "Vencimento": "07/12/2025"
                    },
                    {
                        "Código_Tipo": "TAg003.1",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 600,
                        "Unidade": "ml",
                        "Quantidade_Total": 24,
                        "Preço_Unitário": 2.50,
                        "Vencimento": "07/10/2025"
                    }
                ]
            },
            {
                "Código": "Ag004",
                "Marca": "Água Mineral Com Gás - Serra Azul",
                "Tipos": [
                    {
                        "Código_Tipo": "TAg004",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 1,
                        "Unidade": "L",
                        "Quantidade_Total": 24,
                        "Preço_Unitário": 5.00,
                        "Vencimento": "07/12/2025"
                    },
                    {
                        "Código_Tipo": "TAg004.1",
                        "Tipo_Embalagem": "Garrafa",
                        "Volume": 600,
                        "Unidade": "ml",
                        "Quantidade_Total": 24,
                        "Preço_Unitário": 2.50,
                        "Vencimento": "07/10/2025"
                    }
                ]
            }
        ]
    }
}


def estoque_Agua():
    """Aqui eu crio uma função que itera no dict com list atraves de for acessando suas propriedades."""
    for categoria, aguas in estoque['Bebidas'].items():
        print(f"\n\U0001f4a6  ► Categoria: {categoria} ◄\n")

        for agua in aguas:
            print(
                f"\n\U0001f525 Código do Produto: {agua['Código']}\n\U0001f7e2 {agua['Marca']}")

            for tipo in agua['Tipos']:
                print(f"\U0001f535 - {tipo['Tipo_Embalagem']} ({tipo['Volume']} {tipo['Unidade']}) \n"

                      f"Quantidade: {tipo['Quantidade_Total']} |Vencimento: {tipo['Vencimento']}\n"

                      f"--> \U0001f4b0 Preço: R$ {tipo['Preço_Unitário']: .2f} <--\n" + "*" * 40 if tipo['Preço_Unitário'] else
                      "\n\U0001f7e2 Preço: Não Informado.")


estoque_Agua()
