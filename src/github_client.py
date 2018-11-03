import datetime
import terminal_print
import user_data
from pr_reference_scrapper import get_pr_references_numbers_if_exist
from github import Github

class Git:
  def __init__(self):
    self.config = user_data.Config()
    self.github_secret_key = user_data.Github_secret_key()
    try:
      access_token = self.github_secret_key.get()
      self.git = Github(access_token)
    except Exception as e:
      print('--Error:', e)

  def get_repository(self, git):
    repo_name = self.config.get('repo', 'name')
    return git.get_repo(repo_name)

  def get_formatted_date(self):
    now = datetime.datetime.now()
    minute = '{}{}'.format(0, now.minute) if now.minute <= 9 else now.minute
    return '{}/{}/{} {}:{}'.format(now.day, now.month, now.year, now.hour, minute)

  def get_issue_status(self, issue):
    url = issue.html_url
    all_pr_numbers = get_pr_references_numbers_if_exist(url)

    if all_pr_numbers is None or len(all_pr_numbers) <= 0:
      return 'open'
    elif self.are_all_pr_numbers_similiar(all_pr_numbers):
      pr_number = all_pr_numbers[0]
      return self.get_pr_state(pr_number)
    else:
      return self.handle_multiple_prs(all_pr_numbers)

  def handle_multiple_prs(self, all_pr_numbers):
    state = 'open'
    for pr_amount in range(len(all_pr_numbers)-1, -1, -1):
      pr = all_pr_numbers[pr_amount]
      state = self.get_pr_state(pr)
      if state == 'closed':
        return state

    return 'multiple_prs'

  def get_pr_state(self, pr_number):
    try:
      pull_request = self.repo.get_pull(pr_number)
      if pull_request.is_merged():
        return 'closed'
      elif pull_request.state == 'closed':
        return 'open'
      else:
        return 'in_progress'
    except Exception as e:
      print('--Error: couldn\'t get pull request with number: {}. Code:{}'.format(pr_number, e))
      return 'error | pr_number: {}'.format(pr_number)

  def are_all_pr_numbers_similiar(self, pr_numbers):
    if len(pr_numbers) > 1:
      for n, number in enumerate(pr_numbers):
        if n > 0 and number != pr_numbers[n-1]:
          return False

    return True

  def get_issues_records(self):
    issues_records = []
    try:
      self.repo = self.get_repository(self.git)
    except:
      print('--Error: Github instance is None -  make sure you have configured your github secret key.')
      print('---If you\'re struggling with running this script, read README tutorial:', 'https://github.com/letelete/Github-issues-documentation')
      return

    issues = self.repo.get_issues()
    for n, issue in enumerate(issues):
      terminal_print.print_itteration_status('Collecting issues', n, issues.totalCount)
      if issue.html_url.find('pull') is -1:
        url = issue.html_url
        title =  issue.title
        status = self.get_issue_status(issue)
        date = self.get_formatted_date()
        record = [url, title, status, date]

        issues_records.append(record)

    return issues_records
    