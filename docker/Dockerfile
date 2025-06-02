FROM python:3.12-alpine

WORKDIR /app

# Install curl, git and uv
# git is now essential for cloning the repository
RUN apk add --no-cache curl git && \
    pip install --upgrade pip && \
    pip install uv

# Clone the repository into the WORKDIR (/app)
# The '.' at the end of the git clone command ensures files are cloned
# directly into /app, not into a subdirectory /app/Gitingest-MCP
RUN git clone https://github.com/hotwa/Gitingest-MCP .

# Use uv to install the package dependencies from the cloned pyproject.toml and uv.lock
RUN uv sync

# Expose the port the app runs on
EXPOSE 8000

# Set default command to run the MCP server
# This path is relative to /app, which is the root of the cloned repository
CMD ["uv", "run", "src/gitingest_mcp/server.py"]