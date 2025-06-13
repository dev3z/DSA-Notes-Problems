from notion_client import Client
import os

notion = Client(auth=os.getenv("NOTION_TOKEN"))

def fetch_page_content(page_id):
    blocks = []
    start_cursor = None

    while True:
        response = notion.blocks.children.list(block_id=page_id, start_cursor=start_cursor)
        blocks.extend(response["results"])
        if not response.get("has_more"):
            break
        start_cursor = response.get("next_cursor")

    md_lines = []

    for block in blocks:
        block_type = block["type"]
        data = block[block_type]

        # Handle paragraphs
        if block_type == "paragraph":
            rich_text = data.get("rich_text", [])
            text = "".join([t.get("plain_text", "") for t in rich_text])
            if text.strip():
                md_lines.append(text)

        # Headings
        elif block_type in ["heading_1", "heading_2", "heading_3"]:
            level = int(block_type[-1])
            rich_text = data.get("rich_text", [])
            text = "".join([t.get("plain_text", "") for t in rich_text])
            md_lines.append(f"{'#' * level} {text}")

        # Bullets & numbered
        elif block_type in ["bulleted_list_item", "numbered_list_item"]:
            prefix = "-" if block_type == "bulleted_list_item" else "1."
            rich_text = data.get("rich_text", [])
            text = "".join([t.get("plain_text", "") for t in rich_text])
            md_lines.append(f"{prefix} {text}")

    return "\n\n".join(md_lines)
