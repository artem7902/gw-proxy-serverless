from unittest import TestCase
from websocket import create_connection

from osbot_utils.utils.Files import Files


class test_Firefox_Send(TestCase):

    def test_download(self):
        from osbot_utils.utils.Http import GET
        #print(GET('https://srv-file4.gofile.io/download/ePB3QX/aa-some-text.txt'))
        bytes = GET('https://srv-file7.gofile.io/download/UL8zkd/JS_Siemens-original.pdf',encoding=None)
        print(Files.save_bytes_as_file(bytes, '/tmp/temp-2.pdf'))

    def test_sending_files_to_firefox_send(self):
        print('-------')
        file_metadata = Files.file_contents('/tmp/_firefox_send__file_metadata')
        bytes_1       = Files.file_contents_as_bytes('/tmp/_firefox_send__bytes_1')
        bytes_2       = Files.file_contents_as_bytes('/tmp/_firefox_send__bytes_2')
        bytes_3       = Files.file_contents_as_bytes('/tmp/_firefox_send__bytes_3')
        print(file_metadata)
        print(len(bytes_1))
        print(len(bytes_2))
        print(len(bytes_3))

        ws = create_connection("wss://send.firefox.com/api/ws")
        print("sending file_metadata")
        ws.send(file_metadata)
        target_details = ws.recv()
        print(f'target_details: {target_details}')
        print("sending bytes_1")
        ws.send(bytes_1)
        print("sending bytes_2")
        ws.send(bytes_2)
        print("sending bytes_3")
        ws.send(bytes_3)
        result = ws.recv()
        print(f'result: {result}')






        #first_request = '{"fileMetadata":"Y6v9vtTmoLb9eHKedBGKFqbA13jPBvKyfBC68WH5otGETRtf54Dr8igEnBQKdctjr6wG5RwLkqe7jkRPc9DT133CSxerLbJJ-229ViFsB7zD-EHp0zgPNrGUwf5jE3g_Bm-tLBS8LUFNhwOoxG0YACbRjo_AbejeFP4hRwSI7BYfQ1U1V4Rw_YKEqdtLcJVVFzM","authorization":"send-v1 mhZ8f_vTn00lNJcT-k_25GqnpmEkXUY3FtJ0iRIaYzc7Ii-es1eoO_SJrpFFfKJH0CuRAw_nE9yFFJAXdfK0cA","timeLimit":86400,"dlimit":1}'

        # ws = create_connection("wss://send.firefox.com/api/ws")
        # print("sending first request")
        # ws.send(first_request)
        # result = ws.recv()
        # print("Received '%s'" % result)
        # #print("Sent")
        # #print("Receiving...")
        #
        # ws.close()
