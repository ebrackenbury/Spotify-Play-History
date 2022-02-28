import database_credentials

# with database_credentials.cnxn.connect() as con:
#     rs = con.execute('SELECT DISTINCT ALBUM_ARTIST FROM [SPOTIFY].[dbo].[RAW_PLAYS]')
#
#     for row in rs:
#         print(row)


def normalize_data(connection):

    with connection as con:
        print("Loading Artists")
        con.execute(
            """INSERT INTO [SPOTIFY].[dbo].[DIM_ARTIST]

            SELECT DISTINCT
                   RP.ARTIST_ID
              FROM [SPOTIFY].[dbo].[RAW_PLAYS] RP 
             WHERE NOT EXISTS
             (
             SELECT DA.SPOTIFY_ID
               FROM [SPOTIFY].[dbo].[DIM_ARTIST] DA
              WHERE DA.SPOTIFY_ID = RP.ARTIST_ID
             )"""
        )
        print("Loading Albums")
        con.execute(
            """INSERT INTO [SPOTIFY].[dbo].[DIM_ALBUM]
            ([ALBUM_SPOTIFY_ID], [ALBUM_NAME], [ARTIST_SPOTIFY_ID], [ARTIST_NAME], [RELEASE_DATE], [TOTAL_TRACKS])
            
            SELECT DISTINCT
                   RP.ALBUM_ID,
                   RP.ALBUM_NAME,
                   RP.ARTIST_ID,
                   RP.ALBUM_ARTIST,
                   RP.ALBUM_RELEASE_DATE,
                   RP.ALBUM_TOTAL_TRACKS
              FROM [SPOTIFY].[dbo].[RAW_PLAYS] RP 
             WHERE NOT EXISTS
            (
            SELECT DA.ALBUM_SPOTIFY_ID
              FROM [SPOTIFY].[dbo].[DIM_ALBUM] DA
             WHERE DA.ALBUM_SPOTIFY_ID = RP.ALBUM_ID
            )"""
         )

        print("Loading Tracks")
        con.execute(
            """INSERT INTO [SPOTIFY].[dbo].[DIM_TRACK]
            ([TRACK_SPOTIFY_ID], [TRACK_NAME], [ALBUM_SPOTIFY_ID], [ALBUM_NAME], [ALBUM_TRACK_NUMBER])
            
            SELECT DISTINCT
                   RP.TRACK_ID,
                   RP.TRACK_NAME,
                   RP.ALBUM_ID,
                   RP.ALBUM_NAME,
                   RP.ALBUM_TRACK_NUMBER
              FROM [SPOTIFY].[dbo].[RAW_PLAYS] RP 
             WHERE NOT EXISTS
             (
             SELECT DT.TRACK_SPOTIFY_ID
               FROM [SPOTIFY].[dbo].[DIM_TRACK] DT
              WHERE DT.TRACK_SPOTIFY_ID = RP.TRACK_ID
             )"""
        )

        # Put Below in own function?
        print("Updating SIDs")
        con.execute(
            """UPDATE DT
                  SET DT.ALBUM_SID = DA.ALBUM_SID
                 FROM SPOTIFY.dbo.DIM_TRACK DT
                 JOIN SPOTIFY.dbo.DIM_ALBUM DA ON DT.ALBUM_SPOTIFY_ID = DA.ALBUM_SPOTIFY_ID
            """
        )

        con.execute(
            """UPDATE DAL
                  SET DAL.ARTIST_SID = DAR.ARTIST_SID
                 FROM SPOTIFY.dbo.DIM_ALBUM  DAL
                 JOIN SPOTIFY.dbo.DIM_ARTIST DAR ON DAL.ARTIST_SPOTIFY_ID = DAR.ARTIST_SPOTIFY_ID
            """
        )

        con.execute(
            """UPDATE SPOTIFY.dbo.DIM_ALBUM
                  SET RELEASE_DATE_SID = CAST(CONVERT(varchar(10), CAST(RELEASE_DATE as date), 112) as int)
            """
        )
