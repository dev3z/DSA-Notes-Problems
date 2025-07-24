import os
from notion_client import Client
from datetime import datetime

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_PAGE_ID = os.getenv("NOTION_PAGE_ID")

notion = Client(auth=NOTION_TOKEN)

def extract_text_from_block(block):
    block_type = block["type"]
    if "rich_text" in block[block_type]:
        return "".join([t.get("plain_text", "") for t in block[block_type]["rich_text"]])
    return ""

def fetch_blocks(block_id, depth=0):
    blocks = notion.blocks.children.list(block_id)["results"]
    content = ""
    for block in blocks:
        block_type = block["type"]
        text = extract_text_from_block(block)

        if block_type == "paragraph":
            content += text + "\n\n"
        elif block_type == "heading_1":
            content += "# " + text + "\n\n"
        elif block_type == "heading_2":
            content += "## " + text + "\n\n"
        elif block_type == "heading_3":
            content += "### " + text + "\n\n"
        elif block_type == "bulleted_list_item":
            content += "- " + text + "\n"
        elif block_type == "numbered_list_item":
            content += f"{depth + 1}. " + text + "\n"
        elif block_type == "code":
            content += "```\n" + text + "\n```\n\n"

        # Recursively fetch nested content
        if block.get("has_children"):
            content += fetch_blocks(block["id"], depth + 1)

    return content

def save_to_file(content):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# Synced Notion Notes\n\n")
        f.write(content.strip())
        f.write(f"\n\n_Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n")

if __name__ == "__main__":
    content = fetch_blocks(NOTION_PAGE_ID)
    print("✅ Synced content preview:\n", content[:500])
    save_to_file(content)
