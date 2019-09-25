### Usage for common API cases:
##### (Note: for json format add `&format=json` to url)
* Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by 
channel and country, sorted by clicks in descending order
```
/api/metrics/?date_before=2017-06-01&groupby=channel,country&annotate=impressions,clicks&ordering=-clicks__sum
```
* Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by 
date in ascending order
```
/api/metrics/?date_after=2017-05-01&date_before=2017-05-31&os=ios&groupby=date&annotate=installs&ordering=date
```
* Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue 
in descending order
```
/api/metrics/?date_after=2017-06-01&date_before=2017-06-01&country=US&groupby=os&annotate=revenue&ordering=-revenue__sum
```
* Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order
```
/api/metrics/?country=CA&groupby=channel&annotate=spend,cpi&ordering=-cpi__sum
```
