import aiomeilisearch
import asyncio
import json

Host = '127.0.0.1'
Port = '7700'
MasterKey = '123456'

client = aiomeilisearch.Client('http://{0}:{1}'.format(Host, Port), apiKey=MasterKey, )

def console(json_data):
    print(json.dumps(json_data, indent=2, ensure_ascii=False,))

class DemoSearch(object):
    async def search1(self):
        result = await client.index("movies").search(query='飞天大盗')
        # result = await client.index("movies").search(query='Hustle 飞天大盗')
        console(result)

    async def update_filterable_attribute(self):
        resp = await client.index('movies').update_filterable_attributes(["year", 'is_tv'])

    async def search_filter(self):
        # result = await client.index("movies").search(query='飞天大盗', filter=["year=2012"])
        result = await client.index("movies").search(query='飞天大盗', filter=["is_tv=False", ["year='1994'", "year='2006'"]])
        console(result)

    async def search_facets(self):
        # result = await client.index("movies").search(query='飞天大盗', facetsDistribution=['is_tv'])
        result = await client.index("movies").search('飞天大盗', {'facetsDistribution': ['is_tv', 'year']})
        console(result)

    async def search_attributesToRetrieve(self):
        # limit attributes
        # result = await client.index("movies").search(query='飞天大盗', facetsDistribution=['is_tv'])
        result = await client.index("movies").search('飞天大盗', {'attributesToRetrieve': ["id", "title", 'is_tv', 'year']})
        console(result)

    async def search_attributesToCrop(self):
        # limit attributes
        result = await client.index("movies").search('飞天大盗',
                                                     {
                                                          'attributesToCrop': ['original_title'],
                                                          'cropLength': 8
                                                     })
        console(result)


    async def search_attributesToHighlight(self):
        # limit attributes
        result = await client.index("movies").search('飞天大盗',
                                                     {
                                                          'attributesToHighlight': ['title', 'original_title']
                                                     })
        console(result)

    async def search_match(self):
        # limit attributes
        result = await client.index("movies").search('飞天大盗',
                                                     {
                                                          'matches': True
                                                     })
        console(result)

    async def update_sortable_attributes(self):
        result = await client.index("movies").update_sortable_attributes([ 'id', 'year', 'is_kv'  ] )
        console(result)

    async def get_sortable_attributes(self):
        result = await client.index("movies").get_sortable_attributes( )
        console(result)


    async def search_sort(self):
        # limit attributes
        result = await client.index("movies").search('飞天大盗',
                                                     {
                                                          'sort': ['is_kv:desc']
                                                     })
        console(result)

if __name__ == '__main__':
    t = DemoSearch()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(t.search1())
    # loop.run_until_complete(t.update_filterable_attribute())
    # loop.run_until_complete(t.search_filter())
    # loop.run_until_complete(t.search_facets())
    # loop.run_until_complete(t.search_attributesToRetrieve())
    # loop.run_until_complete(t.search_attributesToCrop())
    # loop.run_until_complete(t.search_attributesToHighlight())
    # loop.run_until_complete(t.search_match())
    # loop.run_until_complete(t.update_sortable_attributes())
    # loop.run_until_complete(t.get_sortable_attributes())
    # loop.run_until_complete(t.search_sort())
