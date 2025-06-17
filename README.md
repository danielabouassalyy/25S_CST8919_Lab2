# CST8919 Lab 2: Building a Web App with Threat Detection

**Student**: Daniel Abou-Assaly/041173113
**Demo video**: 

---

## What I Learned
- How to deploy a Python Flask app to Azure App Service  
- How to enable diagnostic logging and ship logs to Log Analytics  
- How to use Kusto Query Language (KQL) to detect failed-login spikes  
- How to configure an Azure Monitor alert rule with Action Groups

## Challenges & Improvements
- **Challenges**: Fighting PowerShell escaping for runtime strings; trimming down ZIPs so Oryx could build  
- **Improvements**: In a real setup, I’d log the user’s IP address and store login attempts in a database (like Cosmos DB or Azure SQL) so I can spot attacks across multiple machines. I’d also add a lockout or slow-down after a few failed   tries to stop brute-forcing.

## KQL Query & Explanation
```kql
AppServiceConsoleLogs
| where ResultDescription contains "FAILED login"
| summarize failedCount = count() by bin(TimeGenerated, 5m)
| where failedCount > 5
```
**Explanation:**

- **Source table**  
  Start with `AppServiceConsoleLogs`, which captures all console output from our Flask app.

- **Filter failed logins**  
  Use `where ResultDescription contains "FAILED login"` to select only log entries that include the phrase **“FAILED login.”**

- **Group and count**  
  Apply `summarize failedCount = count() by bin(TimeGenerated, 5m)` to bucket the filtered entries into 5-minute intervals and count the number of failures in each bucket.

- **Threshold check**  
  Finally, `where failedCount > 5` returns only those 5-minute intervals where more than five failed logins occurred, indicating a potential brute-force attack.
