import sys
if sys.version_info < (3,6):
    raise Exception('Sorry, For MindsDB Python < 3.6 is not supported')

# @TODO: FIND A WAY TO ACTUALLY SOLVE THIS ASAP !!!
# HORRIBLE HACK TO AVOID SEGFAULT
import lightwood
# HORRIBLE HACK TO AVOID SEGFAULT
# @TODO: FIND A WAY TO ACTUALLY SOLVE THIS ASAP !!!
from mindsdb_native.libs.controllers import functional
F = functional

from mindsdb_native.config import CONFIG
import mindsdb_native.libs.constants.mindsdb as CONST

from mindsdb_native.__about__ import __package_name__ as name, __version__

from mindsdb_native.libs.controllers.predictor import Predictor

from mindsdb_native.libs.data_sources.maria_ds import MariaDS
from mindsdb_native.libs.data_sources.mysql_ds import MySqlDS
from mindsdb_native.libs.data_sources.clickhouse_ds import ClickhouseDS
from mindsdb_native.libs.data_sources.file_ds import FileDS

# These might not initialized properly since they require optional dependencies, so we wrap them in a try-except
try:
    from mindsdb_native.libs.data_sources.s3_ds import S3DS
except:
    print("S3 Datasource is not available by default. If you wish to use it, please install mindsdb_native[extra_data_sources]")
    S3DS = None

try:
    from mindsdb_native.libs.data_sources.postgres_ds import PostgresDS
except ImportError:
    print("Postgres Datasource is not available by default. If you wish to use it, please install mindsdb_native[extra_data_sources]")
    PostgresDS = None

try:
    from mindsdb_native.libs.data_sources.ms_sql_ds import MSSQLDS
except ImportError:
    print("Microsoft SQL Server Datasource is not available by default. If you wish to use it, please install mindsdb_native[extra_data_sources]")
    MSSQLDS = None

try:
    from mindsdb_native.libs.data_sources.mongodb_ds import MongoDS
except ImportError:
    print("Mongo Datasource is not available by default. If you wish to use it, please install mindsdb_native[extra_data_sources]")
    MongoDS = None

try:
    from mindsdb_native.libs.data_sources.snowflake_ds import SnowflakeDS
except ImportError:
    print("SnowflakeDS Datasource is not available by default. If you wish to use it, please install mindsdb_native[snowflake]")
    SnowflakeDS = None


MindsDB = Predictor
