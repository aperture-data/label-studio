import json
from contextlib import nullcontext
from unittest.mock import Mock

from django.test import SimpleTestCase, override_settings
from io_storages.aperturedb.models import ApertureDBImportStorage


class ApertureDBStorageFiltersTests(SimpleTestCase):
    def test_saved_and_expression_filters_work_with_untagged_images(self):
        expected = ['$batch', '==', '$$test']
        for user_filter in ({'batch': ['==', '$test']}, expected):
            for untagged in (True, False):
                with self.subTest(user_filter=user_filter, untagged=untagged):
                    with override_settings(APERTUREDB_UNTAGGED_IMAGES=untagged):
                        storage = ApertureDBImportStorage(limit=1, constraints=json.dumps(user_filter))
                        db = Mock()
                        db.query.return_value = (
                            [
                                {
                                    'FindImage': {
                                        'status': 0,
                                        'returned': 1,
                                        'entities': [{'_uniqueid': '1.2.3'}],
                                    }
                                }
                            ],
                            [],
                        )
                        storage.pool = lambda: Mock(get_connection=lambda: nullcontext(db))

                        self.assertEqual(list(storage.iterkeys()), ['1.2.3'])

                        cmd = db.query.call_args.args[0][0]['FindImage']
                        self.assertEqual(cmd['limit'], 1)
                        self.assertEqual(cmd['offset'], 0)
                        self.assertEqual(
                            cmd['constraints'],
                            expected
                            if untagged
                            else [
                                'all',
                                ['all', ['$width', '>', 0], ['$height', '>', 0]],
                                expected,
                            ],
                        )
