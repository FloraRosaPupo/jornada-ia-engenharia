# 🚀 IA + Engenharia de Software + DevOps/Cloud

Repositório de estudos e projetos práticos de um cronograma de 23 semanas (14/09/2026 → 21/02/2027), cobrindo desde fundamentos de NLP/LLM até uma plataforma de IA em produção.

## Princípio do projeto

> **Não vamos reinventar o que já existe. Vamos entender profundamente, experimentar e saber colocar em produção.**

- ❌ Construir um LLM, Transformer ou protocolo do zero só para "dizer que fez"
- ✅ Entender a fundo como tudo funciona internamente
- ✅ Usar, comparar e ajustar modelos/ferramentas já existentes
- ✅ Construir aplicações reais (RAG, Tool Calling, Agents) e documentar o processo publicamente

## Rotina

- **Segunda a sexta:** ~2h/dia (≈1h teoria + ≈1h prática)
- **Sábado e domingo:** 3–4h/dia de prática intensiva
- **Toda semana:** um artefato aqui no repo + um post no LinkedIn

## Estrutura planejada do repositório

As pastas abaixo são planejadas, não representam entregas concluídas. Cada pasta é uma fase do cronograma, e dentro de cada fase há uma subpasta por semana.

### `fase-1-fundamentos-nlp-llm/` — Semanas 1 a 4 (14/09 – 11/10)
Tokenização, embeddings, self-attention e a arquitetura completa do Transformer — entendendo o caminho Texto → Tokenização → Embeddings → Attention → Transformer → Resposta usando modelos já existentes.
- `semana-01-tokenizacao`
- `semana-02-embeddings`
- `semana-03-attention`
- `semana-04-transformer`

### `fase-2-modelos-existentes/` — Semanas 5 a 6 (12/10 – 25/10)
Explorar o Hugging Face Hub, pipelines, comparação de modelos e critérios de avaliação (custo, latência, qualidade).
- `semana-05-explorando-modelos`
- `semana-06-avaliacao-modelos`

### `fase-3-fine-tuning-avaliacao/` — Semanas 7 a 8 (26/10 – 08/11)
Fine-tuning com LoRA/PEFT em modelos existentes e quantização (FP32/FP16/INT8/INT4) — custo vs qualidade.
- `semana-07-fine-tuning`
- `semana-08-quantizacao`

### `fase-4-rag/` — Semanas 9 a 11 (09/11 – 29/11)
Embeddings semânticos, vector search e construção de uma aplicação RAG completa, com refino (hybrid search, reranking, avaliação).
- `semana-09-vector-search`
- `semana-10-rag`
- `semana-11-rag-avancado`

### `fase-5-tool-calling/` — Semanas 12 a 13 (30/11 – 13/12)
Function/tool calling — o ciclo LLM → ferramenta → resultado → LLM — e segurança em execução de ferramentas.
- `semana-12-tool-calling`
- `semana-13-tool-calling-avancado`

### `fase-6-mcp/` — Semanas 14 a 15 (14/12 – 27/12)
Entender o Model Context Protocol e usar servers MCP existentes (sem necessidade de construir um do zero).
- `semana-14-protocolo-mcp`
- `semana-15-mcp-na-pratica`

### `fase-7-agents/` — Semanas 16 a 17 (28/12 – 10/01)
Construir um agente de IA com framework existente — agent loop, memória, planejamento — e testar sua confiabilidade.
- `semana-16-fundamentos-agentes`
- `semana-17-confiabilidade-agentes`

### `fase-8-arquitetura/` — Semanas 18 a 19 (11/01 – 24/01)
Microsserviços e arquitetura orientada a eventos para o projeto final.
- `semana-18-microservicos`
- `semana-19-event-driven`

### `fase-9-devops-cloud/` — Semanas 20 a 22 (25/01 – 14/02)
Docker, Kubernetes, AWS, Terraform, CI/CD, observabilidade e segurança.
- `semana-20-docker-kubernetes`
- `semana-21-aws-terraform`
- `semana-22-cicd-observabilidade-seguranca`

### `projeto-final-adaptive-learning-ai/` — Semana 23 (15/02 – 21/02)
Integração de tudo em uma plataforma de IA demonstrável: Flutter → API Gateway → Microsserviços → AI Orchestrator → LLM/RAG/Agent → MCP → Tools, rodando em Kubernetes/AWS com CI/CD e observabilidade.

## Competências desenvolvidas

NLP, tokenização, embeddings, Transformers, LLMs, inferência, fine-tuning, LoRA, quantização, avaliação de modelos, vector search, RAG, tool calling, MCP, agentes, microsserviços, arquitetura orientada a eventos, Docker, Kubernetes, AWS, Terraform, CI/CD, observabilidade e segurança de aplicações de IA.

## Acompanhe no LinkedIn

Cada semana gera um post público documentando o que foi aprendido e construído — https://www.linkedin.com/in/flora-rosa-b386841b6/.

## Entrega executável

[Baseline de busca lexical](experimentos/README.md), com testes automatizados e CI. As demais fases permanecem planejadas.


## Stack e bibliotecas

Python padrão: math, collections, argparse e unittest.


## Funcionalidades

- Busca lexical TF-IDF.
- corpus de exemplo.
- roteiro de estudos.


## Licença

Não há licença de distribuição definida neste repositório. Os direitos de terceiros e as atribuições existentes devem ser respeitados; esta revisão não concede permissão de redistribuição.


## Organização e manutenção

Experimentos independentes em `experimentos` e testes em `tests`; o roteiro distingue entregas existentes de diretórios planejados. Funções puras permitem estudar sem depender de API ou modelo remoto.

Veja [a revisão de desenvolvimento](docs/REVISAO.md) para decisões, testes e limites, e [o guia de contribuição](CONTRIBUTING.md) para o fluxo de manutenção.
