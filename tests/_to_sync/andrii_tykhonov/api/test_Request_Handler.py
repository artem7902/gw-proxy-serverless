from unittest import TestCase

from gw_proxy._to_sync.andrii_tykhonov.api.Response_Handler import Response_Handler


class test_response_handler(TestCase):

    def test_strings(self):
        search = 'foo'
        replace = 'bar'
        handler = Response_Handler(search, replace)
        response = handler.process('foobarbaz')
        assert response == 'barbarbaz'

    def test_lists(self):
        search = ['foo']
        replace = ['bar']
        handler = Response_Handler(search, replace)
        response = handler.process('foobarbaz')
        assert response == 'barbarbaz'

    def test_lists_multiple_items(self):
        search = ['foo', 'baz']
        replace = ['bar', 'jaz']
        handler = Response_Handler(search, replace)
        response = handler.process('foobarbaz')
        assert response == 'barbarjaz'

    def test_unequal_lists(self):
        search = ['foo', 'baz']
        replace = ['bar']
        try:
            handler = Response_Handler(search, replace)
        except ValueError as error:
            msg = 'Lenghts of `search` and `replace` are not equal'
            assert error.args[0] == msg