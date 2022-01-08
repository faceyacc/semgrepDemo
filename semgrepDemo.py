import driverlessai
import pyspark as ps
from pyspark.sql.functions import col, pandas_udf
from pyspark.sql.types import LongType
import pandas as pd

def trivial_example_function(a, b):
    return a * b

trivial_ex = pandas_udf(trivial_example_function, returnType = LongType())


pathToCerts = "path/to/certs/file.pem"

def connect_to_dai():
    driverlessaiAddress = "https://hostname.wellsfargo.net:12345"
    un = "BobLaBlah"
    pw = "123456789"
    pathToCerts = "path/to/certs/file.pem"

    dai = driverlessai.Client(address = driverlessaiAddress, username = un, password = pw, verify = pathToCerts)
    return dai
