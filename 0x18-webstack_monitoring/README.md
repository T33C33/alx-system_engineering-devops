 0x18. Webstack monitoring
# DevOpsSysAdminmonitoring

**Weight:** 1

**Project will start:** Aug 14, 2024 6:00 AM

**Must end by:** Aug 15, 2024 6:00 AM

**Checker was released at:** Aug 14, 2024 12:00 PM

**An auto review will be launched at the deadline**

## Concepts

For this project, we expect you to look at these concepts:

- Monitoring
- Server

## Background Context

“You cannot fix or improve what you cannot measure” is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:

1. Application monitoring: getting data about your running software and making sure it is behaving as expected
2. Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)

## Resources

Read or watch:

- [What is server monitoring](https://www.datadoghq.com/blog/what-is-server-monitoring/)
- [What is application monitoring](https://www.datadoghq.com/blog/what-is-application-monitoring/)
- [System monitoring by Google](https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/)
- [Nginx logging and monitoring](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- Why is monitoring needed
- What are the 2 main areas of monitoring
- What are access logs for a web server (such as Nginx)
- What are error logs for a web server (such as Nginx)

## Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what the script is doing

## Your servers

| Name           | Username | IP             | State   |
| -------------- | -------- | -------------- | ------- |
| 141771-web-01  | ubuntu   | 34.202.158.50  | running |
| 141771-web-02  | ubuntu   | 18.207.142.16  | running |
| 141771-lb-01   | ubuntu   | 34.227.89.76   | running |

## Tasks

### 0. Sign up for Datadog and install datadog-agent (mandatory)

For this task head to [https://www.datadoghq.com/](https://www.datadoghq.com/) and sign up for a free Datadog account. When signing up, you’ll have the option of selecting statistics from your current stack that Datadog can monitor for you. Once you have an account set up, follow the instructions given on the website to install the Datadog agent.

- Sign up for Datadog - Please make sure you are using the US website of Datagog ([https://app.datadoghq.com](https://app.datadoghq.com))
- Use the US1 region
- Install datadog-agent on web-01
- Create an application key
- Copy-paste in your Intranet user profile (here) your DataDog API key and your DataDog application key.
- API Key => 3e48222556fa61e90e5be52c1cda013c
- APP Key => 790d0b0926965963b2a9cb5765848b9b59636327
- Your server web-01 should be visible in Datadog under the host name XX-web-01
    - You can validate it by using this API
    - If needed, you will need to update the hostname of your server

