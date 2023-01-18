var settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://api.kroger.com/v1/products?filter.brand=Kroger&filter.term=fish&filter.locationId=20148",// Brand is Kroger, Term is the search, Location will be zip
    "method": "GET",
    "headers": {
      "Accept": "application/json",
      "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYXBpLmtyb2dlci5jb20vdjEvLndlbGwta25vd24vandrcy5qc29uIiwia2lkIjoiWjRGZDNtc2tJSDg4aXJ0N0xCNWM2Zz09IiwidHlwIjoiSldUIn0.eyJhdWQiOiJwcm9qZWN0cHl0aG9uamF2YXNjcmlwdC0wODc0Y2I0Yzg0ZjQyY2U2YTdlMDdiMmY5MThiODUzMDI2ODg5MDI3NzQzNzM3OTU5MDAiLCJleHAiOjE2NzMzMjM4MjIsImlhdCI6MTY3MzMyMjAxNywiaXNzIjoiYXBpLmtyb2dlci5jb20iLCJzdWIiOiIyNjdjODgwMi0yYWNjLTU4YTktYWIxZC04NmRjNWY0MDZkZTIiLCJzY29wZSI6InByb2R1Y3QuY29tcGFjdCIsImF1dGhBdCI6MTY3MzMyMjAyMjcxMDQzNDc4NywiYXpwIjoicHJvamVjdHB5dGhvbmphdmFzY3JpcHQtMDg3NGNiNGM4NGY0MmNlNmE3ZTA3YjJmOTE4Yjg1MzAyNjg4OTAyNzc0MzczNzk1OTAwIn0.Z8TZX8Zd-FQ19ACQ0ZqKmjX_CrL3x2u9qBzcvHmhMwcdeauahBtIsu6qx-WKYMhJqS4SHgc4LPiCyMrTSlAROaqWb5v3wNrWtWQByMvzyEqOFBMLt1ClC7GIY-oIp60vUId6M0ugWYXGyIjWoNkz7SU5Bt6SbSOw-TmTV8a5jJNjxsmL7Usxkk9Gtp9T_XcdmVdVovVqRyyKFuVju5Wv8J2pCpfgzDbuXAgPan6PziErG_5KHcDj49JzAc1uuwsIudhXLJqVClwuENLfJvbSUNssC8hlBQ1gA1blIrFVCsP7EWX5kuq_3a7d5C6NwO9d4b4uJ-ysM9Xg6VkTN0NjpQ"
    }
  }
  
  $.ajax(settings).done(function (response) {
    console.log(response);
  });
  

curl -X GET \
 'https://api.kroger.com/v1/products?filter.brand=Kroger&filter.term=fish' \
 -H 'Accept: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYXBpLmtyb2dlci5jb20vdjEvLndlbGwta25vd24vandrcy5qc29uIiwia2lkIjoiWjRGZDNtc2tJSDg4aXJ0N0xCNWM2Zz09IiwidHlwIjoiSldUIn0.eyJhdWQiOiJwcm9qZWN0cHl0aG9uamF2YXNjcmlwdC0wODc0Y2I0Yzg0ZjQyY2U2YTdlMDdiMmY5MThiODUzMDI2ODg5MDI3NzQzNzM3OTU5MDAiLCJleHAiOjE2NzMzMjM4MjIsImlhdCI6MTY3MzMyMjAxNywiaXNzIjoiYXBpLmtyb2dlci5jb20iLCJzdWIiOiIyNjdjODgwMi0yYWNjLTU4YTktYWIxZC04NmRjNWY0MDZkZTIiLCJzY29wZSI6InByb2R1Y3QuY29tcGFjdCIsImF1dGhBdCI6MTY3MzMyMjAyMjcxMDQzNDc4NywiYXpwIjoicHJvamVjdHB5dGhvbmphdmFzY3JpcHQtMDg3NGNiNGM4NGY0MmNlNmE3ZTA3YjJmOTE4Yjg1MzAyNjg4OTAyNzc0MzczNzk1OTAwIn0.Z8TZX8Zd-FQ19ACQ0ZqKmjX_CrL3x2u9qBzcvHmhMwcdeauahBtIsu6qx-WKYMhJqS4SHgc4LPiCyMrTSlAROaqWb5v3wNrWtWQByMvzyEqOFBMLt1ClC7GIY-oIp60vUId6M0ugWYXGyIjWoNkz7SU5Bt6SbSOw-TmTV8a5jJNjxsmL7Usxkk9Gtp9T_XcdmVdVovVqRyyKFuVju5Wv8J2pCpfgzDbuXAgPan6PziErG_5KHcDj49JzAc1uuwsIudhXLJqVClwuENLfJvbSUNssC8hlBQ1gA1blIrFVCsP7EWX5kuq_3a7d5C6NwO9d4b4uJ-ysM9Xg6VkTN0NjpQ'

  &filter.locationId={{LOCATION_ID}}