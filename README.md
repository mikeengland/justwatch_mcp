# JustWatch MCP Server

An MCP server which wraps the [simple-justwatch-python-api](https://github.com/Electronic-Mango/simple-justwatch-python-api) library.

It provides three tools:
* justwatch_search_movie - Search for movies using JustWatch.
* justwatch_get_movie_details - Get detailed information about a movie using JustWatch
* justwatch_get_offers_for_country - Get offers for a given country using JustWatch

This allows you to ask questions such as "where can i watch pearl harbour for free in the uk"

## Setting up this MCP server
You can set this sever up in Claude Desktop with the following configuration:

```json
{
  "justwatch": {
    "command": "<path to uv>",
    "args": [
      "--directory",
      "<repo directory>",
      "run",
      "main.py"
    ]
  }
}
```