# [GitHub Activity CLI](https://roadmap.sh/projects/github-user-activity)

A simple command-line tool that fetches and displays the recent activity of any GitHub user using the GitHub public API. This project demonstrates how to work with:
- HTTP APIs
- JSON data
- Python standard library networking
- Command-line interfaces (CLI)

## Features
Fetches a user’s most recent GitHub activity, such as:
- Pushes
- Issues
- Pull requests
- Stars
- Forks

Error handling for:
- Invalid users
- Rate limits
- Network failures

## How to use this project

Clone the repository:

```
git clone https://github.com/HienXuanPham/github-activity-cli.git
cd github-activity-cli
```

Run the script from the terminal:

```
python main.py <github_username>
```

## How it Works

1. Reads the GitHub username from the command line

2. Calls the GitHub Events API:

```
https://api.github.com/users/<username>/events
```

3. Parses the JSON response

4. Converts GitHub event objects into readable messages

5. Prints them to the terminal

## License

MIT License ( ദ്ദി ˙ᗜ˙ )
