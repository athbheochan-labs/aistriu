from typing import Any


def map_irish_projects(matches: list[dict[str, Any]]) -> list[dict[str, Any]]:
    mapped_projects = []

    for match in matches:
        project = match["project"]
        irish_stats = match["irish_stats"]

        mapped_projects.append(
            {
                "name": project["name"],
                "slug": project["slug"],
                "web_url": project["web_url"],
                "locked": project["locked"],
                "irish": {
                    "translated_percent": irish_stats["translated_percent"],
                    "translated_strings": irish_stats["translated"],
                    "total_strings": irish_stats["total"],
                    "translated_words": irish_stats["translated_words"],
                    "total_words": irish_stats["total_words"],
                    "translated_chars": irish_stats["translated_chars"],
                    "total_chars": irish_stats["total_chars"],
                    "fuzzy": irish_stats["fuzzy"],
                    "failing": irish_stats["failing"],
                    "suggestions": irish_stats["suggestions"],
                    "comments": irish_stats["comments"],
                    "last_change": irish_stats["last_change"],
                    "url": irish_stats["url"],
                    "translate_url": irish_stats["translate_url"],
                },
            }
        )

    return mapped_projects
