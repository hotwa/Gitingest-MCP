FROM python:3.12-alpine

WORKDIR /app

# Install uv
RUN pip install --upgrade pip && \
    pip install uv

# Copy all files into the container
COPY . /app

# Use uv to install the package
RUN uv sync

# Set default command to run the MCP server
CMD ["uv", "run", "src/gitingest-mcp/server.py"]