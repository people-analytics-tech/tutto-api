"""Module to represent the endpoints of Tutto API."""

import asyncio
import aiohttp

from typing import List
from datetime import date
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

from tutto_api.helpers.http import HTTPRequest
from tutto_api.models.entities import Relative, Occurrence
from tutto_api.models.authorization import Authorization
from tutto_api.utils.filter_clean_utils import (
    filter_dict_with_falsy_values,
    convert_dict_dates_to_isoformat,
)

__all__ = ["Endpoint"]


### ABC for Endpoints ###
@dataclass(init=True, frozen=True, slots=True)
class Endpoint(ABC):
    """Tutto API endpoint abstract dataclass with batteries included."""

    http_client: HTTPRequest = field(
        init=True, repr=False, compare=False, hash=False, metadata=False
    )
    authorization: Authorization = field(
        init=True, repr=False, compare=False, hash=False, metadata=False
    )

    @abstractmethod
    def call(self, **kwargs) -> aiohttp.ClientResponse:
        """Method to call the endpoint."""
        return asyncio.run(
            self.http_client.request(
                **kwargs,
                headers={
                    **self.authorization.auth.as_bearer_token(),
                    **kwargs.get("headers", {}),
                },
            )
        )


### Endpoints ###
# GETs
@dataclass(init=True, frozen=True, slots=True)
class _Deductions(Endpoint):
    """Class to handle the 'deductions' endpoint.\n
    Args:
        reference (str, required): Reference period in AAAAMM date format.
        type (str, optional): Deductions type.
        start_date (str, optional): Deductions start date in AAAAMMDD date format.
        end_date (str, optional): Deductions end date in AAAAMMDD date format.
        id (int, optional): Deductions ID.
    """

    reference: str
    type: str = field(default="")
    start_date: str = field(default="")
    end_date: str = field(default="")
    id: int = field(default=0)

    def call(self):
        endpoint = "deductions"
        method = "get"
        parameters = filter_dict_with_falsy_values(self.__dict__)
        return super().call(endpoint=endpoint, method=method, parameters=parameters)


@dataclass(init=True, frozen=True, slots=True)
class _Purchases(Endpoint):
    """Class to handle the 'purchases' endpoint.\n
    Args:
        reference (str, required): Reference period in AAAAMM date format.
        type (str, optional): Purchases type.
        start_date (str, optional): Purchase start date in AAAAMMDD date format.
        end_date (str, optional): Purchase end date in AAAAMMDD date format.
        id (int, optional): Purchase ID.
    """

    reference: str
    type: str = field(default="")
    start_date: str = field(default="")
    end_date: str = field(default="")
    id: int = field(default=0)

    def call(self):
        endpoint = "purchases"
        method = "get"
        parameters = filter_dict_with_falsy_values(self.__dict__)
        return super().call(endpoint=endpoint, method=method, parameters=parameters)


@dataclass(init=True, frozen=True, slots=True)
class _ServiceTypes(Endpoint):
    """Class to handle the 'service_types' endpoint."""

    def call(self):
        endpoint = "service_types"
        method = "get"
        return super().call(endpoint=endpoint, method=method)


@dataclass(init=True, frozen=True, slots=True)
class _DirfInfos(Endpoint):
    """Class to handle the 'dirf_infos' endpoint.\n
    Args:
        reference (str, required): Reference period in AAAAMM date format.
        layout (str, optional): data layout.
        company_id (int, optional): Company ID.
        type (str, optional): DIRF type.
        start_date (str, optional): DIRF start date in AAAAMMDD date format.
        end_date (str, optional): DIRF end date in AAAAMMDD date format.
        id (int, optional): DIRF ID.
    """

    reference: str
    layout: str = field(default="")
    company_id: int = field(default=0)
    type: str = field(default="")
    start_date: str = field(default="")
    end_date: str = field(default="")
    id: int = field(default=0)

    def call(self):
        endpoint = "dirf_infos"
        method = "get"
        parameters = filter_dict_with_falsy_values(self.__dict__)
        return super().call(endpoint=endpoint, method=method, parameters=parameters)


@dataclass(init=True, frozen=True, slots=True)
class _DirfAdditionalInfos(Endpoint):
    """Class to handle the 'dirf_additional_infos' endpoint.\n
    Args:
        reference (str, required): Reference period in AAAAMM date format.
        layout (str, optional): data layout.
        company_id (int, optional): Company ID.
        type (str, optional): DIRF type.
        start_date (str, optional): DIRF start date in AAAAMMDD date format.
        end_date (str, optional): DIRF end date in AAAAMMDD date format.
        id (int, optional): DIRF ID.
    """

    reference: str
    layout: str = field(default="")
    company_id: int = field(default=0)
    type: str = field(default="")
    start_date: str = field(default="")
    end_date: str = field(default="")
    id: int = field(default=0)

    def call(self):
        endpoint = "dirf_additional_infos"
        method = "get"
        parameters = filter_dict_with_falsy_values(self.__dict__)
        return super().call(endpoint=endpoint, method=method, parameters=parameters)


