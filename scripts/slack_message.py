import requests
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

# Main function
def main(token, channel, link, date):
    message = f"Here is the link to next week's slides ({date}): {link}"
    send_slack_message(token, channel, message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send a weekly reminder to Slack with a link to slides.')
    parser.add_argument('--token', required=True, help='Slack API token')
    parser.add_argument('--channel', required=True, help='Slack channel ID')
    parser.add_argument('--link', required=True, help='Link to the slides')
    parser.add_argument('--date', required=True, help='Date for the slides')

    args = parser.parse_args()
    main(token=args.token, channel=args.channel, link=args.link, date=args.date)