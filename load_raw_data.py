import cleanjson
import json
import database_credentials
import pandas as pd

# pd.set_option('expand_frame_repr', False)
#
# spotify_json = json.load(open("spotify_api_output.json"))
# spotify_json2 = json.load(open("spotify_api_output2.json"))
#
# spotify_df = cleanjson.convert_spotify_json_to_df(spotify_json)
# spotify_df2 = cleanjson.convert_spotify_json_to_df(spotify_json2)
#
# spotify_df.to_sql(name="RAW_PLAYS", con=database_credentials.cnxn, index=False, if_exists="append")
# spotify_df2.to_sql(name="RAW_PLAYS", con=database_credentials.cnxn, index=False, if_exists="append")


def load_raw_data(connection, dataframe):
    dataframe.to_sql(name="RAW_PLAYS", con=connection, index=False, if_exists="append")
