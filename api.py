from instabot import Bot
import time
import re

# Initialize the bot
bot = Bot()
bot.login(username="Your_Username", password="Your_Password")  # Provide your Instagram credentials

# Function to follow accounts based on various acronyms and hashtags, excluding specific graduation year
def follow_filtered_accounts(acronyms, graduation_year, excluded_year, hashtags, max_to_follow):
    all_users = bot.get_user_medias(bot.user_id)  # Get the bot's user ID to filter followers
    for user_id in all_users:
        user_info = bot.get_user_info(user_id)
        if (
            "biography" in user_info
            and any(re.search(fr"\b{acronym}\b", user_info["biography"], re.IGNORECASE) for acronym in acronyms)
            and re.search(f"'{graduation_year[-2:]}", user_info["biography"])
            and not re.search(f"'{excluded_year[-2:]}", user_info["biography"])
        ):
            post = bot.get_media_info(user_id)
            for tag in hashtags:
                if tag in post.get("caption", ""):
                    bot.follow(user_id)
                    time.sleep(10)  # Adding a delay to avoid rate limits

# Function to upload photos at regular intervals
def upload_photos(images_to_post, interval, max_photos):
    for i in range(max_photos):
        for image_path in images_to_post:
            bot.upload_photo(image_path, caption="Your caption here")
            time.sleep(interval)
    
# Example usage with multiple acronyms and hashtags
# Replace 'Your_Username', 'Your_Password', 'acronyms', 'graduation_year', 'excluded_year', and 'hashtags' with your data
university_acronyms = ['MHS', 'ABC']  # List of university acronyms
grad_year = '24'  # The graduation year to search for in bios
excluded_grad_year = '23'  # The year to exclude from bios
hashtag_values = ['#chineseuniversity', '#education', '#tech']  # Hashtags to search for in post captions
max_follow_accounts = 50  # Maximum number of student accounts to follow
max_photos_to_post = 50  # Maximum number of photos to post
post_interval = 14400  # 4 hours in seconds (4 hours * 60 minutes * 60 seconds)

# Loop for following accounts every 4 hours
while True:
    follow_filtered_accounts(university_acronyms, grad_year, excluded_grad_year, hashtag_values, max_follow_accounts)
    time.sleep(post_interval)

# Loop for uploading photos every 4 hours
while True:
    upload_photos(['path/to/image1.jpg', 'path/to/image2.jpg'], post_interval, max_photos_to_post)
    time.sleep(post_interval)
