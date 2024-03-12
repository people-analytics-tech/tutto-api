"""This module provides a factory method to create an endpoint object."""

from typing import Any

from tutto_api.helpers.http import HTTPRequest
from tutto_api.models.authorization import Authorization
from tutto_api.models.endpoints import (
    _Deductions,
    _Purchases,
    _ServiceTypes,
    _DirfInfos,
    _DirfAdditionalInfos,
    _Employees,
    _EmployeesOccupations,
    _Occupations,
    _ServiceTickets,
    Endpoint,
)

__all__ = []


class _EndpointCatalog:
    """
    A catalog of endpoints for the Tutto API.

    This class provides a collection of endpoints that can be used to interact with the Tutto API.
    It also provides methods to get and set services required by the endpoints.
    """

    __services = {
        "http_client": None,
        "authorization": None,
    }
    __catalog = {
        "deductions": _Deductions,
        "purchases": _Purchases,
        "service_types": _ServiceTypes,
        "dirf_infos": _DirfInfos,
        "dirf_additional_infos": _DirfAdditionalInfos,
        "employees": _Employees,
        "employees_occupations": _EmployeesOccupations,
        "occupations": _Occupations,
        "service_tickets": _ServiceTickets,
    }
    __setters = ["http_client", "authorization"]

    @staticmethod
    def get_endpoint(name: str, **kwargs) -> Endpoint:
        """
        Get an endpoint instance by name.

        Args:
            name (str): The name of the endpoint.

        Returns:
            Endpoint: An instance of the requested endpoint.

        Return if endpoint not found:
            Endpoint(ABC): An instance of the endpoint abstract dataclass, so you can
            use it to create an endpoint that this library does not support yet.
        """
        if not all(_EndpointCatalog.__services):
            raise ValueError("Services not set. Please set all required services first")

        endpoint = _EndpointCatalog.__catalog.get(name)
        if endpoint:
            return endpoint(**kwargs)
        if not endpoint:
            return Endpoint(
                http_client=_EndpointCatalog.__services["http_client"],
                authorization=_EndpointCatalog.__services["authorization"],
            )

    @staticmethod
    def get_catalog() -> dict:
        """
        Get the catalog of endpoints.

        Returns:
            dict: The catalog of endpoints.
        """
        return _EndpointCatalog.__catalog

    @staticmethod
    def set_services(name: str, value: Any) -> None:
        """
        Set a service required by the endpoints.

        Args:
            name (str): The name of the service.
            value (Any): The value of the service.

        Returns:
            None

        Raises:
            NameError: If the provided name is not accepted in the `set_services` method.
        """
        if name in _EndpointCatalog.__setters:
            _EndpointCatalog.__services[name] = value
        else:
            raise NameError(f"Name '{name}' not accepted in set_services() method")


class _EndpointFactory:
    @staticmethod
    def create_endpoint(
        base_url: str, endpoint: str, authorization: Authorization, **kwargs
    ) -> Endpoint:
        """Factory method to create an endpoint object"""
        # Fill the services catalog with the required services
        http_client = HTTPRequest(base_url=base_url)
        _EndpointCatalog.set_services(name="http_client", value=http_client)
        _EndpointCatalog.set_services(name="authorization", value=authorization)
        return _EndpointCatalog.get_endpoint(name=endpoint, **kwargs)
