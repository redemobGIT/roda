# RODA — Diagnóstico Urbano e Mobilidade

**Notebooks e utilitários para descrever o ambiente urbano e analisar mobilidade, acessibilidade e desigualdades socioespaciais.**
Projeto no âmbito do **MOB 4.0**, com apoio de **FAPERJ** e **FAPEMIG**, em parceria com a **COPPE/UFRJ (PET)** e com a **Universidade Estadual de Montes Claros/MG (UNIMONTES)**.

## Sumário

* [Visão geral](#visão-geral)
* [Escopo do repositório](#escopo-do-repositório)
* [Principais métodos](#principais-métodos)
* [Entradas de dados](#entradas-de-dados)
* [Requisitos e instalação](#requisitos-e-instalação)
* [Início rápido](#início-rápido)
* [Boas práticas e reprodutibilidade](#boas-práticas-e-reprodutibilidade)
* [Roadmap](#roadmap)
* [Contribuição](#contribuição)
* [Como citar](#como-citar)
* [Financiamento e parcerias](#financiamento-e-parcerias)
* [Licença](#licença)

## Visão geral

O **RODA** organiza um conjunto de análises **reprodutíveis** com foco em cidades brasileiras, integrando:

* **Mobilidade e transporte público** (diagnósticos GTFS, cobertura e oferta);
* **Acessibilidade a oportunidades** (empregos, saúde pública, educação pública);
* **Desigualdade e segregação socioespacial**;
* **Topologia de redes urbanas** (sintaxe espacial e centralidade em grafos);
* **Segurança pública** (quando disponível), relacionando incidentes e padrões de deslocamento.

Os notebooks priorizam **parâmetros explícitos** no início do fluxo e **automação** dos passos, produzindo mapas, indicadores e gráficos prontos para relatórios técnicos e apoio à decisão.

## Escopo do repositório

A estrutura pode evoluir, mas parte das seguintes frentes:

```
roda/
├─ tutoriais/              # Documentos contextualizadores de cada script e guia de instalação
├─ scripts/                # Notebooks temáticos (acessibilidade, GTFS, rede, etc.)
├─ database/               # Esquemas, tabelas auxiliares, metadados
├─ data/                   # alguns insumos brutos e processados
├─ outputs/                # Figuras, mapas e tabelas geradas (opcional)
└─ README.md               # Este documento
```

## Principais métodos

* **Unidade espacial comum (H3)**: análises em malhas hexagonais (tipicamente res. 9), mitigando efeitos de borda e favorecendo comparabilidade entre temas.
* **Acessibilidade**: medidas cumulativas (n oportunidades em *T* minutos) e/ou custo mínimo até a oportunidade mais próxima, a partir de **matrizes de tempo de viagem multimodal**.
* **GTFS**: leitura, validação e diagnóstico de oferta (frequência, janela de operação, cobertura), subsidiando cálculos de acessibilidade.
* **Topologia de rede**: métricas de **sintaxe espacial** e **centralidade em grafos** para identificar corredores estruturantes, áreas candidatas a estações e potenciais **screenlines** para contagem/calibração.
* **Desigualdade/segregação**: comparação de indicadores entre grupos socioeconômicos, uso de índices (p.ex., **Gini**, **dissimilaridade**) e análises escalares.
* **Segurança** (opcional): integração de ocorrências (p.ex., **Fogo Cruzado**, ISP) para investigar co-variação com mobilidade e forma urbana.


## Requisitos e instalação

Recomenda-se **Conda** (ou `uv`/`venv`) com Python ≥ 3.11 e o ecossistema geoespacial.

Dependências típicas:

* Núcleo: `pandas`, `numpy`, `pyarrow`, `geopandas`, `shapely`, `pyproj`, `rtree`
* Hex e zonificação: `h3` (h3-py), `tobler`
* Visualização: `matplotlib`, `plotly`, `contextily`
* Mobilidade: `r5py` (e Java instalado), `gtfs_kit` e/ou `partridge`
* Cadernos e utilidades: `jupyterlab`, `ipykernel`, `tqdm`
* (Opcional – nuvem): `google-cloud-bigquery`, `pandas-gbq`

> Um arquivo `environment.yml` facilita a instalação de dependêncas. Ele possui a lista completa das bibliotecas necessárias utilizadas para rodar os scripts, garantir a compatibilidade de bibliotecas e a reprodutibilidade dos resultados.

> Na pasta tutoriais há um guia de instalação voltado para iniciantes

## Contribuição

Contribuições são bem-vindas via *pull requests* e *issues*.
Por favor:

1. Mantenha notebooks **modulares e parametrizados**;
2. Documente passos e suposições com *docstrings* e *markdown*;
3. Prefira soluções **transparentes e reprodutíveis**;
4. Anexe *previews* leves (figuras) quando pertinente.

## Como citar

**A definir.**

## Financiamento e parcerias

Este trabalho integra o **MOB – Mobilidade Urbana 4.0** com apoio de **FAPERJ** e **FAPEMIG**, em parceria com a **COPPE/UFRJ (PET)** e com a **Universidade Estadual de Montes Claros/MG (UNIMONTES)**, reunindo esforços de pesquisa e inovação voltados à qualificação de processos urbanos.

## Licença

**A definir.**

---

## ESTADO DO PROJETO

Este repositório encontra-se em versão alpha. Há notebooks e utilitários já funcionais, mas a estrutura, nomes de funções/colunas, parâmetros e outputs podem mudar a qualquer momento. Mudanças frequentes e adições substanciais são esperadas nas próximas iterações.

O que significa “alpha” aqui

    Utilidade: fluxos principais (diagnósticos GTFS, acessibilidade, H3, indicadores socioespaciais) já produzem resultados.

    Estabilidade incompleta: sem garantia de compatibilidade entre versões; refatorações e reorganização de pastas são prováveis.

    Cobertura de testes: parcial; prioriza-se evolução metodológica e documentação de uso.

    Documentação: em expansão; exemplos e guias “passo a passo” serão ampliados.

**Roadmap futuro resumido**

    Consolidar módulo de utilidades (I/O, H3, plotting e validadores).

    Ampliar testes e dados de exemplo.

    Publicar tutoriais narrativos (ex.: GTFS → matriz de tempos → mapas de acessibilidade).

    Integrar checks automáticos de qualidade (lint/CI) e pre-commit.

**Feedback e suporte**

    Problemas e sugestões: abra uma issue descrevendo contexto, dados de entrada, passos para reproduzir e tracebacks (quando houver).

    Contribuições: pull requests são bem-vindos.


