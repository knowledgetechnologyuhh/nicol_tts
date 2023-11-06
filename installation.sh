python3 -m venv env
source env/bin/activate
pip install wheel
pip install -r requirements.txt
python nicol_speech.py

# For video_talker_cached.py:
# sudo apt install sox libgirepository1.0-dev espeak-ng
# pip install sox
# pip install pygobject
# mkdir talker_cache
