import requests
from bs4 import BeautifulSoup
import html2text
import os

if __name__ == "__main__":
    url = "https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview"
    base_url = "https://docs.anthropic.com"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    # Select the Claude Code section
    claude_links = soup.select("div#navigation-items ul li a")

    # Filter only links under the Claude Code <ul> (not top nav)
    filtered_links = [
        (a.get_text(strip=True), f"{base_url}{a["href"]}")
        for a in claude_links
        if a["href"].startswith("/en/docs/claude-code/")
    ]

    # Store Each Menu Url
    documentation_menu = {}
    for text, href in filtered_links:
        documentation_menu[text] = href

    # Save to claude_docs
    SAVE_DIR = "claude_docs"
    os.makedirs(SAVE_DIR, exist_ok=True)

    # Markdown converter
    converter = html2text.HTML2Text()
    converter.ignore_links = False

    for title, url in documentation_menu.items():
        response = requests.get(url)
        page = BeautifulSoup(response.text, "lxml")
        content_div = page.select_one("#content-area")
        if not content_div:
            print(f"Skipping: {url}")
            continue

        markdown = converter.handle(str(content_div))

        # Clean filename
        filename = f"{title.lower().replace(' ', '_')}.md"
        with open(os.path.join(SAVE_DIR, filename), "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n{markdown}")
            print(f"Saved: {filename}")
