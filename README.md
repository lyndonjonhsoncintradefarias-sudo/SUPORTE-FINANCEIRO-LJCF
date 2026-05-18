# Suporte Financeiro LJCF

Sistema de suporte financeiro com processamento de tarefas em segundo plano usando Celery e Redis.

## Componentes

### Backend Worker (Python + Celery)
- **Celery Worker**: Processa tarefas assíncronas
- **Celery Beat**: Agendador de tarefas periódicas
- **Redis**: Broker de mensagens e backend de resultados

### Frontend (Web Analytics)
- **Vercel Web Analytics**: Monitoramento de visitantes e análise de tráfego

## Configuração

### Variáveis de Ambiente

Copie `.env.example` para `.env` e configure:

```bash
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

### Instalação

#### Backend (Python)
```bash
pip install -r requirements.txt
```

#### Frontend (Node.js)
```bash
npm install
```

## Execução

### Worker Celery
```bash
celery -A worker.tasks worker --loglevel=info
```

### Celery Beat (Agendador)
```bash
celery -A worker.tasks beat --loglevel=info
```

### Servidor de Desenvolvimento Web
```bash
npm run dev
```

Acesse http://localhost:8000/public/ para ver a interface web.

## Vercel Web Analytics

O projeto está configurado com Vercel Web Analytics para rastreamento de visitantes. A análise é feita automaticamente quando o site está implantado no Vercel.

### Recursos do Analytics
- Visualizações de página
- Origem do tráfego
- Dispositivos e navegadores
- Localização geográfica
- Performance em tempo real

### Verificação

Após o deploy no Vercel:
1. Acesse o dashboard do projeto no Vercel
2. Navegue até a aba "Analytics"
3. Visualize os dados de tráfego em tempo real

O script de analytics está incluído em `public/index.html` e será carregado automaticamente em produção.

## Deploy no Vercel

```bash
# Instalar Vercel CLI
npm i -g vercel

# Deploy
vercel
```

## Tarefas Disponíveis

### Tarefa Periódica de Exemplo
Executada automaticamente a cada 5 minutos:
```python
worker.tasks.example_periodic_task
```

### Tarefa Sob Demanda
```python
from worker.tasks import example_task
example_task.delay("sua mensagem aqui")
```

## Estrutura do Projeto

```
.
├── worker/              # Módulo do worker Celery
│   ├── __init__.py
│   └── tasks.py        # Definição de tarefas
├── public/             # Arquivos estáticos da web
│   └── index.html     # Página principal com Analytics
├── requirements.txt    # Dependências Python
├── package.json       # Dependências Node.js
├── vercel.json        # Configuração do Vercel
└── .env.example       # Exemplo de variáveis de ambiente
```

## Tecnologias

- **Python 3.x**: Linguagem principal
- **Celery**: Framework de tarefas assíncronas
- **Redis**: Message broker e cache
- **Vercel**: Hospedagem e analytics
- **Node.js**: Runtime para ferramentas de build

## Licença

© 2026 LJCF - Todos os direitos reservados
