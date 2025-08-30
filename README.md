# Speech Classification and Emotion Analysis

![Python](https://img.shields.io/badge/Python-TensorFlow-blue)

This repository contains complementary machine learning projects demonstrating advanced audio and natural language processing techniques for speech classification and emotion analysis.

## Projects Overview

### Speech Classification
- **Objective:** Classify 6 speech categories — bird, dog, cat, down, eight, and bed — using audio data.
- **Dataset:** Over 1200 audio samples (200 files per category) sourced from Kaggle.
- **Approach:** CNN-based model optimized for speech recognition.
- **Performance:** Achieves ~84% accuracy after 50 epochs.
- **Features:**
  - Audio preprocessing (MFCC, spectrograms)
  - CNN architecture tailored for audio feature extraction
  - Detailed training/testing accuracy tracking

### Emotion Analysis from Twitter News
- **Objective:** Classify emotions in Twitter news text data.
- **Approach:** NLP pipeline for emotion classification.
- **Performance:** ~75% accuracy.
- **Features:**
  - Text preprocessing (tokenization, normalization, stopword removal)
  - Emotion classification techniques for sentiment analysis

## Installation

Clone the repository:

git clone https://github.com/yourusername/speech-emotion-analysis.git
cd speech-emotion-analysis

text

Install dependencies (recommended: use a virtual environment):

pip install -r requirements.txt

text

Download and prepare datasets following `DATASETS.md` instructions.

## Usage

### Speech Classification

Train the CNN model:

python train_speech_model.py --epochs 50

text

Evaluate and predict on test audio:

python evaluate_speech_model.py --input <audio_file>

text

### Emotion Analysis

Run emotion classification on Twitter news data:

python run_emotion_analysis.py --input <twitter_news_file>

text

Check classification report and accuracy metrics in the output.

## Results

- Speech classification accuracy: ~84% after 50 epochs.
- Emotion analysis accuracy: ~75% on Twitter news text.

Includes sample graphs, model checkpoints, and logs.

## Future Work

- Real-time emotion recognition from speech integration.
- Expand speech categories and dataset size.
- Deploy interactive web or mobile app interface.

## License

This project is licensed under the MIT License.

## Acknowledgements

Thanks to course instructors and open-source communities for tools and support.
