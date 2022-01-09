*** Frontend ***

*** Backend ***

*** Crawler ***

Crawl single player stats

`python3 -m player.playerRawDataCrawler --pdgaNumber 44708`

Crawl latest PDGA Number on player

`python3 -m player.playerLatestIdCrawler`

Run larger batch of PDGA numbers

`python3 -m runners.runPlayerRawData --type test --startId 1 --endId 5`

Crawl tournament with specific ID

`python3 -m tournament.tournamentRawDataCrawler --tournamentId 52082`

Run all unit tests

`python3 -m unittest discover -v`

*** TODO ***

- Crawl tournaments
- Tests for crawling

- Decide DB for project

- Schema for DB
- Upload utils to DB

- Parse & upload players
- Tests for parsing players

- Parse & upload tournaments
- Tests for parsing tournaments

- Mock data for frontend

- Start Backend/API 
- Python or JS

- Start frontend for project
- 
