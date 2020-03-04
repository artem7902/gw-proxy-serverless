import json

import requests

from osbot_utils.utils.Files import Files


class GW_Rebuild_Azure:

    def file_type_detection(self,target_file):
        endpoint = 'https://glasswall-file-drop-detection-api.azurewebsites.net/api/sas/FileTypeDetection'
        files = {'file': open(target_file, 'rb')}
        return json.loads(requests.post(endpoint, files=files).text)
        #return Files.file_contents_as_bytes(target_file)
    
    def file_analysis(self,target_file):
        endpoint = 'https://glasswall-file-drop-detection-api.azurewebsites.net/api/sas/FileAnalysis'
        files = {'file': open(target_file, 'rb')}
        return json.loads(requests.post(endpoint, files=files).text)
        #return Files.file_contents_as_bytes(target_file)
    
    def file_protect(self, target_file):
        endpoint = 'https://glasswall-file-drop-detection-api.azurewebsites.net/api/sas/FileProtect'
        files = {'file': open(target_file, 'rb')}
        return requests.post(endpoint, files=files).content
        # return Files.file_contents_as_bytes(target_file)
        
