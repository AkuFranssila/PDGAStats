*** Frontend ***

*** Backend ***

*** Crawler ***

Crawl single player stats

`python -m player.playerRawDataCrawler --pdgaNumber 44708`

Crawl latest PDGA Number on player

`python -m player.playerLatestIdCrawler`

Run larger batch of PDGA numbers

`python -m runners.runPlayerRawData --type test --startId 1 --endId 5`

Crawl tournament with specific ID

`python -m tournament.tournamentRawDataCrawler --tournamentId 52082`

Run all unit tests

`python -m unittest discover`

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
