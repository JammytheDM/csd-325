def city_country(city, country, population=None, language=None):
    """Return a formatted city, country, and optional details."""
    result = f"{city}, {country}"

    if population is not None:
        result += f" - population {population}"

    if language is not None:
        result += f", {language}"

    return result


print(city_country("Santiago", "Chile"))
print(city_country("Tokyo", "Japan", 14000000))
print(city_country("Nairobi", "Kenya", 4397000, "Swahili"))