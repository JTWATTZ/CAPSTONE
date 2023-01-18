
curl -X  POST  -vL \
'https://api.kroger.com/v1/connect/oauth2/token' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-H 'Authorization: Basic cHJvamVjdHB5dGhvbmphdmFzY3JpcHQtMDg3NGNiNGM4NGY0MmNlNmE3ZTA3YjJmOTE4Yjg1MzAyNjg4OTAyNzc0MzczNzk1OTAwOkp6OUp1TlpScWdwLTJ6M0F1WGczak5POTZwOEhZS18yM0sxZXdNdm0=' \
-d 'grant_type=client_credentials&scope=product.compact'



var settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://api.kroger.com/v1/connect/oauth2/token",
    "method": "POST",
    "headers": {
      "Content-Type": "application/x-www-form-urlencoded",
      "Authorization": "Basic cHJvamVjdHB5dGhvbmphdmFzY3JpcHQtMDg3NGNiNGM4NGY0MmNlNmE3ZTA3YjJmOTE4Yjg1MzAyNjg4OTAyNzc0MzczNzk1OTAwOkp6OUp1TlpScWdwLTJ6M0F1WGczak5POTZwOEhZS18yM0sxZXdNdm0="
    },
    "data": {
      "grant_type": "client_credentials",
      "scope": "product.compact"
    }
  }
  
  $.ajax(settings).done(function (response) {
    console.log(response);
  });
  