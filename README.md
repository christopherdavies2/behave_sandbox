# Behave Sandbox

A dockerized Behave suite for practice purposes.

## Run All Tests

At the root level directory run the command:<br>
`. run_tests.sh`

This will create all the docker containers, run the Behave tests then remove all the containers.

## Run Tests Locally

Ensure there are no containers running on your machine by running the command:<br>
`docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)`

Then, at the root level directory of the repo run the command:<br>
`docker-compose -f docker-compose.yml up --build --exit-code-from=behave_test`

This will create all the docker containers and run the Behave tests.

You can now modify any code on your local machine and this will be reflected in the container upon running:<br>
`docker-compose up --exit-code-from=behave_test`

This will run the latest code on your machine within the container and stop all containers after the tests have finished.