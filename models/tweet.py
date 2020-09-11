import datetime

from services import decorator
from services.config import day_zero


class Tweet:

    def __init__(self, index, message, tone_analysis, in_reply_to_id):
        self.day = (datetime.date.today() - day_zero).days
        self.index = index
        self.message = message
        self.tone_analysis = tone_analysis
        self.in_reply_to_id = in_reply_to_id

    def to_string(self):
        to_return = f"Day [{str(self.day)}{decorator.to_subscript_number(self.index)}]: {self.message}"
        if self.tone_analysis['tones']:
            to_return += "\nStats:\n"
            for tone in self.tone_analysis['tones']:
                to_return += f"[{tone['tone_name']}]: {str('{0:.3f}'.format(tone['score']))}\n"

        return to_return.strip()
