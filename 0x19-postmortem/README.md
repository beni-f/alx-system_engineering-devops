# Outage Incident Report: April 14, 2024

## Issue Summary:
On Sunday, April 14, 2024, from 9:00 PM to 10:30 PM UTC (5:00 PM to 6:30 PM ET), our web application experienced an outage that affected 80% of our users. The primary service impacted was our user authentication service, causing users to be unable to log in or access their accounts. The root cause of the outage was a misconfiguration of our load balancer, which caused traffic to be routed to an unresponsive server.

## Timeline:
- 9:00 PM UTC (5:00 PM ET) - Issue detected; high login failure rates alert triggered.
- 9:05 PM UTC (5:05 PM ET) - Incident escalated to on-call engineer for investigation.
- 9:15 PM UTC (5:15 PM ET) - Engineer noticed load balancer misconfiguration.
- 9:30 PM UTC (5:30 PM ET) - Misconfiguration confirmed; investigation initiated.
- 9:45 PM UTC (5:45 PM ET) - Misconfiguration corrected; system monitoring initiated.
- 10:00 PM UTC (6:00 PM ET) - Incident escalated to infrastructure team.
- 10:30 PM UTC (6:30 PM ET) - Infrastructure team confirmed issue resolution.

## Root Cause and Resolution:
The root cause was a load balancer misconfiguration directing traffic to an unresponsive server. The misconfiguration was corrected by updating the load balancer configuration to ensure proper traffic routing. The infrastructure team verified service functionality post-resolution.

## Corrective and Preventative Measures:
To prevent future occurrences, the following measures will be implemented:
- Additional monitoring and alerting for load balancer health.
- Automated testing of load balancer configurations.
- Enhanced training for engineers on load balancer management.
- Regular review processes for load balancer configurations.
- Implementation of a comprehensive disaster recovery plan.

We apologize for any inconvenience and appreciate your understanding as we strive to enhance our systems and processes.
