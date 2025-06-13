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
            para = child.get("paragraph", {})
            text = para.get("text", [])
            content += "".join([t.get("plain_text", "") for t in text]) + "\n\n"
        elif child["type"] == "heading_1":
            heading = child.get("heading_1", {})
            text = heading.get("text", [])
            content += "# " + "".join([t.get("plain_text", "") for t in text]) + "\n\n"
        elif child["type"] == "heading_2":
            heading = child.get("heading_2", {})
            text = heading.get("text", [])
            content += "## " + "".join([t.get("plain_text", "") for t in text]) + "\n\n"
        elif child["type"] == "heading_3":
            heading = child.get("heading_3", {})
            text = heading.get("text", [])
            content += "### " + "".join([t.get("plain_text", "") for t in text]) + "\n\n"
        # Optionally add more types here with similar .get() checks
    return content

def save_to_file(content):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# Synced Notion Notes\n\n")
        f.write(content)
        f.write(f"\n_Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n")

if __name__ == "__main__":
    content = fetch_page_content(NOTION_PAGE_ID)
    save_to_file(content)
