from unittest import TestCase

from gw_proxy.gw.GW_Rebuild_Azure import GW_Rebuild_Azure
from osbot_utils.utils.Files import Files


class test_GW_Rebuild_Azure(TestCase):

    def test_file_type_detection(self):
        gw_azure = GW_Rebuild_Azure()
        test_File = '/Users/diniscruz//Downloads/bug.png'
        print(gw_azure.file_type_detection(test_File).get('fileType'))

    def test_file_analysis(self):
        gw_azure = GW_Rebuild_Azure()
        test_File = '/Users/diniscruz//Downloads/bug.png'
        print(gw_azure.file_analysis(test_File))

    def test_file_protect(self):
        gw_azure = GW_Rebuild_Azure()
        target = '/Users/diniscruz//Downloads/bug.png'
        target = '/Users/diniscruz/Downloads/test/shake.jpeg'
        #target = '/Users/diniscruz/Downloads/aa-some-text.txt' # doesn't work
        bytes = gw_azure.file_protect(target)
        rebuilt = Files.save_bytes_as_file(bytes, extension= '.txt')
        print('-------')
        print(rebuilt)