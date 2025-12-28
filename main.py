import sys
import urllib.request
import json

def main():
  if len(sys.argv) > 1:
    username = sys.argv[1]
    url = f"https://api.github.com/users/{username}/events"
    map_events = {
      "CreateEvent": "created",
      "PushEvent": "pushed a commit to",
      "PullRequestEvent": "opened a pull request in",
      "IssueCommentEvent": "commented in"
    }

    try:
      with urllib.request.urlopen(url) as response:
        response_bytes = response.read() # bytes
        json_text = response_bytes.decode() # JSON
        activities = json.loads(json_text)
        
        for event in activities:
          t = event.get("type")
          if t in map_events:
            print(f"- {username} {map_events[t]} {event.get('repo', {}).get('name')}")

    except urllib.error.URLError as e:
      print(f"Error accessing URL: {e.reason}")
  else:
    print("Please provide a GitHub username")


if __name__ == "__main__":
  main()
