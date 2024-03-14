import python_projects.src.tools.jfrog as jfrog


def main():
    if not jfrog.is_cli_installed():
        print("JFrog CLI is not installed")
        return 3
   
    audit_output = jfrog.run_jfrog_audit()
    if jfrog.code_has_secrets(audit_output):
        print("Code has secrets please use the Jfrog IDE plugin to fix them.")
        return 1
    else:
        return 0