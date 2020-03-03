import os

import gw_proxy
from gw_proxy.api.Lambda_Layer import Lambda_Layer
from unittest import TestCase
from datetime import datetime


class test_Lambda_Layer(TestCase):

    def setUp(self):
        super().setUp()

    def test_create_grasswall_editor_lambda_layer(self):
        source_path = os.path.dirname(gw_proxy.__file__)[0:-8] + "modules/sdk-eval-toolset/libraries/linux"
        folders_mapping = { source_path: 'lib/sdk-eval-toolset'}
        self.api    = Lambda_Layer(name="glasswall_editor_engine", folders_mapping = folders_mapping, s3_bucket=f'gw-bot-test-layer-bucket-{datetime.now().timestamp()}')
        self.assertEqual(type(self.api.create()), str)
        self.assertEqual(self.api.delete(with_s3_bucket=True), True)

    def test_create_httrack_lambda_layer(self):
        source_path = os.path.dirname(gw_proxy.__file__)[0:-8] + "httrack"
        folders_mapping = { source_path: ''}
        self.api    = Lambda_Layer(name="httrack", folders_mapping = folders_mapping, s3_bucket=f'gw-bot-test-layer-bucket-{datetime.now().timestamp()}')
        self.assertEqual(type(self.api.create()), str)
        #self.assertEqual(self.api.delete(with_s3_bucket=True), True)
