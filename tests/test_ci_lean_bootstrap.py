"""Exercise the weighted-flux workflow's bootstrap in a disposable shell.

The external elan download is replaced with a local installer fixture; the
workflow's own commands and its shell PATH propagation remain under test.
"""

from pathlib import Path
import os
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/n1-weighted-flux-gate.yml"


def bootstrap_script() -> str:
    """Extract the actual multi-line shell step, without a YAML dependency."""
    lines = WORKFLOW.read_text(encoding="utf-8").splitlines()
    name = "      - name: Install pinned Lean and cache"
    start = lines.index(name)
    run = lines.index("        run: |", start + 1)
    commands = []
    for line in lines[run + 1 :]:
        if line.startswith("      - "):
            break
        if line.strip():
            if not line.startswith("          "):
                raise AssertionError(f"Unexpected workflow shell indentation: {line}")
            commands.append(line[10:])
    return "\n".join(commands)


class BootstrapTests(unittest.TestCase):
    def test_installed_elan_is_usable_in_the_same_workflow_step(self) -> None:
        """Catch a missing same-step PATH update after installing elan."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home = root / "home"
            fake_bin = root / "bin"
            home.mkdir()
            fake_bin.mkdir()
            log = root / "calls.log"
            script = root / "installer.sh"
            script.write_text(
                'mkdir -p "$HOME/.elan/bin"\n'
                'cp "$FAKE_TOOL" "$HOME/.elan/bin/elan"\n'
                'cp "$FAKE_TOOL" "$HOME/.elan/bin/lake"\n',
                encoding="utf-8",
            )
            tool = root / "fake-tool.sh"
            tool.write_text('#!/bin/sh\nprintf "%s\\n" "$0 $*" >> "$CALL_LOG"\n', encoding="utf-8")
            tool.chmod(0o755)
            curl = fake_bin / "curl"
            curl.write_text('#!/bin/sh\nexec /bin/cat "$FAKE_INSTALLER"\n', encoding="utf-8")
            curl.chmod(0o755)
            env = dict(os.environ)
            env.update(
                HOME=str(home),
                PATH=f"{fake_bin}:/usr/bin:/bin",
                FAKE_INSTALLER=str(script),
                FAKE_TOOL=str(tool),
                CALL_LOG=str(log),
                GITHUB_PATH=str(root / "github_path"),
            )
            result = subprocess.run(
                ["bash", "-e", "-o", "pipefail", "-c", bootstrap_script()],
                cwd=ROOT,
                env=env,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            calls = log.read_text(encoding="utf-8")
            self.assertIn("elan toolchain install", calls)
            self.assertIn("lake update", calls)
            self.assertIn("lake exe cache get", calls)


if __name__ == "__main__":
    unittest.main()
