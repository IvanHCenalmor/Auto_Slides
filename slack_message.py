import requests
from datetime import datetime, timedelta
import argparse

# Function to send message to Slack
def send_slack_message(token, channel, text):
    url = 'https://slack.com/api/chat.postMessage'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    data = {
        'channel': channel,
        'text': text
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        raise Exception(f"Request to Slack API failed with status code {response.status_code}, response: {response.text}")

# Generate the link to the slides
def generate_slides_link(link, slide_name):
    today = datetime.today()
    # Calculate the number of days until next Monday
    days_until_monday = (7 - today.weekday() + 0) % 7
    if days_until_monday == 0:
        days_until_monday = 7
    next_monday = today + timedelta(days=days_until_monday)
    slide_date = next_monday.strftime('%Y-%m-%d')
    return f'{link}{slide_date}{slide_name}'

# Main function
def main(token, channel, link, slide_name):
    slides_link = generate_slides_link(link, slide_name)
    message = f"Here is the link to this week's slides: {slides_link}"
    send_slack_message(token, channel, message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send a weekly reminder to Slack with a link to slides.')
    parser.add_argument('--token', required=True, help='Slack API token')
    parser.add_argument('--channel', required=True, help='Slack channel ID')
    parser.add_argument('--link', required=True, help='Link to the slides')
    parser.add_argument('--slide_name', required=True, help='Name of the slides, without the date (this will go at the beggining with the Y-M-D format)')

    args = parser.parse_args()
    main(token=args.token, channel=args.channel, link=args.link, slide_name=args.slide_name)