import aiomeilisearch
import asyncio, json

Host = '127.0.0.1'
Port = '7700'
MasterKey = '123456'

client = aiomeilisearch.Client('http://{0}:{1}'.format(Host, Port), apiKey=MasterKey, )

def console(json_data):
    print(json.dumps(json_data, indent=2, ensure_ascii=False,))

class DemoClient(object):

    async def get_update_status(self):
        update = await client.index('movies').get_update_status(1)
        console(update)

    async def get_all_update_status(self):
        updates = await client.index('movies').get_all_update_status()
        console(updates)

    async def get_keys(self):
        update = await client.get_keys()
        console(update)

    async def get_stats(self):
        stats = await client.index('movies').get_stats()
        console(stats)

    async def get_all_stats(self):
        stats = await client.get_all_stats()
        console(stats)

    async def health(self):
        health = await client.health()
        console(health)

    async def get_version(self):
        version = await client.get_version()
        console(version)

    async def create_dump(self):
        status = await client.create_dump()
        console(status)

    async def get_dump_status(self, dump_id):
        status = await client.get_dump_status(dump_id)
        console(status)


if __name__ == '__main__':
    t = DemoClient()
    loop = asyncio.new_event_loop()
    # loop.run_until_complete( t.get_update_status() )
    # loop.run_until_complete( t.get_all_update_status() )
    # loop.run_until_complete( t.get_keys() )
    # loop.run_until_complete( t.get_stats() )
    # loop.run_until_complete( t.get_all_stats() )
    # loop.run_until_complete( t.health() )
    # loop.run_until_complete( t.get_version() )
    # loop.run_until_complete( t.create_dump() )
    loop.run_until_complete( t.get_dump_status("20211028-093739606") )
