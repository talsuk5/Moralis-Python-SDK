# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.2
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_evm_api import schemas  # noqa: F401


class ContractsReviewDto(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "contracts",
        }
        
        class properties:
            
            
            class contracts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 25
                    
                    @staticmethod
                    def items() -> typing.Type['ContractsReviewItem']:
                        return ContractsReviewItem
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ContractsReviewItem'], typing.List['ContractsReviewItem']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'contracts':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ContractsReviewItem':
                    return super().__getitem__(i)
            __annotations__ = {
                "contracts": contracts,
            }

    
    contracts: MetaOapg.properties.contracts
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contracts"]) -> MetaOapg.properties.contracts: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["contracts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contracts"]) -> MetaOapg.properties.contracts: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["contracts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        contracts: typing.Union[MetaOapg.properties.contracts, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContractsReviewDto':
        return super().__new__(
            cls,
            *args,
            contracts=contracts,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_evm_api.model.contracts_review_item import ContractsReviewItem
