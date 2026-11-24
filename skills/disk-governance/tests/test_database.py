import sqlite3
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from runtime.disk_governance.database import DataPaths, Store


class ReadOnlyDatabaseTests(unittest.TestCase):
    def test_reserved_path_characters_keep_connection_read_only(self):
        with TemporaryDirectory(prefix="disk-governance-test-") as root:
            for name in ("with#hash", "with%25escape", "with space"):
                with self.subTest(name=name):
                    paths = DataPaths(Path(root) / name)
                    with Store.open(paths, migrate=True) as store:
                        store.conn.execute("CREATE TABLE test_marker (value TEXT)")
                        store.conn.execute("INSERT INTO test_marker VALUES ('expected')")
                    original_bytes = paths.database.read_bytes()

                    with Store.open(paths, read_only=True) as store:
                        value = store.conn.execute("SELECT value FROM test_marker").fetchone()[0]
                        self.assertEqual(value, "expected")
                        with self.assertRaisesRegex(sqlite3.OperationalError, "readonly"):
                            store.conn.execute("DELETE FROM test_marker")

                    self.assertEqual(paths.database.read_bytes(), original_bytes)
