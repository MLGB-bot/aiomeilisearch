import aiomeilisearch
import asyncio

Host = '127.0.0.1'
Port = '7700'
MasterKey = '123456'

client = aiomeilisearch.Client('http://{0}:{1}'.format(Host, Port), apiKey=MasterKey, )


class DemoDocument(object):
    async def add_documents(self):
        status = await client.index('movies').add_documents([{
          'id': 287947,
          'title': 'Shazam',
          'poster': 'https://image.tmdb.org/t/p/w1280/xnopI5Xtky18MPhK40cZAGAOVeV.jpg',
          'overview': 'A boy is given the ability to become an adult superhero in times of need with a single magic word.',
          'release_date': '2019-03-23'
        }])
        print("add_documents", status)

    async def update_documents(self):
        status = await client.index('movies').update_documents([{
            'id': 287947,
            'title': 'Shazam ⚡️',
            'genres': 'comedy'
        }])
        print(status)

    async def get_documents(self):
        documents = await client.index('movies').get_documents({'limit':10})
        print(documents)

    async def get_document(self):
        document = await client.index('movies').get_document(10430313)
        print(document)

    async def demo_add(self):
        # movies = [
        #     {
        #         "id": i,
        #         "title": "title {0}".format(i)
        #     } for i in range(10)
        # ]
        import json
        with open('movies.json', 'r') as f:
            datas = f.read()
            movies = json.loads(datas)
            await client.index('movies').add_documents(movies)

    async def delete_document(self, _id):
        print( await client.index('movies').delete_document(_id) )

    async def delete_documents(self, _ids):
        print(await client.index('movies').delete_documents( _ids ))

    async def delete_all_documents(self):
        print(await client.index('movies').delete_all_documents(  ))

if __name__ == '__main__':
    t = DemoDocument()
    loop = asyncio.new_event_loop()
    # loop.run_until_complete(t.add_documents())
    # loop.run_until_complete(t.update_documents())
    # loop.run_until_complete(t.delete_document(0))
    # loop.run_until_complete(t.delete_documents( [1,2,3] ))
    # loop.run_until_complete(t.delete_all_documents( ))
    # loop.run_until_complete(t.get_documents())
    loop.run_until_complete(t.get_document())
    # loop.run_until_complete(t.demo_add())