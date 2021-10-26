from typing import Any, Dict, Generator, List, Optional, Union

from aiomeilisearch.config import Config
from datetime import datetime
from aiomeilisearch._http_client import HttpClient

class Index():
    """

    """
    def __init__(self,
                 config: Config,
                 uid: str,
                 primary_key: Optional[str] = None,
                 created_at: Optional[Union[datetime, str]] = None,
                 updated_at: Optional[Union[datetime, str]] = None,
                 ) -> None:
        self.config = config
        self.http = HttpClient(config)
        self.uid = uid
        self.primary_key = primary_key
        self.created_at = self._iso_to_date_time(created_at)
        self.updated_at = self._iso_to_date_time(updated_at)

    @staticmethod
    def _iso_to_date_time(iso_date: Optional[Union[datetime, str]]) -> Optional[datetime]:
        """
        MeiliSearch returns the date time information in iso format. Python's implementation of
        datetime can only handle up to 6 digits in microseconds, however MeiliSearch sometimes
        returns more digits than this in the micosecond sections so when that happens this method
        reduces the number of microseconds so Python can handle it. If the value passed is either
        None or already in datetime format the original value is returned.
        """
        if not iso_date:
            return None

        if isinstance(iso_date, datetime):
            return iso_date

        try:
            return datetime.strptime(iso_date, "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            split = iso_date.split(".")
            reduce = len(split[1]) - 6
            reduced = f"{split[0]}.{split[1][:-reduce]}Z"
            return datetime.strptime(reduced, "%Y-%m-%dT%H:%M:%S.%fZ")

    async def fetch_info(self) -> 'Index':
        """
        Fetch the info of the index.
        """
        return await self.get()

    async def get_raw(self)-> Dict:
        """
        :return:  An index in dictionary format. (e.g { 'uid': 'movies' 'primaryKey': 'objectID' })
        """
        path = "/indexes/{0}".format(self.uid)
        index_dict = await self.http.get(path)
        return index_dict

    async def get(self)-> 'Index':
        index_dict = await self.get_raw()
        self.primary_key = index_dict['primaryKey']
        self.created_at = self._iso_to_date_time(index_dict['createdAt'])
        self.updated_at = self._iso_to_date_time(index_dict['updatedAt'])
        return self

    async def update(self, **options: Optional[Dict[str, Any]]) -> 'Index':
        """
        Update an index.
        :param options:
            - primaryKey: The primary key of the documents,
                          The primaryKey can be added if it does not exist,
                          if primaryKey already exists, will raise Error
        :return:
        """
        if not options:
            # todo raise error
            return
        path = "/indexes/{0}".format(self.uid)
        index_dict = await self.http.put(path, json_=options)
        self.primary_key = index_dict['primaryKey']
        self.created_at = self._iso_to_date_time(index_dict['createdAt'])
        self.updated_at = self._iso_to_date_time(index_dict['updatedAt'])
        return self

    async def delete(self)-> None:
        """
        Delete an index
        :return: None
        """
        path = "/indexes/{0}".format(self.uid)
        await self.http.delete(path)

    async def delete_if_exists(self) -> bool:
        """Deletes the index if it already exists
        Returns True if an index was deleted or False if not
        """
        try:
            await self.delete()
            return True
        # todo raise
        # except MeiliSearchApiError as error:
        #     if error.error_code != "index_not_found":
        #         raise error
        #     return False
        except:
            raise
