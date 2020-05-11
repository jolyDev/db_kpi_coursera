import collections
import json
import sys


def main():
    tweet_file = open(sys.argv[1])

    hashtags = collections.defaultdict(int)

    for line in tweet_file.readlines():
        tweet = json.loads(line)
        if "entities" in tweet:
            entities = tweet["entities"]
            tweet_hashtags = entities["hashtags"]

            for hashtag in tweet_hashtags:
                text = hashtag["text"]
                hashtags[text] += 1

    k = collections.Counter(hashtags)
    high = k.most_common(10)
    for i in high:
        print(i[0] + " " + str(i[1]))


if __name__ == '__main__':
    main()
