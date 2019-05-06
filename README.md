# Hindi-Speech-Corpus
  ## Goal
  To build a short-vocabulary 1 hour Hindi Speech Corpus which can be used for Automatic Speech Recognition, and further perform acoustic and phonemic analysis on the dataset.
  
  ## Getting Started
  These instructions describe the prerequisites and steps to get started with the project.

  ### Setup
  To setup an Anaconda environment in-built with all the prerequisite packages used to retrieve the audio files from [Youtube](www.youtube.com), do the following:
  1. Download [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/), and install the same using `> bash install conda_install.sh`
  
  2. Create a conda environment from the included `environment.yml` file using the following command:
     
     `$ conda env create -f environment.yml`
  3. Activate the environment
     
     `$ conda activate hscorpus`

  ### Usage
  To retrieve audio files from Youtube, write the URL's of the required files in the `src/links.txt` alongwith a Reference ID. Now, run the script `downloader.py` using the command: `> python downloader.py`. This will create an `audios` directory in the current working directory containing the retrieved audio files with their reference IDs. To change the defaults for the `downloader.py` script, run `> python downloader.py --help` to receive a list of arguments accessible to the user.
  
  ## Project Design
  The short-vocabulary Hindi speech corpus is stored in the `corpus` directory.
  
  ### Data
  The dataset is created from the audio files in `audios` directory, by breaking them down into sentences using the [Praat](http://www.fon.hum.uva.nl/praat/) software and [Audacity](https://www.audacityteam.org/) software. All of the files retrieved by this procedure are saved in the `data` sub-directory within the `corpus` directory.

  ### Files for Acoustic Modeling
  The files required for acoustic modeling in the Automatic Speech Recognition application include `speaker_to_gender.txt` and `text.txt`. The `speaker_to_gender.txt` file contains information mapping speaker IDs to their genders. The `text.txt` file contains information mapping audio data utterance ID's to their text transcriptions.
  
  ### Files for Language Modeling
  The files required for language modeling in the Automatic Speech Recognition application include `lexicon.txt` and `nonsilence_phones.txt`. The former contains information mapping all the words in the dataset with their corresponding phoneme transcriptions, while the latter includes all the individual phonemes used in the dataset.
  
  ## Contributors
  See [Contributors]() file for more details.
  
  ## License
  This project is licensed with MIT License. See [License]() file for more details.
