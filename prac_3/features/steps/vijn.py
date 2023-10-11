from behave import *
from encoder import Encoder


@given('a running encoder object (vijn)')
def step_impl(context):
    context.encoder = Encoder()


@when('a {string} and {key} are provided (vijn)')
def step_impl(context, string, key):
    context.string = string
    context.key = key


@then('decrypted (vijn) string should be equal to {correct_string}')
def step_impl(context, correct_string):
    assert correct_string == context.encoder.vijn_decrypt(context.string, context.key)


@then('decrypt (vijn) function should raise a value error')
def step_impl(context):
    try:
        context.encoder.vijn_decrypt(context.text, context.key)
    except Exception as e:
        assert type(e) == ValueError
