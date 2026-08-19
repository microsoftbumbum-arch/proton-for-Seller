# Proton for Seller — Public

Versão pública e parcial do **Proton for Seller**, um sistema de vendas e automação para servidores do Discord.

Este repositório existe como **showcase técnico** do projeto. Ele contém utilitários e exemplos reais usados na experiência do Seller, mas **não contém o núcleo comercial nem os sistemas sensíveis da aplicação**.

## O que está público

- Parser de produtos no formato `nome | preço | quantidade`
- Formatação e leitura de preços em BRL
- Utilitários de estoque
- Normalização de URLs de imagem para painéis
- Sanitização de nomes de canais
- Utilitários de duração de sorteios
- Exemplos de catálogo e testes

## O que permanece privado

- Token e inicialização do bot de produção
- Pagamentos, PIX, Mercado Pago e GoatPay
- Wallet e saques
- MongoDB e persistência de produção
- Sistema de licenças/keys e planos
- Cupons e lógica comercial
- Entrega automática e estoque sensível
- Fluxo completo de carrinho e confirmação de compra
- Painéis administrativos internos
- Proteções e regras de produção

## Exemplo rápido

```python
from proton_seller_public.catalog import parse_product_lines

products = parse_product_lines(
    "Nitro | R$ 12,90 | 5\n"
    "VIP | 7,50 | 10"
)

for product in products:
    print(product)
```

Saída aproximada:

```text
{'name': 'Nitro', 'price': 'R$ 12,90', 'stock': '5', 'emoji_id': None}
{'name': 'VIP', 'price': '7,50', 'stock': '10', 'emoji_id': None}
```

## Estrutura

```text
proton-for-seller-public/
├── src/proton_seller_public/
│   ├── catalog.py
│   ├── giveaways.py
│   └── text.py
├── examples/
├── tests/
└── docs/
```

## Segurança

Nenhuma credencial real deve ser adicionada a este repositório. Use variáveis de ambiente para segredos e veja [`SECURITY.md`](SECURITY.md).

## Licença

Nenhuma licença de reutilização é concedida automaticamente por este repositório. Se o projeto passar a aceitar reutilização ou contribuições externas, adicione uma licença adequada explicitamente.
