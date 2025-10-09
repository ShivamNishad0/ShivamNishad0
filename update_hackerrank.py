import requests
from bs4 import BeautifulSoup
import re
import os

USERNAME = os.getenv("HACKERRANK_USERNAME", "2313672_mca_1_B")
URL = f"https://www.hackerrank.com/{USERNAME}"

def get_profile_data():
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Example: problems solved
    stats = soup.find_all("div", class_="hacker-card__box")
    problems_solved = "N/A"
    if stats:
        for s in stats:
            if "Problems Solved" in s.text:
                problems_solved = re.sub(r"[^0-9]", "", s.text)
    
    return problems_solved

if __name__ == "__main__":
    solved = get_profile_data()
    print(f"Problems solved: {solved}")

    # Update README
    with open("README.md", "r") as f:
        content = f.read()

    new_content = re.sub(r"<!--HACKERRANK_START-->.*<!--HACKERRANK_END-->",
                         f"<!--HACKERRANK_START-->\nSolved: {solved} problems\n<!--HACKERRANK_END-->",
                         content, flags=re.DOTALL)

    with open("README.md", "w") as f:
        f.write(new_content)
