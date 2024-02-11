import requests
import argparse
import time


def create_github_issue(repo_owner, repo_name, title, body, token):
    """Create a GitHub issue on the specified repository.

    Args:
        repo_owner: The owner of the GitHub repository.
        repo_name: The name of the GitHub repository.
        title: The title of the issue.
        body: The body text of the issue.
        token: GitHub Personal Access Token for authentication.
    """
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "title": title,
        "body": body
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        print("Issue created successfully!")
        return True
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

    print(f"Failed to create issue. Status code: {response.status_code}")
    print(response.text)
    return False


def main():
    """Parse command line arguments and call the issue creation function."""
    parser = argparse.ArgumentParser(description="Create a GitHub issue from the command line.")
    parser.add_argument("--repo_owner", help="GitHub repository owner", default="m-c-frank")
    parser.add_argument("--repo_name", help="GitHub repository name", default="ghinsert")
    parser.add_argument("--title", help="Issue title", default=str(int(1000*time.time())))
    parser.add_argument("--body", help="Issue body text", required=True)
    parser.add_argument("--token", help="GitHub Access Token", required=True)

    args = parser.parse_args()

    # Call the function with parsed arguments
    create_github_issue(args.repo_owner, args.repo_name, args.title, args.body, args.token)


if __name__ == "__main__":
    main()
