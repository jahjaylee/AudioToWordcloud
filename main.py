import AudioToWordcloud

api_key = '-------YOUR API KEY HERE--------------'


def main(mediaUrl, wordcloudName):
    converter = AudioToWordcloud.AudioToWordcloudConverter(api_key)
    converter.convert_audio_to_wordcloud(mediaUrl, wordcloudName)


if __name__ == '__main__':
    main('https://support.rev.com/hc/en-us/article_attachments/200043975/FTC_Sample_1_-_Single.mp3', 'TestCloud')
