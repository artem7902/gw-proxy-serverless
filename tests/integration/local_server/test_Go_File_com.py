from unittest import TestCase

import requests

from osbot_utils.utils.Http import GET, GET_Json


class test_Go_File_com(TestCase):

    def test_upload_file(self):
        server_name = GET_Json('https://apiv2.gofile.io/getServer').get('data').get('server')
        upload_url  = f'https://{server_name}.gofile.io/upload'
        #upload_url = 'https://localhost/.gofile.io/upload'
        multipart_form_data = (
                ('filesUploaded', ('bbbbb.txt'       , open('/tmp/uploaded_files/bbbbb.txt', 'rb'))),
                ('filesUploaded', ('aa-some-text.txt', open('/tmp/uploaded_files/aa-some-text.txt', 'rb'))),
                #('email',  (None, 'dinis.cruz@owasp.org'))
             )
        #print(multipart_form_data)
        response = requests.post(upload_url, files=multipart_form_data, verify=False)
        print(response.content)

