import aiomeilisearch
import asyncio, json

Host = '127.0.0.1'
Port = '7700'
MasterKey = '123456'

client = aiomeilisearch.Client('http://{0}:{1}'.format(Host, Port), apiKey=MasterKey, )

def console(json_data):
    print(json.dumps(json_data, indent=2, ensure_ascii=False,))

class DemoIndexSetting(object):
    async def get_settings(self):
        # indexes = await client.get_indexes()
        settings = await client.index('movies').get_settings()
        console(settings)

    async def update_settings(self):
        status = await client.index('movies').update_settings({
            'sortableAttributes': [ "id", "is_kv", ],
        })
        console(status)

    async def reset_settings(self):
        status = await client.index('movies').reset_settings()
        console(status)

    async def get_displayed_attributes(self):
        # indexes = await client.get_indexes()
        settings = await client.index('movies').get_displayed_attributes()
        console(settings)

    async def update_displayed_attributes(self):
        status = await client.index('movies').update_displayed_attributes(["id", 'title', 'year'])
        console(status)

    async def reset_displayed_attributes(self):
        status = await client.index('movies').reset_displayed_attributes()
        console(status)

    async def get_distinct_attribute(self):
        # indexes = await client.get_indexes()
        settings = await client.index('movies').get_distinct_attribute()
        console(settings)

    async def update_distinct_attribute(self):
        status = await client.index('movies').update_distinct_attribute("id")
        console(status)

    async def reset_distinct_attribute(self):
        status = await client.index('movies').reset_distinct_attribute()
        console(status)

    async def get_filterable_attributes(self):
        # indexes = await client.get_indexes()
        settings = await client.index('movies').get_filterable_attributes()
        console(settings)

    async def update_filterable_attributes(self):
        status = await client.index('movies').update_filterable_attributes(["year", 'is_tv'])
        console(status)

    async def reset_filterable_attributes(self):
        status = await client.index('movies').reset_filterable_attributes()
        console(status)

    async def get_ranking_rules(self):
        # indexes = await client.get_indexes()
        settings = await client.index('movies').get_ranking_rules()
        console(settings)

    async def update_ranking_rules(self):
        status = await client.index('movies').update_ranking_rules(['words',
                                                                    'typo',
                                                                    'proximity',
                                                                    'attribute',
                                                                    'sort',
                                                                    'exactness',
                                                                    'release_date:asc',
                                                                    'rank:desc'])
        console(status)

    async def reset_ranking_rules(self):
        status = await client.index('movies').reset_ranking_rules()
        console(status)

    async def get_searchable_attributes(self):
        # indexes = await client.get_indexes()
        settings = await client.index('movies').get_searchable_attributes()
        console(settings)

    async def update_searchable_attributes(self):
        status = await client.index('movies').update_searchable_attributes(['title',
                                                                    'original_title', ])
        console(status)

    async def reset_searchable_attributes(self):
        status = await client.index('movies').reset_searchable_attributes()
        console(status)

    async def get_sortable_attributes(self):
        # indexes = await client.get_indexes()
        settings = await client.index('movies').get_sortable_attributes()
        console(settings)

    async def update_sortable_attributes(self):
        status = await client.index('movies').update_sortable_attributes(['year'])
        console(status)

    async def reset_sortable_attributes(self):
        status = await client.index('movies').reset_sortable_attributes()
        console(status)

    async def get_stop_words(self):
        # indexes = await client.get_indexes()
        settings = await client.index('movies').get_stop_words()
        console(settings)

    async def update_stop_words(self):
        status = await client.index('movies').update_stop_words(['of', 'the', 'to'])
        console(status)

    async def reset_stop_words(self):
        status = await client.index('movies').reset_stop_words()
        console(status)

    async def get_synonyms(self):
        # indexes = await client.get_indexes()
        settings = await client.index('movies').get_synonyms()
        console(settings)

    async def update_synonyms(self):
        status = await client.index('movies').update_synonyms({
              'wolverine': ['xmen', 'logan'],
              'logan': ['wolverine', 'xmen'],
              'wow': ['world of warcraft']
            })
        console(status)

    async def reset_synonyms(self):
        status = await client.index('movies').reset_synonyms()
        console(status)

if __name__ == '__main__':
    t = DemoIndexSetting()
    loop = asyncio.new_event_loop()
    loop.run_until_complete( t.get_settings() )
    # loop.run_until_complete( t.update_settings() )
    # loop.run_until_complete( t.reset_settings() )

    # loop.run_until_complete(t.get_displayed_attributes())
    # loop.run_until_complete( t.update_displayed_attributes() )
    # loop.run_until_complete( t.reset_displayed_attributes() )

    # loop.run_until_complete(t.get_distinct_attribute())
    # loop.run_until_complete( t.update_distinct_attribute() )
    # loop.run_until_complete( t.reset_distinct_attribute() )

    # loop.run_until_complete( t.get_filterable_attributes())
    # loop.run_until_complete( t.update_filterable_attributes() )
    # loop.run_until_complete( t.reset_filterable_attributes() )

    # loop.run_until_complete( t.get_ranking_rules())
    # loop.run_until_complete( t.update_ranking_rules() )
    # loop.run_until_complete( t.reset_ranking_rules() )

    # loop.run_until_complete( t.get_searchable_attributes())
    # loop.run_until_complete( t.update_searchable_attributes() )
    # loop.run_until_complete( t.reset_searchable_attributes() )

    # loop.run_until_complete( t.get_sortable_attributes())
    # loop.run_until_complete( t.update_sortable_attributes() )
    # loop.run_until_complete( t.reset_sortable_attributes() )

    # loop.run_until_complete(t.get_stop_words())
    # loop.run_until_complete( t.update_stop_words() )
    # loop.run_until_complete( t.reset_stop_words() )

    # loop.run_until_complete(t.get_synonyms())
    # loop.run_until_complete( t.update_synonyms() )
    # loop.run_until_complete( t.reset_synonyms() )
