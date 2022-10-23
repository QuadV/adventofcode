import urllib.request


def read_link(link):
    import requests

    x = requests.get(link)
    print(x.text)


def read_file(path):
    with open(path, 'r') as f_out:
        data = f_out.readlines()
    return data
