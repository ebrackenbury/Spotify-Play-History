--Create Table
CREATE TABLE [SPOTIFY].[dbo].[RAW_PLAYS]
(
TRACK_NAME varchar(100),
TRACK_ID varchar(50),
TRACK_DURATION_MS int,
TRACK_TYPE varchar(50),
ALBUM_ARTIST varchar(100),
ARTIST_ID varchar(50),
ALBUM_ID varchar(50),
ALBUM_TRACK_NUMBER int,
ALBUM_NAME varchar(100),
ALBUM_RELEASE_DATE date,
ALBUM_TOTAL_TRACKS int,
ALBUM_TYPE varchar(50),
PLAYED_AT datetime
)
;