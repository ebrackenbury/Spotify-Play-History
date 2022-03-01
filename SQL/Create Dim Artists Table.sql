-- Create table
CREATE TABLE [SPOTIFY].[dbo].[DIM_ARTIST]
(
ARTIST_SID int IDENTITY(0, 1),
ARTIST_NAME varchar(50) NOT NULL,
ARTIST_SPOTIFY_ID varchar(50) NOT NULL UNIQUE,
PRIMARY KEY (ARTIST_SID)
)
;

-- Insert Dummy Row
INSERT INTO [SPOTIFY].[dbo].[DIM_ARTIST] VALUES ('Unknown Artist', 'Unknown Spotify ID')
;