import requests
s=0
while True:
    Token='the Token of your bot'
    url=f'https://api.telegram.org/bot{Token}/getUpdates'
    response=requests.get(url=url)
    response=response.json()['result']
    n=len(response)
    while n>s:
        s=n
        i=response[-1]
        url1=f'https://api.telegram.org/bot{Token}/sendMessage'
        chat_id=i['message']['chat']['id']
        text=i['message']['text']
        reply=i['message']['message_id']
        pyload={
            'chat_id':chat_id,
            'text':text,
            'reply_to_message_id':reply
        }
        j=requests.get(url=url1,params=pyload)


