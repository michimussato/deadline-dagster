

---

# ca153978-9ed2-4d3b-8f54-22584099490a

```
import json
import gazu

host = "http://miniboss/api"
user = "michimussato@gmail.com"
password = "mysecretpassword"
gazu.client.set_host(host)

login_dict = gazu.log_in(email=user, password=password)

with open(r'/home/michael/git/repos/dagster-projects/deadline-jobhandler/deadline_jobhandler_tests/test_resources/fixtures/login_dict__ca153978-9ed2-4d3b-8f54-22584099490a.json', 'w') as fo:
    json.dump(login_dict, fo, ensure_ascii=False, indent=2)

task_id = 'ca153978-9ed2-4d3b-8f54-22584099490a'
task_dict = gazu.task.get_task(task_id=task_id)

with open(r'/home/michael/git/repos/dagster-projects/deadline-jobhandler/deadline_jobhandler_tests/test_resources/fixtures/task_dict__ca153978-9ed2-4d3b-8f54-22584099490a.json', 'w') as fo:
    json.dump(task_dict, fo, ensure_ascii=False, indent=2)
```