# POSTs
@dataclass(init=True, frozen=True, slots=True)
class _Employees(Endpoint):
    """Class to handle the 'employees' endpoint.\n
    Args:
        company_code (str, required): Company code.
        company_vat (str, required): Company VAT number.
        name (str, required): Employee name.
        badge (str, required): Employee badge.
        vat (str, required): Employee VAT number.
        id_card (str, required): Employee ID card number.
        id_card_entity (str, required): Employee ID card entity.
        id_card_emission (date, required): Employee ID card emission date.
        id_card_emission_state (str, required): Employee ID card emission state.
        sus_card (str, required): Employee SUS card number.
        ctps_number (str, required): Employee CTPS number.
        pis_pasep (str, required): Employee PIS/PASEP number.
        mother_name (str, required): Employee mother name.
        address (str, required): Employee address.
        address_number (str, required): Employee address number.
        complement (str, required): Employee address complement.
        neighborhood (str, required): Employee neighborhood.
        city (str, required): Employee city.
        state (str, required): Employee state.
        zipcode (str, required): Employee ZIP code.
        phone (str, required): Employee phone number.
        email (str, required): Employee email.
        personal_email (str, required): Employee personal email.
        gender (str, required): Employee gender.
        marital_status (str, required): Employee marital status.
        salary (float, required): Employee salary.
        birthday_date (date, required): Employee birthday date.
        admission_date (date, required): Employee admission date.
        resignation_date (date, required): Employee resignation date.
        experience_end_date (date, required): Employee experience end date.
        status_in_payroll (str, required): Employee status in payroll.
        organizational_unit_code (str, required): Employee organizational unit code.
        organizational_unit_name (str, required): Employee organizational unit name.
        position_code (str, required): Employee position code.
        position_name (str, required): Employee position name.
        occupation_code (str, required): Employee occupation code.
        occupation_name (str, required): Employee occupation name.
        workplace_code (str, required): Employee workplace code.
        workplace_name (str, required): Employee workplace name.
        syndicate_name (str, required): Employee syndicate name.
        transfer_date (date, required): Employee transfer date.
        bank_code (str, required): Employee bank code.
        bank_agency (str, required): Employee bank agency.
        bank_account (str, required): Employee bank account.
        resignation_reason_code (str, required): Employee resignation reason code.
        resignation_reason_name (str, required): Employee resignation reason name.
        relatives (List[Relative], optional): Employee relatives.
        occurrences (List[Occurrence], optional): Employee occurrences.
    """

    company_code: str
    company_vat: str
    name: str
    badge: str
    vat: str
    id_card: str
    id_card_entity: str
    id_card_emission: date
    id_card_emission_state: str
    sus_card: str
    ctps_number: str
    pis_pasep: str
    mother_name: str
    address: str
    address_number: str
    complement: str
    neighborhood: str
    city: str
    state: str
    zipcode: str
    phone: str
    email: str
    personal_email: str
    gender: str
    marital_status: str
    salary: float
    birthday_date: date
    admission_date: date
    resignation_date: date
    experience_end_date: date
    status_in_payroll: str
    organizational_unit_code: str
    organizational_unit_name: str
    position_code: str
    position_name: str
    occupation_code: str
    occupation_name: str
    workplace_code: str
    workplace_name: str
    syndicate_name: str
    transfer_date: date
    bank_code: str
    bank_agency: str
    bank_account: str
    resignation_reason_code: str
    resignation_reason_name: str
    relatives: List[Relative] = field(default_factory=list)
    occurrences: List[Occurrence] = field(default_factory=list)

    def call(self):
        endpoint = "employees"
        method = "post"
        payload = convert_dict_dates_to_isoformat(self.__dict__)
        return super().call(endpoint=endpoint, method=method, json=payload)


@dataclass(init=True, frozen=True, slots=True)
class _EmployeesOccupations(Endpoint):
    """Class to handle the 'employees_occupations' endpoint.\n
    Args:
        company_code (str, optional): Company code.
        company_vat (str, optional): Company CPNJ number.
        badge (str, required): Employee badge.
        vat (str, required): Employee VAT number.
        occupation_code (str, required): Employee occupation code.
    """

    badge: str
    vat: str
    occupation_code: str
    company_code: str = field(default="")
    company_vat: str = field(default="")

    def call(self):
        endpoint = "employees_occupations"
        method = "post"
        payload = filter_dict_with_falsy_values(self.__dict__)
        return super().call(endpoint=endpoint, method=method, json=payload)


@dataclass(init=True, frozen=True, slots=True)
class _Occupations(Endpoint):
    """Class to handle the 'occupations' endpoint.\n
    Args:
        company_code (str, optional): Company code.
        company_vat (str, optional): Company VAT number.
        name (str, required): Occupation name.
        code (str, required): Occupation code.
        description (str, required): Occupation description.
        points (int, required): Occupation points.
    """

    code: str
    name: str
    description: str
    points: int
    company_code: str = field(default="")
    company_vat: str = field(default="")

    def call(self):
        endpoint = "occupations"
        method = "post"
        payload = filter_dict_with_falsy_values(self.__dict__)
        return super().call(endpoint=endpoint, method=method, json=payload)


@dataclass(init=True, frozen=True, slots=True)
class _ServiceTickets(Endpoint):
    """Class to handle the 'service_tickets' endpoint.\n
    Args:
        employee_badge (str, required): Employee badge code.
        employee_vat (str, required): Employee VAT number.
        employee_email (str, required): Employee e-mail.
        title (str, required): Service title.
        description (str, required): Service description.
        service_type_id (int, required): Service type ID.
    """

    employee_badge: str
    employee_vat: str
    employee_email: str
    title: str
    description: str
    service_type_id: int

    def call(self):
        endpoint = "service_tickets"
        method = "post"
        payload = filter_dict_with_falsy_values(self.__dict__)
        return super().call(endpoint=endpoint, method=method, json=payload)
