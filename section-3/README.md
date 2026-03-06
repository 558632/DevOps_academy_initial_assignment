Task B – CI/CD pipeline is stuck
Debug Steps:
1/ Identify stuck stage/job - Check Jenkins Console Output / GitLab Job Trace
2/ Check logs - Look for build errors, network timeouts, or dependency issues
3/ Verify runner/agent health - CPU, memory, disk space, agent status
4/ Check external dependencies - Docker images, package registries, databases, APIs
5/ Check queue/executors - Ensure runner capacity is available
Unblock Pipeline:
1/ Abort & retry job
2/ Restart runner/agent (sudo systemctl restart gitlab-runner)
3/ Remove stuck containers (docker rm -f <container>)
Prevent Future Hangs:
1/ Set stage/job timeouts (GitLab timeout: 20m, Jenkins timeout)
2/ Monitor runners and resources
3/ Ensure sufficient CI worker capacity
