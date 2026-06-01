# lab (ejemplo)

<!-- TASK:t1_1 -->
# Task 1.1 — Create User Account

step:
copy:
```
system-view
aaa
local-user huawei password irreversible-cipher Huawei@123
local-user huawei service-type telnet ssh
local-user huawei level 3
quit
```
captura: createuser

step:
copy:
```
display local-user
```
captura: displayusers
<!-- END:t1_1 -->
