import aiomeilisearch
import asyncio

Host = '127.0.0.1'
Port = '7700'
MasterKey = '123456'

client = aiomeilisearch.Client('http://{0}:{1}'.format(Host, Port), apiKey=MasterKey, )

class DemoIndex(object):
    async def get_indexes(self):
        indexes = await client.get_indexes()
        print("indexes: ", indexes)
        assert isinstance(indexes, list)

    async def get_one_index(self):
        index_ = await client.get_index('movies')
        # index_ = await client.get_raw_index('movies')
        print("1", index_)

    async def create_index(self):
        index_ = await client.create_index('movies', {'primaryKey': 'id'})
        print("create_index", index_)

    async def update_index(self):
        index_ = await client.index('movies').update(primary_key='movie_id')
        print("update_index", index_)

    async def delete_index(self):
        index_ = await client.index('movies').delete()
        print("delete_index", index_)

if __name__ == '__main__':
    t = DemoIndex()
    loop = asyncio.new_event_loop()
    # loop.run_until_complete( t.get_indexes() )
    # loop.run_until_complete( t.get_one_index() )
    loop.run_until_complete( t.create_index() )
    # loop.run_until_complete( t.update_index() )
    # loop.run_until_complete( t.delete_index() )
