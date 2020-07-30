# asuna
heoll word

def base_request(url, json=None, headers=None, **kwargs):
    result = None

    logger.info('request: {}'.format(url))
    if json:
        result = requests.post(
            url=url, json=json, headers=headers,
            timeout=30,
            **kwargs).json()
    elif json == {}:
        result = requests.post(
            url=url, json=json, headers=headers,
            timeout=30,
            **kwargs).json()
    else:
        result = requests.get(url=url, json=json, headers=headers).json()

    logger.debug('response: {}'.format(result))
    return result
