# Behave Sandbox

A dockerized Behave suite for practice purposes.

## How to Run

At the root level directory run the command:<br>
`. run_tests.sh`

This will create all the docker containers, run the Behave tests then destroy all the containers.

## How to Run Tests Locally

At the root level directory run the command:<br>
`docker-compose up -d wiremock`

This will create the wiremock container.
In order to run the tests locally run the command:<br>
`behave`