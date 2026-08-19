# Arquitetura pública

O projeto privado completo do Proton for Seller possui várias camadas. Este snapshot publica somente utilitários independentes e seguros para demonstração.

## Catálogo

Responsável por interpretar produtos, preços, estoque e elementos de apresentação do painel.

## Tickets

O snapshot contém apenas utilitários simples de nomes e metadados de ticket. Criação de canais, permissões, transcripts, triagem e integrações ficam fora deste repositório.

## Sorteios

Apenas o parser/formatador de duração é público. Persistência, participantes, seleção de vencedores, compras obrigatórias e cupons ficam privados.

## Integrações privadas

Gateways de pagamento, banco de dados, licenciamento, wallet, webhooks, lógica de confirmação e rotinas de produção não são incluídos.
