- before you can build the challenge locally, you must replace the variable `CHALL_URL` inside the `docker-compose.yml` with an `https` endpoint pointing to the `web` service (port `8000`).
- an easy way to do so is by using `ngrok http 8000` on your machine and use the `https` link provided by ngrok.
- note that ngrok will present a confirmation prompt for standard user agents, so if you want to bypass it just change your browser's user agent to whatever is not a common one.
- the headless browser's user agent is not affected by this problem