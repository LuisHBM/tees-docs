# Histórias de Usuário — LicitAI

## Atores

**Usuário público** é o pesquisador, jornalista, fornecedor ou cidadão que consulta licitações sem autenticação

**Administrador** é o responsável pela operação da plataforma, pela configuração das coletas e pelo monitoramento do sistema

---

## Histórias do Usuário Público

### HU01 Busca por palavra-chave

Como usuário público quero pesquisar licitações digitando termos do objeto da compra para encontrar rapidamente editais relacionados ao meu interesse sem precisar navegar por portais governamentais

Requisito originado: RF01

---

### HU02 Busca por linguagem natural

Como usuário público quero descrever o que estou procurando com minhas próprias palavras e obter resultados relevantes mesmo que minha frase não corresponda exatamente ao texto do edital para que eu não precise conhecer o vocabulário técnico das licitações

Requisito originado: RF02

---

### HU03 Filtro por critérios objetivos

Como usuário público quero filtrar os resultados por estado, modalidade, faixa de valor, situação e período de publicação para restringir a busca ao contexto que me interessa e reduzir o volume de resultados irrelevantes

Requisito originado: RF03

---

### HU04 Detalhamento da licitação

Como usuário público quero ver todas as informações de uma licitação específica em uma única tela para avaliar se ela é relevante sem precisar acessar o PNCP diretamente

Requisito originado: RF04

---

### HU05 Visão analítica agregada

Como usuário público quero ver painéis com indicadores sobre volume de licitações, distribuição por modalidade, órgão ou região e evolução temporal dos valores para entender o comportamento das compras públicas em determinado contexto

Requisito originado: RF05

---

## Histórias do Administrador

### HU06 Coleta de dados do PNCP

Como administrador quero acionar a coleta de licitações na API do PNCP informando um intervalo de datas, modalidade e UF para manter a base de dados atualizada com novos editais publicados

Requisito originado: RF06

---

### HU07 Configuração dos parâmetros de coleta

Como administrador quero definir com antecedência os parâmetros de uma coleta como período, modalidade, UF e frequência para automatizar a atualização da base sem precisar intervir manualmente a cada execução

Requisito originado: RF07

---

### HU08 Monitoramento do sistema

Como administrador quero acompanhar os logs das coletas e o status de cada execução para identificar falhas, reprocessar coletas com erro e garantir a integridade dos dados

Requisito originado: RF08

---

### HU09 Exportação para BI

Como administrador quero exportar os dados de licitações em formato CSV para alimentar dashboards no Power BI com dados tratados e atualizados

Requisito originado: RF09
