from behave import *
from encoder import Encoder

@given('a running encoder object')
def step_impl(context):
    context.encoder = Encoder()

@when('a {string} and {offset} are provided')
def step_impl(context, string, offset):
    context.string = string
    context.offset = offset

@then('decrypted string should be equal to {correct_string}')
def step_impl(context, correct_string):
    assert correct_string == context.encoder.caesar_decrypt(context.string, context.offset)

@then('decrypt function should raise a value error')
def step_impl(context):
    try:
        context.encoder.caesar_decrypt(context.text, context.offset)
    except Exception as e:
        assert type(e) == ValueError
