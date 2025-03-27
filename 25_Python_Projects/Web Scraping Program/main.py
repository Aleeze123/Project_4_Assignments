import requests
from bs4 import BeautifulSoup
from termcolor import colored
def get_github_profile_image_url(github_url):
    try:
        response = requests.get(github_url)
        if response.status_code != 200:
            print(colored(f"Failed to retrieve the page. Status code: {response.status_code}", 'red'))
            return None
        soup = BeautifulSoup(response.content, 'html.parser')
        avatar = soup.find('img', {'class': 'avatar-user'})
        if avatar and 'src' in avatar.attrs:
            image_url = avatar['src']
            if image_url.startswith('//'):
                image_url = 'https:' + image_url
            return image_url
        else:
            print(colored("Profile image not found.", 'red'))
            return None
    except requests.exceptions.RequestException as e:
        print(colored(f"An error occurred: {e}", 'red'))
        return None
def main():
    github_url = input(colored("Enter the GitHub user profile URL: ", 'magenta')).strip()
    image_url = get_github_profile_image_url(github_url)
    if image_url:
        print(colored(f"Profile image URL: {image_url}", 'cyan'))

if __name__ == "__main__":
    main()
