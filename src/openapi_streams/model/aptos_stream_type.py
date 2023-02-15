# coding: utf-8

"""
    Streams Api

    API that provides access to Moralis Streams  # noqa: E501

    The version of the OpenAPI document: 1.0.0
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

from openapi_streams import schemas  # noqa: F401


class AptosStreamType(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "includeChanges",
            "functions",
            "description",
            "includePayload",
            "demo",
            "statusMessage",
            "webhookUrl",
            "network",
            "allAddresses",
            "id",
            "tag",
            "amountOfAddresses",
            "events",
            "includeEvents",
            "isErrorSince",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            allAddresses = schemas.BoolSchema
            demo = schemas.BoolSchema
            description = schemas.StrSchema
            includeChanges = schemas.BoolSchema
            includeEvents = schemas.BoolSchema
            includePayload = schemas.BoolSchema
            
            
            class isErrorSince(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'isErrorSince':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def network() -> typing.Type['AptosNetwork']:
                return AptosNetwork
        
            @staticmethod
            def status() -> typing.Type['StreamsStatus']:
                return StreamsStatus
            statusMessage = schemas.StrSchema
            
            
            class events(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'events':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class functions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'functions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            tag = schemas.StrSchema
            webhookUrl = schemas.StrSchema
            amountOfAddresses = schemas.Float64Schema
            __annotations__ = {
                "id": id,
                "allAddresses": allAddresses,
                "demo": demo,
                "description": description,
                "includeChanges": includeChanges,
                "includeEvents": includeEvents,
                "includePayload": includePayload,
                "isErrorSince": isErrorSince,
                "network": network,
                "status": status,
                "statusMessage": statusMessage,
                "events": events,
                "functions": functions,
                "tag": tag,
                "webhookUrl": webhookUrl,
                "amountOfAddresses": amountOfAddresses,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    includeChanges: MetaOapg.properties.includeChanges
    functions: MetaOapg.properties.functions
    description: MetaOapg.properties.description
    includePayload: MetaOapg.properties.includePayload
    demo: MetaOapg.properties.demo
    statusMessage: MetaOapg.properties.statusMessage
    webhookUrl: MetaOapg.properties.webhookUrl
    network: 'AptosNetwork'
    allAddresses: MetaOapg.properties.allAddresses
    id: MetaOapg.properties.id
    tag: MetaOapg.properties.tag
    amountOfAddresses: MetaOapg.properties.amountOfAddresses
    events: MetaOapg.properties.events
    includeEvents: MetaOapg.properties.includeEvents
    isErrorSince: MetaOapg.properties.isErrorSince
    status: 'StreamsStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeChanges"]) -> MetaOapg.properties.includeChanges: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["functions"]) -> MetaOapg.properties.functions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includePayload"]) -> MetaOapg.properties.includePayload: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["demo"]) -> MetaOapg.properties.demo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusMessage"]) -> MetaOapg.properties.statusMessage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhookUrl"]) -> MetaOapg.properties.webhookUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network"]) -> 'AptosNetwork': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allAddresses"]) -> MetaOapg.properties.allAddresses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag"]) -> MetaOapg.properties.tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amountOfAddresses"]) -> MetaOapg.properties.amountOfAddresses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> MetaOapg.properties.events: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeEvents"]) -> MetaOapg.properties.includeEvents: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isErrorSince"]) -> MetaOapg.properties.isErrorSince: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'StreamsStatus': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["includeChanges"], typing_extensions.Literal["functions"], typing_extensions.Literal["description"], typing_extensions.Literal["includePayload"], typing_extensions.Literal["demo"], typing_extensions.Literal["statusMessage"], typing_extensions.Literal["webhookUrl"], typing_extensions.Literal["network"], typing_extensions.Literal["allAddresses"], typing_extensions.Literal["id"], typing_extensions.Literal["tag"], typing_extensions.Literal["amountOfAddresses"], typing_extensions.Literal["events"], typing_extensions.Literal["includeEvents"], typing_extensions.Literal["isErrorSince"], typing_extensions.Literal["status"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeChanges"]) -> MetaOapg.properties.includeChanges: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["functions"]) -> MetaOapg.properties.functions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includePayload"]) -> MetaOapg.properties.includePayload: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["demo"]) -> MetaOapg.properties.demo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusMessage"]) -> MetaOapg.properties.statusMessage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhookUrl"]) -> MetaOapg.properties.webhookUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network"]) -> 'AptosNetwork': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allAddresses"]) -> MetaOapg.properties.allAddresses: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag"]) -> MetaOapg.properties.tag: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amountOfAddresses"]) -> MetaOapg.properties.amountOfAddresses: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> MetaOapg.properties.events: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeEvents"]) -> MetaOapg.properties.includeEvents: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isErrorSince"]) -> MetaOapg.properties.isErrorSince: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'StreamsStatus': ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["includeChanges"], typing_extensions.Literal["functions"], typing_extensions.Literal["description"], typing_extensions.Literal["includePayload"], typing_extensions.Literal["demo"], typing_extensions.Literal["statusMessage"], typing_extensions.Literal["webhookUrl"], typing_extensions.Literal["network"], typing_extensions.Literal["allAddresses"], typing_extensions.Literal["id"], typing_extensions.Literal["tag"], typing_extensions.Literal["amountOfAddresses"], typing_extensions.Literal["events"], typing_extensions.Literal["includeEvents"], typing_extensions.Literal["isErrorSince"], typing_extensions.Literal["status"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        includeChanges: typing.Union[MetaOapg.properties.includeChanges, bool, ],
        functions: typing.Union[MetaOapg.properties.functions, list, tuple, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        includePayload: typing.Union[MetaOapg.properties.includePayload, bool, ],
        demo: typing.Union[MetaOapg.properties.demo, bool, ],
        statusMessage: typing.Union[MetaOapg.properties.statusMessage, str, ],
        webhookUrl: typing.Union[MetaOapg.properties.webhookUrl, str, ],
        network: 'AptosNetwork',
        allAddresses: typing.Union[MetaOapg.properties.allAddresses, bool, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        tag: typing.Union[MetaOapg.properties.tag, str, ],
        amountOfAddresses: typing.Union[MetaOapg.properties.amountOfAddresses, decimal.Decimal, int, float, ],
        events: typing.Union[MetaOapg.properties.events, list, tuple, ],
        includeEvents: typing.Union[MetaOapg.properties.includeEvents, bool, ],
        isErrorSince: typing.Union[MetaOapg.properties.isErrorSince, None, str, datetime, ],
        status: 'StreamsStatus',
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AptosStreamType':
        return super().__new__(
            cls,
            *args,
            includeChanges=includeChanges,
            functions=functions,
            description=description,
            includePayload=includePayload,
            demo=demo,
            statusMessage=statusMessage,
            webhookUrl=webhookUrl,
            network=network,
            allAddresses=allAddresses,
            id=id,
            tag=tag,
            amountOfAddresses=amountOfAddresses,
            events=events,
            includeEvents=includeEvents,
            isErrorSince=isErrorSince,
            status=status,
            _configuration=_configuration,
        )

from openapi_streams.model.aptos_network import AptosNetwork
from openapi_streams.model.streams_status import StreamsStatus
