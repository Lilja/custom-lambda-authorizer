# Eriks custom lambda authorizer

This is an example of a lambda authorizer using API gateway on AWS.

There two lambda functions in one file with two different handlers. `handler.auth` and `handler.get_body`

## Requirements
* `serverless`
* A section in `$HOME/.aws/credentials` with a profile of `experiments`. In this case, I assumed a role that was used in an experimental AWS account. Same thing for `$HOME/.aws/config`

## `handler.get_body`
Serverless init boilerplate. Acts as the content when using a proper `api_key`.

## `handler.auth`
The function to check an event for the required query paramter `api_key`. The function has access to environmental variables where serverless has injected the variable.

## Serverless
All configuration is done in `serverless.yml`. `serverless` is using AWS CloudFormation to create the API Gateway, the Lambda execution role and the functions itself.

It also creates the lambda authorizer to the `get_body` endpoint.
