from fastmcp import FastMCP
from simplejustwatchapi import details, offers_for_countries, search, MediaEntry, Offer

mcp = FastMCP("JustWatchServer")


@mcp.tool()
def justwatch_search_movie(
    title: str,
    country: str = "GB",
    language: str = "en",
    page_size: int = 3,
    best_only: bool = True,
) -> list[MediaEntry]:
    """Search for movies using JustWatch."""
    return search(title, country, language, page_size, best_only)


@mcp.tool()
def justwatch_get_movie_details(
    entity_id: str, country: str = "GB", language: str = "en", best_only: bool = True
) -> MediaEntry:
    """Get detailed information about a movie using JustWatch"""
    return details(entity_id, country, language, best_only)


@mcp.tool()
def justwatch_get_offers_for_country(
    entity_id: str, country: str, language: str = "en", best_only: bool = True
) ->  dict[str, list[Offer]]:
    """Get offers for a given country using JustWatch"""
    return offers_for_countries(entity_id, {country}, language, best_only)


if __name__ == "__main__":
    mcp.run(transport="stdio")
