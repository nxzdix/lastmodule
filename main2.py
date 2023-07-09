import random
import vk_api

token = 'vk1.a.zKx0C6NQd0Y8LcFE_l5X47uBuVRxnpbMMn9JIRxEiRVlVoHMYysy-xhNuV78yQ2SA9pfzhWFX_IWbvAo0KRaV6mMQGns7TbLAt8KLBewAiYrNFSjlpVzkOvIrl6Dx_zCB-7intyo8r_ZZdQwTyvyh8VE_SdLAE-bIoHojLIrMoQrweCoC9SQP_0bwZkbq60PQOJOrrqWEFewNxN8hnMNeg'
vk = vk_api.VkApi(token=token)

while True:
    messages = vk.method('messages.getConversations', {'filter': 'unanswered'})
    if messages ['count'] > 0:
        user_messages = messages['items'][0]['last_message']['text']
        user_id = messages['items'][0]['last_message']['from_id']

    vk.method(
        'messages.send',
        {
            'random_id': random.randint(-10 ** 7, 10 ** 7),
            'message': user_messages,
            'user_id': user_id
        }
    )

