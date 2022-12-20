from behave import Given, When, Then
from main import incrementor

@Given("a new incrementor of size {val}")
def given_incrementor(context, val: str):
    context.incrementor = incrementor(int(val))

@When("we increment {num}")
def when_increment(context, num):
    context.results = context.incrementor(int(num))

@Then("we should see {results}")
def then_results(context, results: str):
    assert(context.results == int(results))