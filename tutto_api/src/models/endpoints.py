"""Class to represent the endpoints of Tutto API."""

import asyncio

from typing import List, Union, Any
from datetime import date
from dataclasses import dataclass, field
from operator import itemgetter
from abc import ABC, abstractmethod

from tutto_api.src.helpers.http import HTTPRequest
from tutto_api.src.models.entities import Relative, Occurrence


@dataclass(init=False, frozen=True, slots=True)
class Endpoint(ABC):
    http_client: HTTPRequest = field()
    bearer_token: str = field()

    @abstractmethod
    def call(self) -> Any:
        pass


class EndpointFactory:
    @staticmethod
    def create_endpoint(
        base_url: str, endpoint: str, bearer_token: str, **kwargs
    ) -> Endpoint:
        """Factory method to create an endpoint object"""
        endpoints: dict[str, Endpoint] = {
            "deductions": Deductions,
            "purchases": Purchases,
            "service_types": ServiceTypes,
            "dirf_infos": DirfInfos,
            "dirf_additional_infos": DirfAdditionalInfos,
            "auth": Auth,
            "employees": Employees,
            "employees_occupations": EmployeesOccupations,
            "occupations": Occupations,
            "service_tickets": ServiceTickets,
        }
        endpoint_class: Union[Endpoint, None] = endpoints.get(endpoint)

        if endpoint_class:
            http_client = HTTPRequest(base_url=base_url)
            return endpoint_class(
                http_client=http_client, bearer_token=bearer_token, **kwargs
            )


### Endpoints ###
# GETs
@dataclass(init=True, frozen=True, slots=True)
class Deductions(Endpoint):
    """Class to handle the 'deductions' endpoint.\n
    Args:
        reference (str, required): Reference period in AAAAMM date format.
        type (str, optional): Deductions type.
        start_date (str, optional): Deductions start date in AAAAMMDD date format.
        end_date (str, optional): Deductions end date in AAAAMMDD date format.
        id (int, optional): Deductions ID.
    """

    http_client: HTTPRequest
    bearer_token: str

    reference: str
    type: str = field(default="")
    start_date: str = field(default="")
    end_date: str = field(default="")
    id: int = field(default=0)

    def call(self) -> Any:
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
                headers={"Authorization": f"Bearer {self.bearer_token}"},
                parameters=dict(filter(itemgetter(1), payload.items())),
            )
        )


@dataclass(init=True, frozen=True, slots=True)
class Purchases(Endpoint):
    """Class to handle the 'purchases' endpoint.\n
    Args:
        reference (str, required): Reference period in AAAAMM date format.
        type (str, optional): Purchases type.
        start_date (str, optional): Purchase start date in AAAAMMDD date format.
        end_date (str, optional): Purchase end date in AAAAMMDD date format.
        id (int, optional): Purchase ID.
    """

    http_client: HTTPRequest
    bearer_token: str

    reference: str
    type: str = field(default="")
    start_date: str = field(default="")
    end_date: str = field(default="")
    id: int = field(default=0)

    def call(self) -> Any:
        payload = {
            "reference": self.reference,
            "type": self.type,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "id": self.id,
        }
        return asyncio.run(
            self.http_client.request(
                endpoint="/purchases",
                method="get",
                headers={"Authorization": f"Bearer {self.bearer_token}"},
                parameters=dict(filter(itemgetter(1), payload.items())),
            )
        )


@dataclass(init=True, frozen=True, slots=True)
class ServiceTypes(Endpoint):
    """Class to handle the 'service_types' endpoint."""

    http_client: HTTPRequest
    bearer_token: str

    def call(self) -> Any:
        return asyncio.run(
            self.http_client.request(
                endpoint="/service_types",
                method="get",
                headers={"Authorization": f"Bearer {self.bearer_token}"},
            )
        )


