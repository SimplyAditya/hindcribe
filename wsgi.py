import sys
import os

# Ensure vendored argostranslate is found
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(script_dir, "vox_bridge", "utils"))

from vox_bridge.main import app

if __name__ == "__main__":
    app.run()
