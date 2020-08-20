import robin_stocks as r

'''
This is an example script that will show you how to close option positions.
'''

#!!! Fill out username and password
username = '************'
password = '************'
#!!!

login = r.login(username, password)

symbol = 'DOGE'

cryptoList = r.get_crypto_quote(symbol)

print(cryptoList)


