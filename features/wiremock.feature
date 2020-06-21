Feature: Wiremock Tutorial

  A feature to demo using Wiremock in Docker

  Scenario: run a simple test
     Given I have mocked an endpoint
     When I call the mock endpoint
     Then I get the mocked response