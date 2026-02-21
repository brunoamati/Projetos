# 🔐 Gerador de Senhas

Utilitário desenvolvido para criar senhas seguras e personalizadas, com foco em usabilidade e segurança da informação.

### ✨ Funcionalidades
* **Customização Total:** Escolha entre incluir letras, números e símbolos.
* **Filtro de Ambiguidade:** Opção para remover caracteres visualmente parecidos (como `1`, `l`, `0`, `O`) para evitar erros de digitação.
* **Análise de Força:** Classifica a senha como Fraca, Mediana ou Forte com base em critérios de complexidade.
* **Histórico Automático:** Salva cada senha gerada em um arquivo `senhas_geradas.txt` com carimbo de data e hora.

### 💻 Conceitos Aplicados
* Manipulação de arquivos (`with open`).
* Uso da biblioteca `datetime` para logs.
* Bibliotecas `random` e `string` para geração de dados.

**Qualquer adição ou erro que possa ter no código fico aberto a sugestões e correções na aba de issues.**