import spotify
import cleanjson
import load_raw_data
import database_credentials


# select_job = input()

def main():

    spotify_json_data = spotify.get_spotify_data(unix='', limit=50)

    clean_data = cleanjson.convert_spotify_json_to_df(json_file=spotify_json_data)

    load_raw_data.load_raw_data(connection=database_credentials.cnxn, dataframe=clean_data)


if __name__ == '__main__':
    main()
