# corujai-platform
Plataforma de Análise de Dados para Inteligência Policial

# 🦉 CORUJAI  
*Plataforma de Análise de Dados para Inteligência Policial*  

![Logo CorujAI](docs/logo_corujai.png)  

## 🚀 Recursos  
- Coleta de dados de redes sociais.  
- Detecção de ameaças com NLP em PT-BR.  
- Dashboard interativo.

- /policia-inteligencia-opensource  
│  
├── /coleta-de-dados/                # Scripts para extração de dados  
│   ├── twitter_scraper.py            # Usando snscrape (sem API)  
│   ├── reddit_collector.py           # Via PRAW (API oficial)  
│   └── news_fetcher.py               # RSS e Newspaper3k  
│  
├── /processamento-nlp/               # Limpeza e análise de texto  
│   ├── preprocessamento.py           # spaCy/NLTK para PT-BR  
│   ├── modelo_ameacas.py             # Fine-tuning BERTimbau  
│   └── fasttext_model.py             # Alternativa leve  
│  
├── /armazenamento/                   # Bancos de dados e cache  
│   ├── postgres_setup.sh             # Configuração do PostgreSQL  
│   └── minio_docker.yml              # MinIO (S3 open-source)  
│  
├── /visualizacao/                    # Dashboards  
│   ├── streamlit_app.py              # Protótipo interativo  
│   └── metabase_dashboard.sql        # Consultas para BI  
│  
├── /infra/                           # Deploy e automação  
│   ├── Dockerfile                    # Containerização  
│   ├── docker-compose.yml            # Airflow + PostgreSQL  
│   └── README.md                     # Guia de deploy  
│  
├── LICENSE                           # Licença MIT  
└── README.md                         # Documentação do projeto


