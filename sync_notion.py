# sync_notion.py
import os
from notion_client import Client
from datetime import datetime

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_PAGE_ID = os.getenv("NOTION_PAGE_ID")

notion = Client(auth=NOTION_TOKEN)

def fetch_page_content(page_id):
    from notion_client.helpers import get_id
   block_id = page_id
    children = notion.blocks.children.list(block_id)["results"]
    content = ""
    for child in children:
        if child["type"] == "paragraph":
            text = child["paragraph"]["text"]
            content += "".join([t["plain_text"] for t in text]) + "\n\n"
        elif child["type"] == "heading_1":
            text = child["heading_1"]["text"]
            content += "# " + "".join([t["plain_text"] for t in text]) + "\n\n"
        elif child["type"] == "heading_2":
            text = child["heading_2"]["text"]
            content += "## " + "".join([t["plain_text"] for t in text]) + "\n\n"
        elif child["type"] == "heading_3":
            text = child["heading_3"]["text"]
            content += "### " + "".join([t["plain_text"] for t in text]) + "\n\n"
    return content

def save_to_file(content):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# Synced Notion Notes\n\n")
        f.write(content)
        f.write(f"\n_Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n")

if __name__ == "__main__":
    content = fetch_page_content(NOTION_PAGE_ID)
    save_to_file(content)
