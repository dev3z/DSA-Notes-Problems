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
            text = "".join([t.get("plain_text", "") for t in data.get("rich_text", [])])
            if text.strip():
                md_lines.append(text)

        # Handle headings
        elif block_type in ["heading_1", "heading_2", "heading_3"]:
            level = int(block_type[-1])
            text = "".join([t.get("plain_text", "") for t in data.get("rich_text", [])])
            md_lines.append(f"{'#' * level} {text}")

        # Handle bullets
        elif block_type in ["bulleted_list_item", "numbered_list_item"]:
            text = "".join([t.get("plain_text", "") for t in data.get("rich_text", [])])
            prefix = "-" if block_type == "bulleted_list_item" else "1."
            md_lines.append(f"{prefix} {text}")

        # You can add more types here (code, to_do, etc.)

    return "\n\n".join(md_lines)
