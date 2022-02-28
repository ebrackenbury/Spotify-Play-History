# TODO: INSERT INTO SQL RAW_PLAYS TABLE, ADD ARTISTS, CONVERT TIME TO EASTERN?
import pandas as pd
import json

pd.set_option('expand_frame_repr', False)

# spotify_json = json.load(open("spotify_api_output2.json")) # temp


def convert_spotify_json_to_df(json_file):
    track_name = []
    track_spotify_id = []
    track_duration_ms = []
    track_type = []
    album_artist = []
    album_artist_spotify_id = []
    album_name = []
    album_spotify_id = []
    album_track_number = []
    album_total_tracks = []
    album_release_date = []
    album_type = []
    played_at = []

    for track in json_file["items"]:
        track_name.append(track["track"]["name"])
        track_spotify_id.append(track["track"]["id"])
        track_duration_ms.append(track["track"]["duration_ms"])
        track_type.append(track["track"]["type"])
        album_artist.append(track["track"]["album"]["artists"][0]["name"])
        album_artist_spotify_id.append(track["track"]["album"]["artists"][0]["id"])
        album_track_number.append(track["track"]["track_number"])
        album_name.append(track["track"]["album"]["name"])
        album_spotify_id.append(track["track"]["album"]["id"])
        album_release_date.append(track["track"]["album"]["release_date"])
        album_total_tracks.append(track["track"]["album"]["total_tracks"])
        album_type.append(track["track"]["album"]["type"])
        played_at.append(track["played_at"])

    data_dict = {"TRACK_NAME": track_name,
                 "TRACK_ID": track_spotify_id,
                 "TRACK_DURATION_MS": track_duration_ms,
                 "TRACK_TYPE": track_type,
                 "ALBUM_ARTIST": album_artist,
                 "ARTIST_ID": album_artist_spotify_id,
                 "ALBUM_TRACK_NUMBER": album_track_number,
                 "ALBUM_NAME": album_name,
                 "ALBUM_ID": album_spotify_id,
                 "ALBUM_RELEASE_DATE": album_release_date,
                 "ALBUM_TOTAL_TRACKS": album_total_tracks,
                 "ALBUM_TYPE": album_type,
                 "PLAYED_AT": played_at,
                 }

    data_df = pd.DataFrame(data_dict)

    return data_df

