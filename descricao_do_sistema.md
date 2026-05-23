# Descrição do Sistema — LicitAI

## Descrição geral

O LicitAI é uma plataforma de consulta e análise de licitações públicas brasileiras. O sistema coleta periodicamente dados do Portal Nacional de Contratações Públicas (PNCP), os armazena em base estruturada e os disponibiliza para consulta por meio de mecanismos de busca textual e de busca por similaridade semântica. A plataforma atende dois perfis de usuário: o usuário público, que realiza consultas e análises sem necessidade de autenticação, e o administrador, que opera e monitora o sistema.

O sistema permite que qualquer pessoa pesquise licitações utilizando tanto termos objetivos quanto descrições em linguagem natural. Os resultados podem ser refinados por critérios como unidade federativa, modalidade de contratação, faixa de valor e período de publicação. Cada licitação pode ser visualizada em detalhe, com informações sobre o órgão responsável, a unidade contratante, os itens do processo e os valores estimados. Um painel analítico apresenta indicadores agregados sobre o conjunto de licitações armazenadas.

Do lado operacional, o administrador define os parâmetros das coletas, acompanha o status de cada execução e pode exportar os dados para ferramentas externas de análise.

---

## Requisitos Funcionais

**RF01** O sistema deve realizar busca de licitações por termos textuais sobre o objeto da compra, retornando resultados ordenados por relevância

**RF02** O sistema deve realizar busca de licitações por linguagem natural, interpretando a consulta do usuário e recuperando resultados por similaridade semântica

**RF03** O sistema deve permitir que o usuário refine os resultados de qualquer modalidade de busca aplicando filtros por unidade federativa, modalidade de contratação, faixa de valor, situação e período de publicação

**RF04** O sistema deve exibir, em tela dedicada, todas as informações de uma licitação selecionada, incluindo dados do órgão contratante, itens do processo com quantidades e valores, datas relevantes e situação atual

**RF05** O sistema deve disponibilizar um painel com indicadores agregados sobre as licitações armazenadas, incluindo distribuição por modalidade, órgão e unidade federativa, e evolução temporal dos valores

**RF06** O sistema deve coletar licitações da API do PNCP a partir de parâmetros de data, modalidade e UF configurados pelo administrador, registrando cada execução com status e total de registros processados

**RF07** O sistema deve permitir que o administrador configure e agende coletas recorrentes sem necessidade de intervenção manual a cada execução

**RF08** O sistema deve disponibilizar ao administrador o histórico de execuções de coleta, com status, parâmetros utilizados e possibilidade de reprocessamento em caso de falha

**RF09** O sistema deve permitir que o administrador exporte os dados de licitações em formato CSV para uso em ferramentas externas de análise

---

## Rastreabilidade

| Requisito | Motivado por  | Compõe              |
|-----------|---------------|---------------------|
| RF01      | HU01          | UC01                |
| RF02      | HU02          | UC02                |
| RF03      | HU03          | UC01 UC02 UC03      |
| RF04      | HU04          | UC04                |
| RF05      | HU05          | UC05                |
| RF06      | HU06          | UC06 UC08           |
| RF07      | HU07          | UC07                |
| RF08      | HU08          | UC08                |
| RF09      | HU09          | UC09                |
