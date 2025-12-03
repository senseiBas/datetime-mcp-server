# datetime-mcp-server

A simple, focused MCP (Model Context Protocol) server that provides current date and time information. This server enables Claude to always get accurate current date/time instead of relying on stale session start dates.

## Features

- **Three datetime tools** for different use cases:
  - `get_current_datetime`: Returns ISO 8601 format with timezone
  - `get_current_date`: Returns date in YYYY-MM-DD format
  - `get_formatted_datetime`: Returns human-readable format

- **Europe/Amsterdam timezone** - All times are in CET/CEST timezone
- **Proper error handling** - Graceful error management
- **Type hints** - Full type annotations for better code quality
- **Clean implementation** - Simple, focused, no extra features

## Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Install from source

1. Clone the repository:
```bash
git clone https://github.com/<ACTUAL_USERNAME_OR_ORG>/datetime-mcp-server.git
cd datetime-mcp-server
```

2. Install the package:
```bash
pip install -e .
```

Or install dependencies directly:
```bash
pip install -r requirements.txt
```

## Usage

### Running the server standalone

You can test the server by running it directly:

```bash
python -m datetime_mcp_server.server
```

### Adding to Claude Desktop

To use this MCP server with Claude Desktop, add the following to your Claude Desktop configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "datetime": {
      "command": "python",
      "args": [
        "-m",
        "datetime_mcp_server.server"
      ],
      "env": {
        "PYTHONPATH": "/absolute/path/to/datetime-mcp-server/src"
      }
    }
  }
}
```

Replace `/absolute/path/to/datetime-mcp-server/src` with the actual absolute path to the `src` directory in your installation.

Alternatively, if you installed the package globally or in a virtual environment:

```json
{
  "mcpServers": {
    "datetime": {
      "command": "python",
      "args": [
        "-m",
        "datetime_mcp_server.server"
      ]
    }
  }
}
```

After updating the configuration, restart Claude Desktop.

## Available Tools

### get_current_datetime

Returns the current date and time in ISO 8601 format with timezone information.

**Example output**: `2025-12-03T14:30:15.123456+01:00`

### get_current_date

Returns just the current date in YYYY-MM-DD format.

**Example output**: `2025-12-03`

### get_formatted_datetime

Returns the current date and time in a human-readable format.

**Example output**: `Wednesday, December 03, 2025 - 14:30:15 CET`

## Development

### Project Structure

```
datetime-mcp-server/
├── src/
│   └── datetime_mcp_server/
│       ├── __init__.py
│       └── server.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

### Running tests

Install dev dependencies:
```bash
pip install -e ".[dev]"
```

Run tests:
```bash
pytest
```

## Technical Details

- **Language**: Python 3.10+
- **Framework**: MCP Python SDK
- **Timezone**: Europe/Amsterdam (CET/CEST)
- **Protocol**: Model Context Protocol (MCP)

## Why This Server?

Claude's knowledge of the current date/time is based on the session start time, which can become stale during long conversations. This MCP server provides a reliable way for Claude to:

- Get the actual current date and time
- Format dates consistently
- Work with accurate timezone information
- Avoid confusion from stale session data

## License

MIT License - feel free to use and modify as needed.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues or questions, please open an issue on the GitHub repository.
