<img src="assets/demo.gif" width="415">

# Discord Dynamic Status

---

## Description

The program let you have dynamic status on discord

## Maintenance status

This is a legacy experiment using a user-account token and a private settings endpoint. API compatibility and permitted usage must be reviewed before running it. Do not paste real tokens into source code or public issues. Dependency updates alone do not validate this integration.

## Getting started

#### Connect to Discord

Provide `DISCORD_USER_TOKEN` through your shell or secret manager. The process reads it from its environment; Docker Compose forwards the same variable. Do not paste it into a source file, a command saved in shell history, or a public issue. If an old token was committed, revoke it with Discord before using a replacement.

#### Start the program

##### Using python3

Install all the dependencies  
`pip install -r requirements.txt`

Start the program  
`python3 main.py`

##### Using docker-compose

Start the docker-compose.yml
`docker-compose up`

## Usage

For now, only the **spaceInvader** animation is available...

## Roadmap

- [x] Dockerize the program
- [ ] Change animations inside the docker
- [ ] Create new animations

## Contributing

Feel free to use the program and make it grow.  
And share your custom animations 😃
