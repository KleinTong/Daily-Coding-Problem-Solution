import requests


def main():
    print(r"b5)Py3]Qwrc+D[he")
    proxies = {
        'http': r'socks5://root:{}@140.82.11.73:18891'.format(r"b5)Py3]Qwrc+D[he"),
        'https': r'socks5://root:{}@140.82.11.73:18891'.format(r"b5)Py3]Qwrc+D[he")
    }
    # proxies = {
    #     'http': 'socks5://127.0.0.1:1080',
    #     'https': 'socks5://127.0.0.1:1080'
    # }
    r = requests.get('https://facebook.com', proxies=proxies)
    # r = requests.get('https://zhihu.com', proxies=proxies)
    # r = requests.get('https://zhihu.com')
    print('yes')


if __name__ == '__main__':
    main()
