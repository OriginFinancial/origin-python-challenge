from dataclasses import dataclass
from typing import Dict, List

import requests
from fastapi import APIRouter

router = APIRouter(
    prefix="/pokemon",
)


@dataclass
class PokemonDTO:
    name: str
    url: str


@router.get("")
async def list_pokemon(page: int = 1):
    limit = 20
    offset = page - 1
    url = f'https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}'

    r = requests.get(url, auth=('origin-user',
                                'eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY2MjA0MjMzNCwiaWF0IjoxNjYyMDQyMzM0fQ.xi3uKpbHXXxE5iTOkDrkHJfpXQhGQGjLHXwC1SE-kFI'))

    r2 = r.json()
    return map_dict(r2)


def map_dict(response: Dict) -> List[PokemonDTO]:
    return [PokemonDTO(name=item['name'], url=item['url']) for item in response['results']]
