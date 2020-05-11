import json
import re
import sys


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    for line in tweet_file.readlines():
        tweet = json.loads(line)
        if "text" in tweet:
            text = tweet["text"]
            words = re.split(r"[\s.,?:]+", text)
            sentiment = 0
            for word in words:
                if word in scores:
                    sentiment = sentiment + scores[word]

            print(sentiment)


if __name__ == '__main__':
    main()
