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


class HistoricalNftTransfer(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "contract_type",
            "token_ids",
            "address",
            "amounts",
            "block_timestamp",
            "block_hash",
            "block_number",
            "to_address",
            "from_address",
            "transaction_hash",
        }
        
        class properties:
            transaction_hash = schemas.StrSchema
            address = schemas.StrSchema
            block_timestamp = schemas.StrSchema
            block_number = schemas.StrSchema
            block_hash = schemas.StrSchema
            to_address = schemas.StrSchema
            from_address = schemas.StrSchema
            
            
            class token_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'token_ids':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class amounts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'amounts':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            contract_type = schemas.StrSchema
            __annotations__ = {
                "transaction_hash": transaction_hash,
                "address": address,
                "block_timestamp": block_timestamp,
                "block_number": block_number,
                "block_hash": block_hash,
                "to_address": to_address,
                "from_address": from_address,
                "token_ids": token_ids,
                "amounts": amounts,
                "contract_type": contract_type,
            }

    
    contract_type: MetaOapg.properties.contract_type
    token_ids: MetaOapg.properties.token_ids
    address: MetaOapg.properties.address
    amounts: MetaOapg.properties.amounts
    block_timestamp: MetaOapg.properties.block_timestamp
    block_hash: MetaOapg.properties.block_hash
    block_number: MetaOapg.properties.block_number
    to_address: MetaOapg.properties.to_address
    from_address: MetaOapg.properties.from_address
    transaction_hash: MetaOapg.properties.transaction_hash
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_hash"]) -> MetaOapg.properties.transaction_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address"]) -> MetaOapg.properties.to_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_ids"]) -> MetaOapg.properties.token_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amounts"]) -> MetaOapg.properties.amounts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract_type"]) -> MetaOapg.properties.contract_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["transaction_hash", "address", "block_timestamp", "block_number", "block_hash", "to_address", "from_address", "token_ids", "amounts", "contract_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_hash"]) -> MetaOapg.properties.transaction_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address"]) -> MetaOapg.properties.to_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_ids"]) -> MetaOapg.properties.token_ids: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amounts"]) -> MetaOapg.properties.amounts: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract_type"]) -> MetaOapg.properties.contract_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["transaction_hash", "address", "block_timestamp", "block_number", "block_hash", "to_address", "from_address", "token_ids", "amounts", "contract_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        contract_type: typing.Union[MetaOapg.properties.contract_type, str, ],
        token_ids: typing.Union[MetaOapg.properties.token_ids, list, tuple, ],
        address: typing.Union[MetaOapg.properties.address, str, ],
        amounts: typing.Union[MetaOapg.properties.amounts, list, tuple, ],
        block_timestamp: typing.Union[MetaOapg.properties.block_timestamp, str, ],
        block_hash: typing.Union[MetaOapg.properties.block_hash, str, ],
        block_number: typing.Union[MetaOapg.properties.block_number, str, ],
        to_address: typing.Union[MetaOapg.properties.to_address, str, ],
        from_address: typing.Union[MetaOapg.properties.from_address, str, ],
        transaction_hash: typing.Union[MetaOapg.properties.transaction_hash, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'HistoricalNftTransfer':
        return super().__new__(
            cls,
            *args,
            contract_type=contract_type,
            token_ids=token_ids,
            address=address,
            amounts=amounts,
            block_timestamp=block_timestamp,
            block_hash=block_hash,
            block_number=block_number,
            to_address=to_address,
            from_address=from_address,
            transaction_hash=transaction_hash,
            _configuration=_configuration,
            **kwargs,
        )
