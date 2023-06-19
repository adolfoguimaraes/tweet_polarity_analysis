# Sentiment and Polarity Analysis on Twitter Data

Repositório contendo conjunto de dados utilizados para treino e teste dos algoritmos de machine learning: Naive Bayes, SVM e BERT. Esse projeto faz parte do estudo realizado para o meu trabalho de conclusâo de curso de Ciências da Computação na Universidade Tiradentes (UNIT).

![Pipeline_johnny](https://github.com/Jownao/tweet_polarity_analysis/assets/50759662/43786ccb-91f9-46c8-aeb8-78b5e36666dc)


Foi realizado um estudo em que foram coletadas mensagens do Twitter entre as 13:00 e 00:00 do dia 8 de janeiro de 2023. Esses dados foram utilizados para criar um subconjunto de treinamento e teste, a fim de classificar os textos, enquanto o restante foi utilizado para realizar uma análise geral de sentimentos e polaridade. Em breve, será possível acessar o meu texto contendo os resultados da análise realizada.

### Objetivos

##### Geral
Analisar a reação da população à manifestação, identificando de forma imparcial seus principais sentimentos e opiniões para compreender seu impacto político e social,  e contribuir fornecendo informações adicionais sobre o evento.

##### Específicos
Para alcançar o objetivo geral, delineiam-se os seguintes objetivos específicos compreendidos nesse projeto:

* Elaborar uma pipeline de coleta e análise com um conjunto representativo de tweets relacionados ao ocorrido, usando ferramentas de mineração de dados e análise de texto;
* Identificar os temas mais frequentes e relevantes nos tweets, como reivindicações políticas, sociais ou econômicas, apoio ou não as ações feitas, etc;
* Classificar os tweets de acordo com o sentimento expresso pelos usuários, por exemplo, positivo, negativo ou neutro, para entender a polarização das opiniões e as percepções sobre a tentativa de golpe;
* Identificar os usuários mais influentes na discussão sobre a revolta com grafos,gráficos, etc,  avaliando o número de seguidores, retweets e respostas recebidas;
* Identificar o papel das redes sociais na organização e mobilização da tentativa, avaliando a proporção de tweets que mencionam hashtags específicas, como #ForaBolsonaro, #grevegeral, etc;


### Estruturação do repositório

```
|- scripts
  |- botometer
    |- analyser.py
    |- config.ini
    |- main.py
|- utils
  |- random.py
|- LICENSE
|- README.md
|- Sentiment_analysis.ipynb
|- search_archive.py
|- utils_convert.py



```

### Dicionário dos datasets
#### Tweets

- **tweet_id:** identificador único que representa um tweet no Twitter.
- **created_at:** data e hora em que o tweet foi criado no formato "aaaa-mm-ddThh:mm:ss".
- **retweet_count:** número de vezes que o tweet foi retweetado por outros usuários.
- **reply_count:** número de vezes que o tweet foi respondido por outros usuários.
- **like_count:** número de vezes que o tweet foi curtido por outros usuários.
- **quote_count:** número de vezes que o tweet foi citado por outros usuários em seus próprios tweets.
- **mentions:** lista de usuários do Twitter mencionados no tweet.
- **hashtags:** lista de hashtags usadas no tweet.

#### Usuários

- **user_id:** identificador único para cada usuário da rede social.
- **tweets_ids:** lista dos identificadores únicos de cada tweet que o usuário postou.
- **followers_count:** número de seguidores do usuário.
- **following_count:** número de contas que o usuário está seguindo.
- **tweet_count:** número de tweets que o usuário postou.
- **listed_count:** número de listas nas quais o usuário está incluído.
- **is_verified:** indica se o usuário é uma conta verificada (true) ou não (false).
- **profile_created_at:** data em que o perfil do usuário foi criado na rede social.



