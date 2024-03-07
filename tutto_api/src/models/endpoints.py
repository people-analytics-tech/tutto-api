"""Class to represent the endpoints of Tutto API"""

import asyncio

from dataclasses import dataclass, field
from operator import itemgetter
from abc import ABC, abstractmethod
from tutto_api.src.helpers.http import HTTPRequest


@dataclass(init=False, frozen=True, slots=True)
class Endpoint(ABC):
    http_client: HTTPRequest = field()
    bearer_token: str = field()

    @abstractmethod
    def call(self) -> dict:
        pass


class EndpointFactory:
    @staticmethod
    def create_endpoint(
        base_url: str, endpoint: str, bearer_token: str, **kwargs
    ) -> Endpoint:
        """Factory method to create an endpoint object"""
        endpoints = {
            "deductions": Deductions,
        }
        endpoint_class = endpoints.get(endpoint)
        if endpoint_class:
            http_client = HTTPRequest(base_url=base_url)
            return endpoint_class(
                http_client=http_client, bearer_token=bearer_token, **kwargs
            )


### Endpoints ###
# GET
@dataclass(init=True, frozen=True, slots=True)
class Deductions(Endpoint):
    """Class to handle the 'deductions' endpoint.\n
    Args:
        reference (str, required): Reference period in AAAAMM date format.
        type (str, optional): Deductions type.
        start_date (str, optional): Deductions start date in AAAAMMDD date format.
        end_date (str, optional): Deductions end date in AAAAMMDD date format.
        id (int, optional): Deductions FOPAG ID.
    """

    http_client: HTTPRequest = field()
    bearer_token: str = field()

    reference: str = field()
    type: str = field(default="")
    start_date: str = field(default="")
    end_date: str = field(default="")
    id: int = field(default=0)

    def call(self) -> dict:
        payload = {
            "reference": self.reference,
            "type": self.type,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "id": self.id,
        }
        return asyncio.run(
            self.http_client.request(
                endpoint="/deductions",
                method="get",
                headers={"authorization": f"Bearer {self.bearer_token}"},
                parameters=dict(filter(itemgetter(1), payload.items())),
            )
        )
