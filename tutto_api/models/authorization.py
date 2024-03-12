"""This module handles authorization into Tutto API."""

import asyncio

from typing import Union, Literal, List, Optional
from dataclasses import dataclass

from tutto_api.helpers.http import HTTPRequest
from tutto_api.utils.filter_clean_utils import split_str_to_list


@dataclass(slots=True, init=True)
class _Auth:
    status: int
    message: str
    type: str
    token: str
    companies: List[int]
    companies_codes: List[int]
    companies_names: List[str]

    def __post_init__(self) -> None:
        self.companies = split_str_to_list(values=self.companies, dtype="int")
        self.companies_codes = split_str_to_list(
            values=self.companies_codes, dtype="int"
        )
        self.companies_names = split_str_to_list(
            values=self.companies_names, dtype="str"
        )

    def as_dict(self) -> dict:
        return {
            "status": self.status,
            "message": self.message,
            "type": self.type,
            "token": self.token,
            "companies": self.companies,
            "companies_codes": self.companies_codes,
            "companies_names": self.companies_names,
        }

    def as_bearer_token(self) -> dict:
        return {"Authorization": f"Bearer {self.token}"}


class Authorization:
    def __init__(
        self,
        base_url: str,
        user: str,
        password: str,
        basic_auth_token: str,
        user_type: Union[Literal["external"], str],
    ) -> None:
        self.http_client = HTTPRequest(base_url=base_url)
        self.__user = user
        self.__password = password
        self.__basic_auth_token = basic_auth_token
        self.__user_type = user_type
        pass

    def __get_auth(self) -> Optional[dict]:
        request = asyncio.run(
            self.http_client.request(
                endpoint="auth",
                method="post",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Basic {self.__basic_auth_token}",
                },
                json={
                    "user": self.__user,
                    "password": self.__password,
                    "user_type": self.__user_type,
                },
            )
        )
        if request["status"] == 200:
            return request

    @property
    def auth(self) -> Optional[_Auth]:
        request = self.__get_auth()
        if request:
            return _Auth(**request)
