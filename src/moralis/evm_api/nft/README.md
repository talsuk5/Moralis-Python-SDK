# evm_api: nft

- [re_sync_metadata](#re_sync_metadata)
- [get_contract_nfts](#get_contract_nfts)
- [get_nft_transfers](#get_nft_transfers)
- [get_nft_owners](#get_nft_owners)
- [get_nft_token_id_owners](#get_nft_token_id_owners)
- [get_wallet_nft_collections](#get_wallet_nft_collections)
- [get_nft_transfers_by_block](#get_nft_transfers_by_block)
- [get_nft_contract_metadata](#get_nft_contract_metadata)
- [get_nft_contract_transfers](#get_nft_contract_transfers)
- [sync_nft_contract](#sync_nft_contract)
- [get_nft_metadata](#get_nft_metadata)
- [get_nft_transfers_from_to_block](#get_nft_transfers_from_to_block)
- [get_wallet_nft_transfers](#get_wallet_nft_transfers)
- [get_nft_lowest_price](#get_nft_lowest_price)
- [get_nft_trades](#get_nft_trades)
- [search_nfts](#search_nfts)
- [get_wallet_nfts](#get_wallet_nfts)


---
## `re_sync_metadata()`
Resync the metadata for an NFT
* The metadata flag will request the NFT's metadata from an already existing token_uri
* The URI (default) flag will fetch the latest token_uri from the given NFT contract address. In sync mode the metadata will also be fetched
* The sync mode will make the endpoint synchronous so it will wait for the task to be completed before responding
* The async mode (default) will make the endpoint asynchronous so we will wait for the task to be completed before responding



### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "token_id": "", 
    "chain": "eth", 
    "flag": "URI", 
    "mode": "sync", 
}

result = evm_api.nft.re_sync_metadata(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "" |
| token_id | str | The ID of the token | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| flag | enum[str]: <br/>- "URI"<br/>- "metadata" | The type of resync to operate |  | "URI" | "URI" |
| mode | enum[str]: <br/>- "async"<br/>- "sync" | To define the behaviour of the endpoint |  | "async" | "sync" |



---
## `get_contract_nfts()`
Get NFTs for a given contract address, including metadata for all NFTs (where available).
* Results are limited to 100 per page by default
* Requests for contract addresses not yet indexed will automatically start the indexing process for that NFT collection.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "chain": "eth", 
    "format": "decimal", 
    "limit": 0, 
    "totalRanges": 0, 
    "range": 0, 
    "cursor": "", 
    "normalizeMetadata": True, 
}

result = evm_api.nft.get_contract_nfts(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| limit | int | The desired page size of the result. |  |  | 0 |
| totalRanges | int | The number of subranges to split the results into |  |  | 0 |
| range | int | The desired subrange to query |  |  | 0 |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| normalizeMetadata | bool | Should normalized metadata be returned? |  | False | True |



---
## `get_nft_transfers()`
Get transfers of an NFT given a contract address and token ID.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "token_id": "", 
    "chain": "eth", 
    "format": "decimal", 
    "limit": 0, 
    "cursor": "", 
}

result = evm_api.nft.get_nft_transfers(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "" |
| token_id | str | The ID of the token | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| limit | int | The desired page size of the result. |  |  | 0 |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |



---
## `get_nft_owners()`
Get owners of NFTs for a given contract.
* Requests for contract addresses not yet indexed will automatically start the indexing process for that NFT collection.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "chain": "eth", 
    "format": "decimal", 
    "limit": 0, 
    "cursor": "", 
    "normalizeMetadata": True, 
}

result = evm_api.nft.get_nft_owners(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| limit | int | The desired page size of the result. |  |  | 0 |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| normalizeMetadata | bool | Should normalized metadata be returned? |  | False | True |



---
## `get_nft_token_id_owners()`
Get owners of a specific NFT given the contract address and token ID. 
* Requests for contract addresses not yet indexed will automatically start the indexing process for that NFT collection



### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "token_id": "", 
    "chain": "eth", 
    "format": "decimal", 
    "limit": 0, 
    "cursor": "", 
    "normalizeMetadata": True, 
}

result = evm_api.nft.get_nft_token_id_owners(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "" |
| token_id | str | The ID of the token | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| limit | int | The desired page size of the result. |  |  | 0 |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| normalizeMetadata | bool | Should normalized metadata be returned? |  | False | True |



---
## `get_wallet_nft_collections()`
Get NFT collections owned by a given wallet address.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "chain": "eth", 
    "limit": 0, 
    "cursor": "", 
}

result = evm_api.nft.get_wallet_nft_collections(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The wallet address of the owner of NFTs in the collections | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| limit | int | The desired page size of the result. |  |  | 0 |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |



---
## `get_nft_transfers_by_block()`
Get transfers of NFTs given a block number or block hash.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "block_number_or_hash": "", 
    "chain": "eth", 
    "subdomain": "", 
    "limit": 0, 
    "cursor": "", 
}

result = evm_api.nft.get_nft_transfers_by_block(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| block_number_or_hash | str | The block number or block hash | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| subdomain | str | The subdomain of the Moralis server to use (only use when selecting local devchain as chain) |  |  | "" |
| limit | int | The desired page size of the result. |  | 100 | 0 |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |



---
## `get_nft_contract_metadata()`
Get the collection / contract level metadata for a given contract (name, symbol, base token URI).
* Requests for contract addresses not yet indexed will automatically start the indexing process for that NFT collection



### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "chain": "eth", 
}

result = evm_api.nft.get_nft_contract_metadata(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |



---
## `get_nft_contract_transfers()`
Get transfers of NFTs for a given contract and other parameters.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "chain": "eth", 
    "format": "decimal", 
    "limit": 0, 
    "cursor": "", 
}

result = evm_api.nft.get_nft_contract_transfers(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| limit | int | The desired page size of the result. |  |  | 0 |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |



---
## `sync_nft_contract()`
Initiates a sync of a previously non synced contract.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "chain": "eth", 
}

result = evm_api.nft.sync_nft_contract(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |



---
## `get_nft_metadata()`
Get NFT data, including metadata (where available), for the given NFT token ID and contract address.
* Requests for contract addresses not yet indexed will automatically start the indexing process for that NFT collection



### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "token_id": "", 
    "chain": "eth", 
    "format": "decimal", 
    "normalizeMetadata": True, 
}

result = evm_api.nft.get_nft_metadata(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "" |
| token_id | str | The ID of the token | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| normalizeMetadata | bool | Should normalized metadata be returned? |  | False | True |



---
## `get_nft_transfers_from_to_block()`
Get transfers of NFTs from a block number to a block number.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "chain": "eth", 
    "from_block": 0, 
    "to_block": 0, 
    "from_date": "", 
    "to_date": "", 
    "format": "decimal", 
    "limit": 0, 
    "cursor": "", 
}

result = evm_api.nft.get_nft_transfers_from_to_block(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| from_block | int | The minimum block number from which to get the transfers<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | int | The maximum block number from which to get the transfers.<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | 0 |
| from_date | str | The start date from which to get the transfers (any format that is accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | "" |
| to_date | str | The end date from which to get the transfers (any format that is accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| limit | int | The desired page size of the result. |  |  | 0 |
| cursor | str | The cursor returned in the previous response (for getting the next page)<br/> |  |  | "" |



---
## `get_wallet_nft_transfers()`
Get transfers of NFTs given the wallet and other parameters.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "chain": "eth", 
    "format": "decimal", 
    "direction": "both", 
    "from_block": 0, 
    "to_block": "", 
    "limit": 0, 
    "cursor": "", 
}

result = evm_api.nft.get_wallet_nft_transfers(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The wallet address of the sender or recipient of the transfers | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| direction | enum[str]: <br/>- "both"<br/>- "to"<br/>- "from" | The transfer direction |  | "both" | "both" |
| from_block | int | The minimum block number from which to get the transfers<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | str | To get the reserves at this block number |  |  | "" |
| limit | int | The desired page size of the result. |  |  | 0 |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |



---
## `get_nft_lowest_price()`
Get the lowest executed price for an NFT contract for the last x days (only trades paid in ETH).


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xa2107fa5b38d9bbd2c461d6edf11b11a50f6b974", 
    "chain": "eth", 
    "days": 0, 
    "provider_url": "", 
    "marketplace": "opensea", 
}

result = evm_api.nft.get_nft_lowest_price(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "0xa2107fa5b38d9bbd2c461d6edf11b11a50f6b974" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| days | int | The number of days to look back to find the lowest price<br/>If not provided 7 days will be the default<br/> |  |  | 0 |
| provider_url | str | The web3 provider URL to use when using local dev chain |  |  | "" |
| marketplace | enum[str]: <br/>- "opensea" | Marketplace from which to get the trades (only OpenSea is supported at the moment) |  | "opensea" | "opensea" |



---
## `get_nft_trades()`
Get trades of NFTs for a given contract and marketplace.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xa2107fa5b38d9bbd2c461d6edf11b11a50f6b974", 
    "chain": "eth", 
    "from_block": 0, 
    "to_block": "", 
    "from_date": "", 
    "to_date": "", 
    "provider_url": "", 
    "marketplace": "opensea", 
    "cursor": "", 
    "limit": 0, 
}

result = evm_api.nft.get_nft_trades(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "0xa2107fa5b38d9bbd2c461d6edf11b11a50f6b974" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| from_block | int | The minimum block number from which to get the transfers<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | str | The block number to get the trades from |  |  | "" |
| from_date | str | The start date from which to get the transfers (any format that is accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | "" |
| to_date | str | The end date from which to get the transfers (any format that is accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| provider_url | str | The web3 provider URL to use when using local dev chain |  |  | "" |
| marketplace | enum[str]: <br/>- "opensea" | Marketplace from which to get the trades (only OpenSea is supported at the moment) |  | "opensea" | "opensea" |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| limit | int | The desired page size of the result. |  |  | 0 |



---
## `search_nfts()`
Get NFTs that match a given metadata search query.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "q": "", 
    "chain": "eth", 
    "format": "decimal", 
    "filter": "name", 
    "from_block": 0, 
    "to_block": 0, 
    "from_date": "", 
    "to_date": "", 
    "addresses": [], 
    "cursor": "", 
    "limit": 0, 
}

result = evm_api.nft.search_nfts(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| q | str | The search string | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| filter | enum[str]: <br/>- "name"<br/>- "description"<br/>- "attributes"<br/>- "global"<br/>- "name,description"<br/>- "name,attributes"<br/>- "description,attributes"<br/>- "name,description,attributes" | What fields the search should match on. To look into the entire metadata set the value to 'global'. To have a better response time you can look into a specific field like name |  | "global" | "name" |
| from_block | int | The minimum block number from which to start the search<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | int | The maximum block number from which to end the search<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | 0 |
| from_date | str | The date from which to start the search (any format that is accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | "" |
| to_date | str | Get search results up until this date (any format that is accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| addresses | List of str | The addresses to get metadata for |  |  | [] |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| limit | int | The desired page size of the result. |  |  | 0 |



---
## `get_wallet_nfts()`
Get NFTs owned by a given address.
* The response will include status [SYNCED/SYNCING] based on the contracts being indexed.
* Use the token_address param to get results for a specific contract only
* Note that results will include all indexed NFTs
* Any request that includes the token_address param will start the indexing process for that NFT collection the very first time it is requested.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "chain": "eth", 
    "format": "decimal", 
    "limit": 0, 
    "token_addresses": [], 
    "cursor": "", 
    "normalizeMetadata": True, 
}

result = evm_api.nft.get_wallet_nfts(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the wallet | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| limit | int | The desired page size of the result. |  |  | 0 |
| token_addresses | List of str | The addresses to get balances for (optional) |  |  | [] |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| normalizeMetadata | bool | Should normalized metadata be returned? |  | False | True |




