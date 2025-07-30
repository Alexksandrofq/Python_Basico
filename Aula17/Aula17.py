import oauth2
import urllib.parse
import json 

class Twitter:

    def ___init___(self, consumer_key, consumer_secret, token_key, token_secret):
        self.conexao(consumer_key, consumer_secret, token_key, token_secret)

    def conexao(self, consumer_key, consumer_secret, token_key, token_secret):
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(self.consumer, self.token)
    
    def tweet(self, novo_tweet):
        query_codificada = urllib.parse.quote(novo_tweet, safe='')
        requisicao = self.cliente.request('' + query_codificada, method='POST')

        decodificar = requisicao[1].decode()

        objeto = json.loads(decodificar)
        return objeto 

    def search(self, query, lang):
        query_codificada = urllib.parse.quote(query, safe='')
        requisicao = self.cliente.request('' + query_codificada, method='POST')

        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        twittes = objeto['statuses']
        return twittes




#testar
from twitter import Twitter

consumer_key =''
consumer_secret =''

token_key =''
token_secret =''

twitter = Twitter(consumer_key, consumer_secret, token_key, token_secret)

resp = twitter.tweet('Vamos testar nossa lib')

pesquisa = twitter.search('solyd', 'pt')

for resultado in pesquisa:
    print(resultado['text'])
    print(resultado['user'] ['screen_name'])