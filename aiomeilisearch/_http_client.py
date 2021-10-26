import aiohttp
from urllib.parse import urljoin
from aiomeilisearch.config import Config

class HttpClient():
    def __init__(self, config: Config) -> None:
        self.config = config
        if config.api_key:
            self.headers = {
                'X-Meili-Api-Key': config.api_key,
            }
        else:
            self.headers = {}

    async def _handle_resp(self, response):
        response.raise_for_status()
        try:
            return await response.json()
        except:
            return await response.content

    async def get(self, path, args=None):
        url = urljoin(self.config.url, path)
        params = {}
        if self.config.timeout:
            params['timeout'] = self.config.timeout
        if self.headers:
            params['headers'] = self.headers
        if args:
            params['args'] = args
        async with aiohttp.ClientSession() as session:
            async with session.get(url, **params) as response:
                data = await self._handle_resp(response)
                return data

    async def post(self, path, json_=None):
        url = urljoin(self.config.url, path)
        params = {}
        if self.config.timeout:
            params['timeout'] = self.config.timeout
        if self.headers:
            params['headers'] = self.headers
        if json_:
            params["json"] = json_
        async with aiohttp.ClientSession() as session:
            async with session.post(url, **params) as response:
                data = await self._handle_resp(response)
                return data

    async def put(self, path, json_=None):
        url = urljoin(self.config.url, path)
        params = {}
        if self.config.timeout:
            params['timeout'] = self.config.timeout
        if self.headers:
            params['headers'] = self.headers
        if json_:
            params["json"] = json_
        async with aiohttp.ClientSession() as session:
            async with session.put(url, **params) as response:
                data = await self._handle_resp(response)
                return data

    async def delete(self, path):
        url = urljoin(self.config.url, path)
        params = {}
        if self.config.timeout:
            params['timeout'] = self.config.timeout
        if self.headers:
            params['headers'] = self.headers
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, **params) as response:
                response.raise_for_status()
                return
