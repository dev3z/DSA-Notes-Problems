import os
from notion_client import Client

# Initialize Notion client
notion = Client(auth=os.getenv("NOTION_TOKEN"))

def fetch_page_content(page_id):
    md_lines = []
    start_cursor = None

    while True:
        response = notion.blocks.children.list(
            block_id=page_id,
            start_cursor=start_cursor
        )
        blocks = response.get("results", [])

        for block in blocks:
            block_type = block.get("type")
            data = block.get(block_type, {})

            rich_text = data.get("rich_text", [])
            text = "".join([t.get("plain_text", "") for t in rich_text])

            if block_type == "paragraph":
                if text.strip():
                    md_lines.append(text)

            elif block_type in ["heading_1", "heading_2", "heading_3"]:
                level = int(block_type[-1])
                md_lines.append(f"{'#' * level} {text}")

            elif block_type == "bulleted_list_item":
                md_lines.append(f"- {text}")

            elif block_type == "numbered_list_item":
                md_lines.append(f"1. {text}")

            # Optional: handle more types (to_do, code, toggle, etc.)

        if not response.get("has_more"):
            break

        start_cursor = response.get("next_cursor")

    return "\n\n".join(md_lines)


if __name__ == "__main__":
    notion_page_id = os.getenv("NOTION_PAGE_ID")
    if not notion_page_id:
        raise ValueError("Missing NOTION_PAGE_ID environment variable")

    content = fetch_page_content(notion_page_id)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ Notion content written to README.md")
