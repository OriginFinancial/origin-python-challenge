from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, ANY

import requests

from src.controllers.pokemon import list_pokemon


class TestPokemonController(IsolatedAsyncioTestCase):
    async def test_1(self):
        with patch.object(requests, 'get') as mocked_request:
            await list_pokemon(page=1)
            mocked_request.assert_called_once_with('https://pokeapi.co/api/v2/pokemon?offset=0&limit=20', auth=ANY)

    async def test_2(self):
        with patch.object(requests, 'get') as mocked_request:
            await list_pokemon(page=2)
            mocked_request.assert_called_once_with('https://pokeapi.co/api/v2/pokemon?offset=20&limit=20', auth=ANY)
