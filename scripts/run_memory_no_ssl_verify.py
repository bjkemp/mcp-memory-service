#!/usr/bin/env python3
"""
MCP Memory Service launcher with SSL verification disabled
This script disables SSL certificate verification before launching the memory service
"""
import os
import sys
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Set environment variable to disable requests SSL verification
os.environ["PYTHONHTTPSVERIFY"] = "0"

# Import and run the memory server
try:
    from mcp_memory_service.server import main
    sys.exit(main())
except ImportError:
    print("Error: Could not import the MCP memory service. Make sure it's installed correctly.")
    sys.exit(1)
