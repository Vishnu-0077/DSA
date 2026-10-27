
class Twitter:

    def __init__(self):
        self.feed = {}
        self.follows = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.feed:
            self.feed[userId] = []
        if userId not in self.follows:
            self.follows[userId] = [userId]
        self.feed[userId].append([self.time,tweetId])
        self.time+=1

    def getNewsFeed(self, userId: int) -> list[int]:
        total_feed = []
        for uid in self.follows.get(userId, [userId]):
            total_feed.extend(self.feed.get(uid, []))

        sorted_feed = sorted(total_feed, key = lambda x:x[0],reverse=True)
        final = []
        for x in sorted_feed[:10]:
            final.append(x[1])
        return final

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = [followerId]
        if followeeId not in self.follows:
            self.follows[followeeId] = [followeeId]
        if followeeId not in self.follows[followerId]:
            self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId and followerId in self.follows:
            if followeeId in self.follows[followerId]:
                self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)