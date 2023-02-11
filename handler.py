import json
from wiktionaryparser import WiktionaryParser

def scrape_for_word(word):
    wtp = WiktionaryParser()
    word = wtp.fetch(word, "Finnish")
    return word

def word(event, context):
    body = json.loads(event['body'])
    word = body['word']
    result = scrape_for_word(word)
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
