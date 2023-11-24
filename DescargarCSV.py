from urllib import request


remote_url = 'https://www.inegi.org.mx/contenidos/programas/transporteurbano/datosabiertos/etup_mensual_csv.zip'

local_file = 'etup_mensual_csv.zip' 

request.urlretrieve(remote_url, local_file)