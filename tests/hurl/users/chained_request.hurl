GET https://api.example.com/species/1
HTTP 200
[Captures]
species_url: jsonpath "$.species.url"

GET {{species_url}}
HTTP 200
