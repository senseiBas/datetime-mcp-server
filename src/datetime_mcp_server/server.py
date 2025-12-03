"""
Datetime MCP Server

A simple MCP server that provides current date and time information
in the Europe/Amsterdam timezone.
"""

import logging
from datetime import datetime
from typing import Any
from zoneinfo import ZoneInfo

from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("datetime-mcp-server")

# Timezone constant
TIMEZONE = ZoneInfo("Europe/Amsterdam")

# Initialize MCP server
app = Server("datetime-mcp-server")


def get_current_time() -> datetime:
    """
    Get the current datetime in Europe/Amsterdam timezone.

    Returns:
        datetime: Current datetime with Amsterdam timezone
    """
    return datetime.now(TIMEZONE)


@app.list_tools()
async def list_tools() -> list[Tool]:
    """
    List available datetime tools.

    Returns:
        list[Tool]: List of available MCP tools
    """
    return [
        Tool(
            name="get_current_datetime",
            description="Returns the current date and time in ISO 8601 format with timezone information (Europe/Amsterdam)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="get_current_date",
            description="Returns just the current date in YYYY-MM-DD format (Europe/Amsterdam timezone)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="get_formatted_datetime",
            description="Returns the current date and time in a human-readable format: 'DayOfWeek, Month DD, YYYY - HH:MM:SS TZ' (Europe/Amsterdam timezone)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """
    Handle tool execution requests.

    Args:
        name: Name of the tool to execute
        arguments: Tool arguments (not used for datetime tools)

    Returns:
        list[TextContent]: Tool execution results

    Raises:
        ValueError: If tool name is unknown
    """
    try:
        if name == "get_current_datetime":
            current_time = get_current_time()
            iso_format = current_time.isoformat()
            logger.info(f"get_current_datetime called: {iso_format}")
            return [TextContent(
                type="text",
                text=iso_format
            )]

        elif name == "get_current_date":
            current_time = get_current_time()
            date_format = current_time.strftime("%Y-%m-%d")
            logger.info(f"get_current_date called: {date_format}")
            return [TextContent(
                type="text",
                text=date_format
            )]

        elif name == "get_formatted_datetime":
            current_time = get_current_time()
            # Format: "Wednesday, December 03, 2025 - 14:30:15 CET"
            formatted = current_time.strftime("%A, %B %d, %Y - %H:%M:%S %Z")
            logger.info(f"get_formatted_datetime called: {formatted}")
            return [TextContent(
                type="text",
                text=formatted
            )]

        else:
            error_msg = f"Unknown tool: {name}"
            logger.error(error_msg)
            raise ValueError(error_msg)

    except Exception as e:
        error_msg = f"Error executing tool {name}: {str(e)}"
        logger.error(error_msg)
        return [TextContent(
            type="text",
            text=f"Error: {str(e)}"
        )]


async def main():
    """Main entry point for the MCP server."""
    logger.info("Starting Datetime MCP Server")
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
