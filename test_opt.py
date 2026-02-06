
import os
import asyncio
from pageindex.page_index import page_index

# Mock doc
doc = "tests/markdowns/cognitive-load.md" # Wait, page_index expects a PDF
# I need a PDF to test Parsing.

# Let's just check if it fails on opt access by mocking page_index_main call.
from pageindex.page_index import page_index_main
from pageindex.utils import ConfigLoader

try:
    opt = ConfigLoader().load()
    print("Config loaded keys:", vars(opt).keys())
    # Mock doc as something that will fail later but let's see if it gets past opt access
    page_index_main("dummy.pdf", opt=opt)
except Exception as e:
    print(f"Caught expected or unexpected error: {e}")
