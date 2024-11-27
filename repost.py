from connections import linkedin,twitter

message = input("Enter the post you want to post on Linkedin & Twitter - ")

linkedin.post(message)
twitter.post_tweet(message)