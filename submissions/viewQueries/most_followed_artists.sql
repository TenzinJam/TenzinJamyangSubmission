-- SQLite

CREATE VIEW most_followed_artists
AS
SELECT artist_id, artist_name, followers
FROM artist
ORDER BY 3 DESC
