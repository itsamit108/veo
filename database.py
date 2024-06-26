from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine import connection
import pathlib
import config


BASE_DIR = pathlib.Path(__file__).resolve().parent

settings = config.get_settings()


CONNECT_BUNDLE = BASE_DIR / "unencrypted" / "astradb_connect.zip"
ASTRADB_CLIENT_ID = settings.astradb_client_id  # type: ignore
ASTRADB_CLIENT_SECRET = settings.astradb_client_secret  # type: ignore


def get_session():
    cloud_config = {"secure_connect_bundle": CONNECT_BUNDLE}
    auth_provider = PlainTextAuthProvider(ASTRADB_CLIENT_ID, ASTRADB_CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    connection.register_connection(str(session), session=session)
    connection.set_default_connection(str(session))
    return session
