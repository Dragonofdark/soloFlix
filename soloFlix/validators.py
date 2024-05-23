import urllib.parse

def url_valido(url):
  try:
    result = urllib.parse.urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False

def titulo_valido(titulo):
   return titulo.isalpha()