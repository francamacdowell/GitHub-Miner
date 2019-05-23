import argparse
from miner.github_miner import GitHubMiner

# Create the CLI parser
parser = argparse.ArgumentParser(description='Get resources from GitHub project via API.')

# Add the available options to the parser
parser.add_argument("-u", "--url", dest="url",  help="GitHub repository URL in format :user/:repository", required=True)
parser.add_argument("-p", "--path", dest="path", help="Path to the git repository")
parser.add_argument("--issues_output", dest="issues_output", help="Path to the Issues output directory")
parser.add_argument("--issues_events_output", dest="issues_events_output", help="Path to the Issues events output's directory")
parser.add_argument("--issues_comments_output", dest="issues_comments_output", help="Path to the Issues comments output's directory")
parser.add_argument("--pr_output", dest="pr_output", help="Path to the Pull Requests output's directory")
parser.add_argument("--pr_events_output", dest="pr_events_output", help="Path to the Pull events output's directory")
parser.add_argument("--pr_comments_output", dest="pr_comments_output", help="Path to the Pull comments output's directory")
parser.add_argument("--pr_reviewers_output", dest="pr_reviewers_output", help="Path to the Pull reviewers output's directory")
parser.add_argument("--username", dest="username", help="The GitHub username for authentication", required=True)
parser.add_argument("--token", dest="token", help="The GitHub token for authentication", required=True)
parser.add_argument("--params", dest="params", help="The GitHub params in format: {'param1': 'value1', 'param2': 'value2, ...'}")
parser.add_argument("--mine_data_output", dest="mine_data_output", help="Path to the mined data from all API project data")

# Parse the CLI args
(options, args) = parser.parse_args()


# Start GitHub mining
miner = GitHubMiner(options.url, options.username, options.token, options.params)
miner.mine_issues(options.issues_output, options.issues_events_output, options.issues_comments_output, options.mine_data_output)
miner.mine_prs(options.pr_output, options.pr_events_output, options.pr_comments_output, options.pr_reviewers_output, options.mine_data_output)
