
# Overview
An attribute that we can use to determine if a transaction is forward starting. 

# Description
Broadly, if the start date > reporting date we consider it forward starting. Starting on the reporting date is not forward starting.
We don't consider the time aspect because reporting date is not a point in time, but the whole 24hour period. In other words: [2021-09-29 23:19:00] == [2021-09-29 10:19:00]

Edge cases to consider: 

* What if no start date (like equities held?)
* What if product ends on same day as it starts?
* What about products traded before the reporting date but starting after for technical reasons?
* What happens if start or report date is a weekend/bank holiday?
* What happens if this is a rollover from an existing transaction?
* What if the bank can choose to cancel/end the contract at any time up until the start date?