@dataclass(init=True, frozen=True, slots=True)
class DirfInfos(Endpoint):
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

    http_client: HTTPRequest
    bearer_token: str

    reference: str
    layout: str = field(default="")
    company_id: int = field(default=0)
    type: str = field(default="")
    start_date: str = field(default="")
    end_date: str = field(default="")
    id: int = field(default=0)

    def call(self) -> Any:
        payload = {
            "reference": self.reference,
            "layout": self.layout,
            "company_id": self.company_id,
            "type": self.type,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "id": self.id,
        }
        return asyncio.run(
            self.http_client.request(
                endpoint="/dirf_infos",
                method="get",
                headers={"Authorization": f"Bearer {self.bearer_token}"},
                parameters=dict(filter(itemgetter(1), payload.items())),
            )
        )


@dataclass(init=True, frozen=True, slots=True)
class DirfAdditionalInfos(Endpoint):
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

    http_client: HTTPRequest
    bearer_token: str

    reference: str
    layout: str = field(default="")
    company_id: int = field(default=0)
    type: str = field(default="")
    start_date: str = field(default="")
    end_date: str = field(default="")
    id: int = field(default=0)

    def call(self) -> Any:
        payload = {
            "reference": self.reference,
            "layout": self.layout,
            "company_id": self.company_id,
            "type": self.type,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "id": self.id,
        }
        return asyncio.run(
            self.http_client.request(
                endpoint="/dirf_additional_infos",
                method="get",
                headers={"Authorization": f"Bearer {self.bearer_token}"},
                parameters=dict(filter(itemgetter(1), payload.items())),
            )
        )


# POSTs
@dataclass(init=True, frozen=True, slots=True)
class Auth(Endpoint):
    """Class to handle the 'auth' endpoint.\n
    Args:
        username (str, required): Username.
        password (str, required): Password.
        user_type (str, required): User type.
    """
    http_client: HTTPRequest
    bearer_token: str = field(default="", init=False)

    username: str
    password: str
    user_type: str

    def call(self) -> Any:
        payload = {
            "user": self.username,
            "password": self.password,
            "user_type": self.user_type,
        }
        return asyncio.run(
            self.http_client.request(
                endpoint="/auth",
                method="post",
                json=payload,
            )
        )


@dataclass(init=True, frozen=True, slots=True)
class Employees(Endpoint):
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

    http_client: HTTPRequest = field()
    bearer_token: str = field()

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

    def call(self) -> Any:
        payload = {
            "company_code": self.company_code,
            "company_vat": self.company_vat,
            "name": self.name,
            "badge": self.badge,
            "vat": self.vat,
            "id_card": self.id_card,
            "id_card_entity": self.id_card_entity,
            "id_card_emission": self.id_card_emission.isoformat(),
            "id_card_emission_state": self.id_card_emission_state,
            "sus_card": self.sus_card,
            "ctps_number": self.ctps_number,
            "pis_pasep": self.pis_pasep,
            "mother_name": self.mother_name,
            "address": self.address,
            "address_number": self.address_number,
            "complement": self.complement,
            "neighborhood": self.neighborhood,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode,
            "phone": self.phone,
            "email": self.email,
            "personal_email": self.personal_email,
            "gender": self.gender,
            "marital_status": self.marital_status,
            "salary": self.salary,
            "birthday_date": self.birthday_date.isoformat(),
            "admission_date": self.admission_date.isoformat(),
            "resignation_date": self.resignation_date.isoformat(),
            "experience_end_date": self.experience_end_date.isoformat(),
            "status_in_payroll": self.status_in_payroll,
            "organizational_unit_code": self.organizational_unit_code,
            "organizational_unit_name": self.organizational_unit_name,
            "position_code": self.position_code,
            "position_name": self.position_name,
            "occupation_code": self.occupation_code,
            "occupation_name": self.occupation_name,
            "workplace_code": self.workplace_code,
            "workplace_name": self.workplace_name,
            "syndicate_name": self.syndicate_name,
            "transfer_date": self.transfer_date.isoformat(),
            "bank_code": self.bank_code,
            "bank_agency": self.bank_agency,
            "bank_account": self.bank_account,
            "resignation_reason_code": self.resignation_reason_code,
            "resignation_reason_name": self.resignation_reason_name,
            "relatives": [
                {
                    "name": relative.name,
                    "relationship": relative.relationship,
                    "birth_date": relative.birth_date.isoformat(),
                    "cpf": relative.cpf,
                    "rg": relative.rg,
                    "rg_issuer": relative.rg_issuer,
                    "rg_issuer_state": relative.rg_issuer_state,
                    "rg_issuer_date": relative.rg_issuer_date.isoformat(),
                }
                for relative in self.relatives
                if self.relatives
            ],
            "occurrences": [
                {
                    "type": occurrence.type,
                    "start_date": occurrence.start_date.isoformat(),
                    "end_date": occurrence.end_date.isoformat(),
                    "absence_reason_code": occurrence.absence_reason_code,
                    "absence_reason_name": occurrence.absence_reason_name,
                }
                for occurrence in self.occurrences
                if self.occurrences
            ],
        }
        return asyncio.run(
            self.http_client.request(
                endpoint="/employees",
                method="post",
                headers={"Authorization": f"Bearer {self.bearer_token}"},
                json=payload,
            )
        )


