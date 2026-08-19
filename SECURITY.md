# Security Policy

## Segredos

Nunca faça commit de:

- token do Discord
- API keys de gateways de pagamento
- URI do MongoDB com usuário/senha
- tokens do Mercado Pago
- chaves administrativas
- arquivos `.env` reais
- dados privados de servidores ou clientes

Use apenas `.env.example` com placeholders.

## Se uma credencial for exposta

1. Revogue ou rotacione a credencial imediatamente.
2. Gere uma nova credencial.
3. Atualize o ambiente de produção.
4. Remova a credencial do código e do histórico quando necessário.
5. Verifique logs e acessos associados à credencial antiga.
