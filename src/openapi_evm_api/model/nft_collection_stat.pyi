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


class NftCollectionStat(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "transfers",
            "total_tokens",
            "owners",
        }
        
        class properties:
            total_tokens = schemas.StrSchema
            
            
            class owners(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "current",
                    }
                    
                    class properties:
                        current = schemas.StrSchema
                        __annotations__ = {
                            "current": current,
                        }
                
                current: MetaOapg.properties.current
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["current"]) -> MetaOapg.properties.current: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["current", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["current"]) -> MetaOapg.properties.current: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["current", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    current: typing.Union[MetaOapg.properties.current, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'owners':
                    return super().__new__(
                        cls,
                        *args,
                        current=current,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class transfers(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "total",
                    }
                    
                    class properties:
                        total = schemas.StrSchema
                        __annotations__ = {
                            "total": total,
                        }
                
                total: MetaOapg.properties.total
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["total", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    total: typing.Union[MetaOapg.properties.total, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'transfers':
                    return super().__new__(
                        cls,
                        *args,
                        total=total,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "total_tokens": total_tokens,
                "owners": owners,
                "transfers": transfers,
            }

    
    transfers: MetaOapg.properties.transfers
    total_tokens: MetaOapg.properties.total_tokens
    owners: MetaOapg.properties.owners
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_tokens"]) -> MetaOapg.properties.total_tokens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owners"]) -> MetaOapg.properties.owners: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transfers"]) -> MetaOapg.properties.transfers: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["total_tokens", "owners", "transfers", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_tokens"]) -> MetaOapg.properties.total_tokens: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owners"]) -> MetaOapg.properties.owners: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transfers"]) -> MetaOapg.properties.transfers: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total_tokens", "owners", "transfers", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        transfers: typing.Union[MetaOapg.properties.transfers, dict, frozendict.frozendict, ],
        total_tokens: typing.Union[MetaOapg.properties.total_tokens, str, ],
        owners: typing.Union[MetaOapg.properties.owners, dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NftCollectionStat':
        return super().__new__(
            cls,
            *args,
            transfers=transfers,
            total_tokens=total_tokens,
            owners=owners,
            _configuration=_configuration,
            **kwargs,
        )
