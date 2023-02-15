# coding: utf-8

"""
    aptos-api

    The aptos-api provider  # noqa: E501

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

from openapi_aptos_api import schemas  # noqa: F401


class StateCheckpointTransaction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "vm_status",
            "success",
            "event_root_hash",
            "gas_used",
            "changes",
            "state_checkpoint_hash",
            "state_change_hash",
            "accumulator_root_hash",
            "type",
            "version",
            "hash",
            "timestamp",
        }
        
        class properties:
            type = schemas.StrSchema
            version = schemas.StrSchema
            hash = schemas.StrSchema
            state_change_hash = schemas.StrSchema
            event_root_hash = schemas.StrSchema
            state_checkpoint_hash = schemas.StrSchema
            gas_used = schemas.StrSchema
            success = schemas.BoolSchema
            vm_status = schemas.StrSchema
            accumulator_root_hash = schemas.StrSchema
            
            
            class changes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'changes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            timestamp = schemas.StrSchema
            __annotations__ = {
                "type": type,
                "version": version,
                "hash": hash,
                "state_change_hash": state_change_hash,
                "event_root_hash": event_root_hash,
                "state_checkpoint_hash": state_checkpoint_hash,
                "gas_used": gas_used,
                "success": success,
                "vm_status": vm_status,
                "accumulator_root_hash": accumulator_root_hash,
                "changes": changes,
                "timestamp": timestamp,
            }
    
    vm_status: MetaOapg.properties.vm_status
    success: MetaOapg.properties.success
    event_root_hash: MetaOapg.properties.event_root_hash
    gas_used: MetaOapg.properties.gas_used
    changes: MetaOapg.properties.changes
    state_checkpoint_hash: MetaOapg.properties.state_checkpoint_hash
    state_change_hash: MetaOapg.properties.state_change_hash
    accumulator_root_hash: MetaOapg.properties.accumulator_root_hash
    type: MetaOapg.properties.type
    version: MetaOapg.properties.version
    hash: MetaOapg.properties.hash
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hash"]) -> MetaOapg.properties.hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state_change_hash"]) -> MetaOapg.properties.state_change_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_root_hash"]) -> MetaOapg.properties.event_root_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state_checkpoint_hash"]) -> MetaOapg.properties.state_checkpoint_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gas_used"]) -> MetaOapg.properties.gas_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["success"]) -> MetaOapg.properties.success: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vm_status"]) -> MetaOapg.properties.vm_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accumulator_root_hash"]) -> MetaOapg.properties.accumulator_root_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["changes"]) -> MetaOapg.properties.changes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "version", "hash", "state_change_hash", "event_root_hash", "state_checkpoint_hash", "gas_used", "success", "vm_status", "accumulator_root_hash", "changes", "timestamp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hash"]) -> MetaOapg.properties.hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state_change_hash"]) -> MetaOapg.properties.state_change_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_root_hash"]) -> MetaOapg.properties.event_root_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state_checkpoint_hash"]) -> MetaOapg.properties.state_checkpoint_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gas_used"]) -> MetaOapg.properties.gas_used: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["success"]) -> MetaOapg.properties.success: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vm_status"]) -> MetaOapg.properties.vm_status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accumulator_root_hash"]) -> MetaOapg.properties.accumulator_root_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["changes"]) -> MetaOapg.properties.changes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "version", "hash", "state_change_hash", "event_root_hash", "state_checkpoint_hash", "gas_used", "success", "vm_status", "accumulator_root_hash", "changes", "timestamp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        vm_status: typing.Union[MetaOapg.properties.vm_status, str, ],
        success: typing.Union[MetaOapg.properties.success, bool, ],
        event_root_hash: typing.Union[MetaOapg.properties.event_root_hash, str, ],
        gas_used: typing.Union[MetaOapg.properties.gas_used, str, ],
        changes: typing.Union[MetaOapg.properties.changes, list, tuple, ],
        state_checkpoint_hash: typing.Union[MetaOapg.properties.state_checkpoint_hash, str, ],
        state_change_hash: typing.Union[MetaOapg.properties.state_change_hash, str, ],
        accumulator_root_hash: typing.Union[MetaOapg.properties.accumulator_root_hash, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        version: typing.Union[MetaOapg.properties.version, str, ],
        hash: typing.Union[MetaOapg.properties.hash, str, ],
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StateCheckpointTransaction':
        return super().__new__(
            cls,
            *args,
            vm_status=vm_status,
            success=success,
            event_root_hash=event_root_hash,
            gas_used=gas_used,
            changes=changes,
            state_checkpoint_hash=state_checkpoint_hash,
            state_change_hash=state_change_hash,
            accumulator_root_hash=accumulator_root_hash,
            type=type,
            version=version,
            hash=hash,
            timestamp=timestamp,
            _configuration=_configuration,
            **kwargs,
        )
