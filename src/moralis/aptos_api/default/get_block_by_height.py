import json
import typing
import typing_extensions
from .api_instance import get_api_instance
from openapi_aptos_api.paths.blocks_block_height.get import RequestQueryParams, RequestPathParams

RequestNetworkQueryParams = typing_extensions.TypedDict("RequestNetworkQueryParams", {
    "network": typing.Literal["mainnet","testnet",]}, total=False)

class QueryParams(RequestQueryParams, RequestNetworkQueryParams):
    pass

class Params(QueryParams,RequestPathParams,):
    pass

def get_block_by_height(api_key: str, params: Params):
    api_instance = get_api_instance(api_key, params)
    query_params: typing.Any = {k: v for k, v in params.items() if k in RequestQueryParams.__annotations__.keys()}
    path_params: typing.Any = {k: v for k, v in params.items() if k in RequestPathParams.__annotations__.keys()}
    api_response = api_instance.get_block_by_height(
        query_params=query_params,
        path_params=path_params,
        accept_content_types=(
            'application/json; charset=utf-8',
        ),
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)
