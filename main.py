import sys
import urllib.request
import urllib.error
import json

def main():
  if len(sys.argv) < 2:
    print("Please provide a GitHub username")
    return
  
  username = sys.argv[1]
  url = f"https://api.github.com/users/{username}/events"
  event_map = {
    "PushEvent": "pushed a commit to",
    "WatchEvent": "starred",
    "ForkEvent": "forked",
  }

  request = urllib.request.Request(
    url,
    headers={"User-Agent": "github-activity-cli"}
  )

  try:
    with urllib.request.urlopen(request) as response:
      response_bytes = response.read() # bytes
      json_text = response_bytes.decode() # JSON
      activities = json.loads(json_text)

      if not activities:
        print(f"{username} has no recent activities")
        return
      
      for event in activities:
        event_type = event.get("type")
        repo = event.get("repo", {}).get("name", "a repository")
        payload = event.get("payload", {})

        if event_type == "IssuesEvent":
          action = payload.get("action", "did something to")
          issue_title = payload.get("issue", {}).get("title", "")
          print(f"- {username} {action} issue '{issue_title}' in {repo}")
        
        elif event_type == "IssueCommentEvent":
          issue_title = payload.get("issue", {}).get("title", "an issue")
          print(f"- {username} commented on '{issue_title}' in {repo}")

        elif event_type == "PullRequestEvent":
          action = payload.get("action", "did something to")
          pr_number = payload.get("pull_request", {}).get("number", "")
          print(f"- {username} {action} a pull request {pr_number} in {repo}")

        elif event_type == "CreateEvent":
          ref_type = payload.get("ref_type", "something")
          print(f"- {username} created a {ref_type} in {repo}")

        elif event_type in event_map:
          print(f"- {username} {event_map[event_type]} {repo}")

        else:
          print(f"- {username} performed {event_type} on {repo}")

  except urllib.error.HTTPError as e:
    if e.code == 404:
      print(f"User {username} not found")
    elif e.code == 403:
      print("Rate limit exceeded. Try again later")
    else:
      print(f"HTTP error: {e.code}")

  except urllib.error.URLError as e:
    print(f"Error accessing URL: {e.reason}")

if __name__ == "__main__":
  main()
