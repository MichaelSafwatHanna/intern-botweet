class Tweet:

    def __init__(self, day, message, tone_analysis):
        self.day = day
        self.message = message
        self.tone_analysis = tone_analysis

    def to_string(self):
        to_return = f"Day [{str(self.day)}]: {self.message}"

        if self.tone_analysis['tones']:
            to_return += "\nStats:\n"
            for tone in self.tone_analysis['tones']:
                to_return += f"[{tone['tone_name']}]: {str('{0:.3f}'.format(tone['score']))}\n"

        return to_return.strip()
