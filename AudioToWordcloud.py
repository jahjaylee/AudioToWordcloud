from rev_ai import speechrec
import time
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud


class AudioToWordcloudConverter:

    def __init__(self, api_key):
        if not api_key:
            raise ValueError("self.api Key cannot be empty.")
        self.api = speechrec.RevSpeechAPI(api_key)

    def submit_job(self, jobUrl):
        result = self.api.submit_job_url(jobUrl)
        return result['id']

    def poll_for_completion(self, jobId):
        status = self.api.view_job(jobId)['status']
        while status == 'in_progress':
            print 'Transcribing'
            time.sleep(15)
            status = self.api.view_job(jobId)['status']
        return

    def create_wordcloud(self, jobId, name):
        result = self.api.get_transcript(jobId, False)
        cleaned = re.sub(r'Speaker \d    \d\d:\d\d    ', "", result)
        wordcloud = WordCloud().generate(cleaned)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.savefig(name + '.png', dpi=300)

    def convert_audio_to_wordcloud(self, mediaUrl, wordcloudName):
        jobId = self.submit_job(mediaUrl)
        self.poll_for_completion(jobId)
        self.create_wordcloud(jobId, wordcloudName)
        print "Wordcloud Created"
