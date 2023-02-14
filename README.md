# Serverless Lambda API for scraping Wikitonary for Finnish word definitions

This is a serverless API for scraping Wiktionary for Finnish word definitions. It is built using the Serverless framework and uses AWS Lambda and Python package `wiktionaryparser` for scraping. 

## Used in the following project

- [wikifi-chrome-extension](https://github.com/shamsch/wikifi-chrome-extension)

## Sample API call and response

**POST Request**
```bash
curl -X POST \
  https://<API-URL>.com/word/prod \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: <API-KEY>' \
  -d '{
    "word": "kissa"
}'
```
**JSON Response**
```json
[
	{
		"etymology": "Borrowed from Swedish kisse, kissa (“cat”), with other dialectal forms including kise, kiss. Probably ultimately from a cat call \"kis-kis-kis\" used throughout Europe (see kis; also compare Russian киса (kisa)).\n",
		"definitions": [
			{
				"partOfSpeech": "noun",
				"text": [
					"kissa",
					"cat (Felis catus)",
					"(slang) cat, chick, fox (a sexy young woman)"
				],
				"relatedWords": [
					{
						"relationshipType": "synonyms",
						"words": [
							"(colloquial) katti",
							"(diminutive) mirri, kissimirri",
							"(child's speech) kissi, kisu",
							"(species) kesykissa, kotikissa"
						]
					},
					{
						"relationshipType": "hyponyms",
						"words": [
							"kissanpentu",
							"kolli"
						]
					}
				],
				"examples": [
					"Kukas sen kissan hännän nostaisi, ellei kissa itse? ― Who would raise the cat's tail if not the cat itself?"
				]
			}
		],
		"pronunciations": {
			"text": [
				"IPA: /ˈkisːɑ/, [ˈkis̠ːɑ]",
				"Rhymes: -isːɑ",
				"Syllabification: kis‧sa"
			],
			"audio": []
		}
	}
]
```



