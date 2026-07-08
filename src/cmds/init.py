from typer import Argument, Option
from pathlib import Path

from ..consts import *
from ..utils import *


def init_cmd(
    name: str = Argument("Local Project", help="Name of the project."),
    no_template: bool = Option(False, "--no-template", help="Do not generate template files like README and .gitignore")
):
    """Setup the git repository and configure anchor4git."""

    # ───── SAFETY GATEWAY ────────────────────────────────────────────────── #
    git_existance_safety()
    detached_safety()

    if not is_repo(): create_repo()
    if not Path(CONFIG_FILE).exists(): generate_config()


    # Default filenames and their contents
    README_FILE = Path("README.md")
    GITIGNORE_FILE = Path(".gitignore")
    LICENSE_FILE = Path("LICENSE")

    README_TEXT = f"""# {name}\n\n[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)\n![Static Badge](https://img.shields.io/badge/build-passing-darkcyan)\n\nYour project description goes here.\n\n- [Features](#features)\n- [Installation](#installation)\n- [Usage](#usage)\n- [Contributing](#contributing)\n- [License](#license)\n- [Acknowledgements](#acknowledgements)\n\n## Features\n\nDescribe your features here.\n\n## Installation\n\nTell everyone how to install - both developers and end users.\n\n## Usage\n\nUsual commands and basic usage including getting started.\n\n## Contributing\n\nContributions are welcome! Here's how you can help:\n\n1. Fork the repository.\n2. Create a feature branch:\n```bash\ngit checkout -b feature-name\n```\n3. Commit your changes:\n```bash\ngit commit -m "Add new feature"\n```\n4. Push your branch:\n```bash\ngit push origin feature-name\n```\n5. Submit a pull request.\n\nPlease read the [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.\n\n## License\n\nThis project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.\n\n## Acknowledgements\n\n- [Anchor4Git](https://github.com/flint-studios/anchor4git) - minimal, CLI git client for remote repositories."""
    GITIGNORE_TEXT = """# ========== Operating System ==========\n.DS_Store\nThumbs.db\nDesktop.ini\n$RECYCLE.BIN/\n.Spotlight-V100/\n.Trashes/\n\n# ========== Editor / IDE ==========\n.vscode/\n.idea/\n*.swp\n*.swo\n*.tmp\n*.bak\n*.orig\n*.code-workspace\n\n# Visual Studio\n.vs/\n*.user\n*.suo\n*.userosscache\n*.sln.docstates\n\n# ========== Logs ==========\nlogs/\n*.log\nnpm-debug.log*\nyarn-debug.log*\nyarn-error.log*\npnpm-debug.log*\n\n# ========== Environment ==========\n.env\n.env.*\n!.env.example\n\n# ========== Dependencies ==========\nnode_modules/\nvendor/\n\n# ========== Build Output ==========\ndist/\nbuild/\nout/\nbin/\nobj/\ntarget/\ncoverage/\n.cache/\n.temp/\ntmp/\n\n# ========== Package Managers ==========\n.pnpm-store/\n.npm/\n.yarn/\n.yarn/cache/\n.yarn/unplugged/\n.yarn/build-state.yml\n.yarn/install-state.gz\n\n# ========== Python ==========\n__pycache__/\n*.py[cod]\n.venv/\nvenv/\nenv/\n.pytest_cache/\n.mypy_cache/\n\n# ========== Java ==========\n.gradle/\n*.class\n\n# ========== Rust ==========\ntarget/\nCargo.lock\n\n# Uncomment the next line if you're building a library instead of an application.\n# !Cargo.lock\n\n# ========== Go ==========\n*.exe\n*.test\n\n# ========== C / C++ ==========\n*.o\n*.obj\n*.so\n*.dll\n*.dylib\n*.a\n*.lib\n*.exe\n\n# ========== Archives ==========\n*.zip\n*.tar\n*.gz\n*.7z\n*.rar\n\n# ========== Secrets ==========\n*.pem\n*.key\n*.p12\n*.pfx\n\n# ==========  Miscellaneous ==========\n*.pid\n*.seed\n*.lock\n*.cache"""
    LICENSE_TEXT = """MIT License\n\nCopyright (c) [year] [name]\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE."""


    # Generate template
    if not no_template:
        if not README_FILE.exists(): README_FILE.write_text(README_TEXT)
        if not GITIGNORE_FILE.exists(): GITIGNORE_FILE.write_text(GITIGNORE_TEXT)
        if not LICENSE_FILE.exists(): LICENSE_FILE.write_text(LICENSE_TEXT)

        print()
        ok("Generated starter template. Use --no-template in the command to skip this.\n         MIT license has been created. Please replace it with your own if required.")


    print()
    ok("Finished settting up anchor4git sucessfully.")