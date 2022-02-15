from utils.color import Color
from utils.logger import Logger
from bot_modules.reddit_handler import RedditHandler
from utils import env

class MarkRead:

    def __init__(self):
        self.reddit = RedditHandler()
        self.bot_username = env.BOT_USERNAME

    def reset(self):
        reset = False
        while not reset:
            self.reddit.reset()
            reset = True

    def mark_read(self):
        Logger.log('Reading inbox...')
        unread = self.reddit.get_unread()
        unread.reverse() # back to original order

        Logger.log(str(len(unread)) + ' Unread Messages')

        num_messages = 0
        num_marked_read = 0
        for message in unread:
            num_messages += 1
            username = str(message.author).lower()
            if username == self.bot_username and message.subject == self.bot_username + ' - Exception Handled':
                message.mark_read()
                num_marked_read += 1
                Logger.log(str(num_marked_read) + ' marked read')

        Logger.log(str(num_messages) + ' unread ERROR messages handled')
        Logger.log(str(num_marked_read) + ' ERROR messages marked read')

        return num_marked_read
