-- Create Table
CREATE TABLE [SPOTIFY].[dbo].[DIM_TRACK]
(
TRACK_SID int IDENTITY(0, 1),
TRACK_SPOTIFY_ID varchar(50),
TRACK_NAME varchar(100),
ALBUM_SID int,
ALBUM_SPOTIFY_ID varchar(50),
ALBUM_NAME varchar(100),
ALBUM_TRACK_NUMBER int
PRIMARY KEY (TRACK_SID)
FOREIGN KEY (ALBUM_SID) REFERENCES DIM_ALBUM(ALBUM_SID)
)
;

-- Insert Dummy Row
INSERT INTO [SPOTIFY].[dbo].[DIM_TRACK] VALUES ('', 'Unknown Track', 0, '', 'Unknown Album', 0)
;

