# banking-conversational-ai-cx
Dialogflow CX banking virtual assistant with BigQuery backend, Cloud Run webhook integration, OpenAPI tools, and voice-enabled IVR menu.

## What the code currently does

The Flask app serves the banking chat UI and exposes `POST /chat`. Each request creates or reuses a session ID and calls a Dialogflow CX agent deployment using Google Cloud credentials. The browser UI is served from `index.html`.

## Setup

Install `flask` and configure Google Cloud Application Default Credentials. Before deployment, move the project, location, agent, and deployment identifiers into environment variables; they are currently hard-coded in `app.py`.

## Current status

The web-to-Dialogflow integration is implemented as a small prototype. Automated tests, production configuration, input validation, and deployment documentation are not currently present.

