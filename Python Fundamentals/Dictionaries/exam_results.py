def input_score(name, score, res_dict):
    if name not in res_dict.keys():
        res_dict[name] = 0
    if score > res_dict[name]:
        res_dict[name] = score


def input_submission(language, submissions_dict):
    if language not in submissions_dict.keys():
        submissions_dict[language] = 0
    submissions_dict[language] += 1


def user_ban(name, res_dict):
    if name in res_dict.keys():
        del res_dict[name]


results = {}
submissions = {}

while True:
    command = input().split('-')

    if len(command) == 1:
        break
    elif len(command) == 2:
        username = command[0]
        user_ban(username, results)
    elif len(command) == 3:
        username, language_used, points = command[0], command[1], int(command[2])
        input_score(username, points, results)
        input_submission(language_used, submissions)

print('Results:')
for key, value in results.items():
    print(f'{key} | {value}')
print('Submissions:')
for key, value in submissions.items():
    print(f'{key} - {value}')