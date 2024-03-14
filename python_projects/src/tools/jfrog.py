import subprocess
from typing import Dict
import logging


def is_cli_installed() -> bool:
    run_it = subprocess.run(
        ["jfrog", "--version"], capture_output=True, text=True
    )

    if run_it.returncode != 0:
        logging.error("Failed to execute", run_it.stderr)
        return False
        # sys.exit(run_it.returncode)

    return True


def run_jfrog_audit() -> Dict:
    run_it = subprocess.run(
        ["jfrog", "audit", "--format", "sarif"], capture_output=True, text=True
    )

    if run_it.returncode != 0:
        logging.error("Failed to execute", run_it.stderr)
        raise Exception(run_it.stderr)

    return run_it.stdout


def code_has_secrets(audit_output: Dict) -> bool:
    for run in audit_output['runs']:
        if run['tool']['driver']['name'] == "JFrog Secrets scanner":
            secret_scan_results = run['results']

    if len(secret_scan_results) > 0:
        return True
    else:
        return False
