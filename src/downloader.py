"""
This script helps retrieve the audio files for Youtube URL's using the
:mod: `youtube_dl` for each of the URL links in the `src/links.txt` file
at the highest audio-rate. This, furthermore, can be used for the short-speech
corpus creation, which is the central idea of this project.

Author:
-------
Aashish Yadavally
"""
import os
import argparse
import youtube_dl


class Corpus:
    def __init__(self, links_dict, output_dir):
        """Initializes the :class: `Corpus` to retrieve highest audio-rate
        audio files from Youtube

        Args:
            links_dict (dict):
                Dictionary containing reference id's and URL's of Youtube
                videos
            output_dir (str):
                Name of folder the retrieved files will be moved to
        """
        self.links_dict = links_dict
        self.output_dir = output_dir

    def setup(self):
        """Sets up the output directory with the name defined for 'output_dir'
        with the audio files retrieved from Youtube
        """
        if os.path.isdir(self.output_dir):
            pass
        else:
            os.mkdir(self.output_dir)

        for output_name, link in self.links_dict.items():
            self.retrieve(output_name, link)

    def retrieve(self, output_name, link):
        """Retrieves the Youtube audio files using the :mod: `youtube_dl`
        """
        ydl_opts = {
            'outtmpl': os.path.join(self.output_dir, output_name) + '.mp3',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])


def main():
    parser = argparse.ArgumentParser(description='Short-Vocabulary Hindi\
                                     Speech Corpus')
    parser.add_argument('--lfile', dest='lfile', type=str,
                        default='links.txt',
                        help='Text file containing Youtube video links')
    parser.add_argument('--odir', dest='output_dir', type=str,
                        default='audios',
                        help='Name of output directory')
    args = parser.parse_args()

    with open(args.lfile, 'r') as links_file:
        contents = links_file.readlines()
        links_dict = {}
        for line in contents:
            temp = line.strip().split()
            if len(temp) != 2:
                print('Error in links file: Empty line/ No Reference ID')
            else:
                links_dict[temp[0]] = temp[1]
    corpus = Corpus(links_dict, args.output_dir)
    corpus.setup()


if __name__ == '__main__':
    main()
