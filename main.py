import sys
import urllib.request

def main():
  if len(sys.argv) > 1:
    user_name = sys.argv[1]
    url = f"https://api.github.com/users/{user_name}/events"

    try:
      with urllib.request.urlopen(url) as response:
        data = response.read()
        print(data.decode())
    except urllib.error.URLError as e:
      print(f"Error accessing URL: {e.reason}")
  else:
    print("Please provide a GitHub username")


if __name__ == "__main__":
  main()
