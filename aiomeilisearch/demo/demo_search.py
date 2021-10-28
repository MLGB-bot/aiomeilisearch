import aiomeilisearch
import asyncio
import json

Host = '127.0.0.1'
Port = '7700'
MasterKey = '123456'

client = aiomeilisearch.Client('http://{0}:{1}'.format(Host, Port), apiKey=MasterKey, )

a = """
[
    {
      "id": "10428481",
      "title": "永远之永恒 第五章 双绝的来复",
      "original_title": "トワノクオン 第五章 双絶の来復",
      "is_tv": False,
      "year": "2011",
      "poster": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p1414439672.webp"
    },
    {
      "id": "10428497",
      "title": "鸟瞰地球",
      "original_title": "Earthflight",
      "is_tv": True,
      "year": "2011",
      "poster": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2172206661.webp"
    },
    {
      "id": "10428501",
      "title": "新·福音战士剧场版：终",
      "original_title": "シン・エヴァンゲリオン劇場版:│▌",
      "is_tv": False,
      "year": "2021",
      "poster": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2629054917.webp"
    },
    {
      "id": "10428503",
      "title": "摇曳百合2",
      "original_title": "ゆるゆり♪♪",
      "is_tv": True,
      "year": "2012",
      "poster": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2257382779.webp"
    },
    {
      "id": "10429695",
      "title": "灵动：鬼影实录4",
      "original_title": "Paranormal Activity 4",
      "is_tv": False,
      "year": "2012",
      "poster": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p1655123188.webp"
    },
    {
      "id": "10430281",
      "title": "七个隆咚锵咚锵",
      "original_title": "",
      "is_tv": False,
      "year": "2012",
      "poster": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p1377187455.webp"
    },
    {
      "id": "10430284",
      "title": "一起一起这里那里",
      "original_title": "あっちこっち",
      "is_tv": True,
      "year": "2012",
      "poster": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2333656770.webp"
    },
    {
      "id": "10430287",
      "title": "故宫100——看见看不见的紫禁城",
      "original_title": "",
      "is_tv": True,
      "year": "2012",
      "poster": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p1703904586.webp"
    },
    {
      "id": "10430313",
      "title": "飞天大盗  第八季",
      "original_title": "Hustle Season 8",
      "is_tv": True,
      "year": "2012",
      "poster": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2247278688.webp"
    },
    {
      "id": "10430332",
      "title": "迷失 特别篇 最终旅途",
      "original_title": "Lost: The Final Journey",
      "is_tv": False,
      "year": "2010",
      "poster": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2501802150.webp"
    }
]
"""
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
    loop.run_until_complete(t.search_sort())
