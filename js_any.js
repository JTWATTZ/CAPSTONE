let url = "https://api.kroger.com/v1/connect/oauth2/token";

let payload = "grant_type=client_credentials&scope=product.compact";
let headers = {
  "Content-Type": "application/x-www-form-urlencoded",
  Authorization:
    "Basic cHJvamVjdHB5dGhvbmphdmFzY3JpcHQtMDg3NGNiNGM4NGY0MmNlNmE3ZTA3YjJmOTE4Yjg1MzAyNjg4OTAyNzc0MzczNzk1OTAwOkp6OUp1TlpScWdwLTJ6M0F1WGczak5POTZwOEhZS18yM0sxZXdNdm0="
};

let response = await fetch(url, {
  method: "POST",
  headers: headers,
  body: payload
});

console.log