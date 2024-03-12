"""This module handles authorization into Tutto API."""

import asyncio

from typing import Union, Literal, List, Optional
from dataclasses import dataclass

from tutto_api_client.helpers.http import HTTPRequest
from tutto_api_client.utils.filter_clean_utils import split_str_to_list


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
        self.companies = split_str_to_list(self.companies, dtype="int")
        self.companies_codes = split_str_to_list(self.companies_codes, dtype="int")
        self.companies_names = split_str_to_list(self.companies_names, dtype="str")

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
        user: str = "",
        user_type: Union[Literal["external"], str] = "external",
        password: str = "",
        basic_auth_token: str = "",
        bearer_token: str = "",
    ) -> None:
        # Initialize the class
        self.__http_client = HTTPRequest(base_url=base_url)
        self.__user = user
        self.__user_type = user_type
        self.__password = password
        self.__basic_auth_token = basic_auth_token
        self.__bearer_token = bearer_token
        # Check initialization
        self.__check_init()
        pass

    def __check_init(self) -> None:
        # Errors
        if not self.__basic_auth_token and not self.__bearer_token:
            raise ValueError("Basic auth token or bearer token are required.")
        if not self.__bearer_token and not (self.__user and self.__password):
            raise ValueError("User and password are required to get a bearer token.")
        # Warnings
        if self.__bearer_token and self.__basic_auth_token:
            print(
                "Auth Warning: Both basic auth and bearer token were provided. "
                "Using bearer token."
            )

    def __get_auth(self) -> Optional[dict]:
        request = asyncio.run(
            self.__http_client.request(
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
        if self.__bearer_token:
            return _Auth(
                status=0,
                message="Bearer token was user provided",
                type="bearer",
                token=self.__bearer_token,
                companies=[],
                companies_codes=[],
                companies_names=[],
            )
        request = self.__get_auth()
        if request:
            return _Auth(**request)
