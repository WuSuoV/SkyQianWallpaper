import requests


class pictrue:
    def __init__(self):
        pass

    def default(self, cid=36, start=0, count=10):
        if start is None: start = 0
        if count is None: count = 10
        if cid is None: cid = 36
        url = f"http://wp.birdpaper.com.cn/intf/GetListByCategory?cids={cid}&pageno={start}&count={count}"
        response = requests.get(url=url, timeout=5, verify=False)
        return response.json()

    def i360new(self, start=0, count=10):
        if start is None:
            start = 0
        if count is None:
            count = 10
        url = f"http://wp.birdpaper.com.cn/intf/newestList?pageno={start}&count={count}"
        response = requests.get(url=url, timeout=5, verify=False)
        return response.json()

    def i360tags(self):
        url = f"http://wp.birdpaper.com.cn/intf/getCategory"
        response = requests.get(url=url, timeout=5, verify=False)
        return response.json()

    def bing(self, start=-1, count=8):
        if start is None:
            start = -1
        if count is None:
            count = 8

        url = f"http://cn.bing.com/HPImageArchive.aspx?format=js&idx={start}&n={count}"
        response = requests.get(url=url, timeout=5, verify=False)
        return response.json()

    def i360search(self, content='', start=0, count=10):
        if start is None:
            start = 0
        if count is None:
            count = 10
        if content is None:
            content = ''

        url = f"http://wp.birdpaper.com.cn/intf/search?content={content}&pageno={start}&count={count}"
        response = requests.get(url=url, timeout=5, verify=False)
        return response.json()
