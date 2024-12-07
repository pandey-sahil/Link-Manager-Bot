echo "Cloning Repo...."
git clone https://github.com/pandey-sahil/Link-Manager-Bot.git /ShortnerBot
cd /ShortnerBot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
