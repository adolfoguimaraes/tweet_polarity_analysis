import time
import os
import csv
import configparser
import botometer
import pickle


class Analyser:

    def __init__(self, config_file):
        config = configparser.RawConfigParser()
        config.read(config_file)

        BOTOMETER_KEY = config['BOTOMETER']['API_KEY']

        TWITTER_KEY = config['TWITTER']['CONSUMER_KEY']
        TWITTER_SECRET = config['TWITTER']['CONSUMER_SECRET']

        twitter_app_auth = {
            'consumer_key': TWITTER_KEY,
            'consumer_secret': TWITTER_SECRET
        }

        self.bot = botometer.Botometer(wait_on_ratelimit=True,
                                rapidapi_key=BOTOMETER_KEY,
                                **twitter_app_auth)


    def analyser_users(self, ids, output_file):
        # Verifica se existe um arquivo de progresso anterior
        progress_file = "progress.pickle"
        if os.path.isfile(progress_file):
            with open(progress_file, "rb") as f:
                progress = pickle.load(f)
        else:
            progress = set()

        results = {}

        # Faz a análise dos IDs
        for i, id in enumerate(ids):
            # Verifica se o ID já foi analisado antes
            if id in progress:
                continue

            try:
                # Faz a chamada para a API do Botometer para analisar a probabilidade do perfil ser um bot
                result = self.bot.check_account(id)
                results[id] = result
                progress.add(id)
            except Exception as e:
                print(f"Erro ao analisar o perfil {id}: {e}")
                continue

            # Salva o progresso a cada 100 análises
            if i % 100 == 0:
                with open(progress_file, "wb") as f:
                    pickle.dump(progress, f)

            # Faz um mecanismo de espera se atingir o limite de taxa de chamada da API
            if 'reset' in self.bot.api.last_response.headers:
                reset = int(self.bot.api.last_response.headers['reset'])
                remaining = int(self.bot.api.last_response.headers['x-rate-limit-remaining'])
                if remaining <= 1:
                    wait_time = max(reset - time.time(), 0) + 5
                    print(f"Esperando {wait_time} segundos para continuar a análise")
                    time.sleep(wait_time)

        # Salva os resultados em um arquivo CSV
        with open(output_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "scores", "categories"])
            for id, result in results.items():
                scores = result["scores"]
                categories = result["categories"]
                writer.writerow([id, scores, categories])
        
        # Remove o arquivo de progresso
        # os.remove(progress_file)
        
        return results




if __name__ == "__main__":

    analyser = Analyser("config.ini")



