import os
import subprocess
import shutil
import click
import json
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class YouTubeToTextConverter:

	def __init__(self, apikey, watson_url, url, language='en', default_folder='./temp', convert=True):
		self.apikey = apikey
		self.watson_url = watson_url
		self.url = url
		self.language = language
		self.default_folder = default_folder
		if convert:
			self.download_video_and_metadata()
			self.video_to_audio()

	def download_video_and_metadata(self):
		if os.path.exists(self.default_folder):
			if click.confirm(f'Default folder {self.default_folder} already exist. Do you want to delete it and continue?'):
				self.clean_temp()				
				command = f'youtube-dl {self.url} -o {self.default_folder}/you_tube --write-info-json'
				subprocess.call(command, shell=True)
				self.video_title = self.get_video_metadata()['title']
				click.echo(f'Video "{self.video_title}" Downloaded.')
			else:
				click.echo(f'Video "{self.url}" download interrupt.')

	def get_video_metadata(self):
		metadata_path = f'{self.default_folder}/you_tube.info.json'
		if os.path.exists(metadata_path):
			file = open(metadata_path, 'r')
			json_data = json.load(file)
			self.video_metadata = json_data
			click.echo(f'Video {self.video_metadata['title']} metadata retrieved.')
			return json_data
		else:
			click.echo(f'Metadata path "{metadata_path}" invalid.')
	
	def video_to_audio(self):		
		# Nedd ffmpeg installed
		# https://linuxize.com/post/how-to-install-ffmpeg-on-ubuntu-18-04/
		video_path = f'{self.default_folder}/you_tube.mkv'
		if os.path.exists(video_path):
			command = f'ffmpeg -i {video_path} -ab 160k -ar 44100 -vn {self.default_folder}/audio.wav'
			subprocess.call(command, shell=True)
			click.echo(f'Video "{self.video_title}" converted to audio.')
		else:
			click.echo(f'Video path "{video_path}" invalid.')

	def setup_watson_service(self):
		authenticator = IAMAuthenticator(self.apikey)
		stt = SpeechToTextV1(authenticator=authenticator)
		stt.set_service_url(self.url)
		return stt

	def audio_to_text(self):
		audio_path = f'{self.default_folder}/audio.wav'
		if os.path.exists(audio_path):
			with open(audio_path, 'rb') as f:
			    res = stt.recognize(audio=f, content_type='audio/wav', model='en-AU_NarrowbandModel', continuous=True).get_result()
			return res	
		else:
			click.echo(f'Audio path "{audio_path}" invalid.')	    
	
	def clean_temp(self):
		shutil.rmtree(self.default_folder)