@dataclass(init=True, frozen=True, slots=True)
class EmployeesOccupations(Endpoint):
    """Class to handle the 'employees_occupations' endpoint.\n
    Args:
        company_code (str, optional): Company code.
        company_vat (str, optional): Company CPNJ number.
        badge (str, required): Employee badge.
        vat (str, required): Employee VAT number.
        occupation_code (str, required): Employee occupation code.
    """

    http_client: HTTPRequest
    bearer_token: str

    badge: str
    vat: str
    occupation_code: str
    company_code: str = field(default="")
    company_vat: str = field(default="")

    def call(self) -> Any:
        payload = {
            "company_code": self.company_code,
            "company_vat": self.company_vat,
            "badge": self.badge,
            "vat": self.vat,
            "occupation_code": self.occupation_code,
        }
        return asyncio.run(
            self.http_client.request(
                endpoint="/employees_occupations",
                method="post",
                headers={"Authorization": f"Bearer {self.bearer_token}"},
                json=dict(filter(itemgetter(1), payload.items())),
            )
        )


@dataclass(init=True, frozen=True, slots=True)
class Occupations(Endpoint):
    """Class to handle the 'occupations' endpoint.\n
    Args:
        company_code (str, optional): Company code.
        company_vat (str, optional): Company VAT number.
        name (str, required): Occupation name.
        code (str, required): Occupation code.
        description (str, required): Occupation description.
        points (int, required): Occupation points.
    """

    http_client: HTTPRequest
    bearer_token: str

    code: str
    name: str
    description: str
    points: int
    company_code: str = field(default="")
    company_vat: str = field(default="")

    def call(self) -> Any:
        payload = {
            "company_code": self.company_code,
            "company_vat": self.company_vat,
            "code": self.code,
            "name": self.name,
            "description": self.description,
            "points": self.points,
        }
        return asyncio.run(
            self.http_client.request(
                endpoint="/occupations",
                method="post",
                headers={"Authorization": f"Bearer {self.bearer_token}"},
                json=dict(filter(itemgetter(1), payload.items())),
            )
        )


@dataclass(init=True, frozen=True, slots=True)
class ServiceTickets(Endpoint):
    """Class to handle the 'service_tickets' endpoint.\n
    Args:
        employee_badge (str, required): Employee badge code.
        employee_vat (str, required): Employee VAT number.
        employee_email (str, required): Employee e-mail.
        title (str, required): Service title.
        description (str, required): Service description.
        service_type_id (int, required): Service type ID.
    """

    http_client: HTTPRequest
    bearer_token: str

    employee_badge: str
    employee_vat: str
    employee_email: str
    title: str
    description: str
    service_type_id: int

    def call(self) -> Any:
        payload = {
            "employee_badge": self.employee_badge,
            "employee_vat": self.employee_vat,
            "employee_email": self.employee_email,
            "title": self.title,
            "description": self.description,
            "service_type_id": self.service_type_id,
        }
        return asyncio.run(
            self.http_client.request(
                endpoint="/service_tickets",
                method="post",
                headers={"Authorization": f"Bearer {self.bearer_token}"},
                json=dict(filter(itemgetter(1), payload.items())),
            )
        )
