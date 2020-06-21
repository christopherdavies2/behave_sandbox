echo "-------- Running tests --------"
docker-compose -f docker-compose.yml up --build --exit-code-from=behave_test
echo "-------- Shutting down containers --------"
docker-compose -f docker-compose.yml down