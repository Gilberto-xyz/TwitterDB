# Obtener twits mediante snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd
from textblob import TextBlob

# Definir parámetros de búsqueda
consulta = "(otan, OR Zelensky) lang:en"
datos = []
limite = 50_000

# Obtener twits
for tweet in sntwitter.TwitterSearchScraper(consulta).get_items():
    
    if len(datos) == limite:
        break
    else:
        # Obtener sentimiento y polaridad
        blob = TextBlob(tweet.rawContent)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # imprimir el numero de twits obtenidos hasta el momento
        print(len(datos), end='\r')
        datos.append([tweet.date, tweet.user.username, tweet.rawContent, polarity, subjectivity])

# Crear dataframe
df = pd.DataFrame(datos, columns=['Date', 'User', 'Tweet', 'Polarity', 'Subjectivity'])

# Exportar a csv
df.to_csv('Oscars.csv', index=False)