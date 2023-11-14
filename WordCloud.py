import pandas as pd
from wordcloud import WordCloud
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

# Descarga las stopwords (puedes omitir esta línea si ya las tienes descargadas)
import nltk
nltk.download('stopwords')

# Carga tus datos desde el archivo CSV
df = pd.read_csv('TransporteNL_Limpio.csv')

# Define las stopwords en español
stop_words = set(stopwords.words('spanish'))

# Define una función para dividir las cadenas en palabras y filtrar las stopwords
def process_text(text):
    words = str(text).split()
    return ' '.join([word.lower() for word in words if word.lower() not in stop_words])

# Aplica la función a la columna 'TRANSPORTE'
df['processed_text'] = df['TRANSPORTE'].apply(process_text)

# Concatena todas las palabras procesadas en una sola cadena
text = ' '.join(df['processed_text'])

# Crea la nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Muestra la nube de palabras utilizando matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
