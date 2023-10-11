from behave import *
from encoder import Encoder


@given('a running vernam encoder object')
def step_impl(context):
    context.encoder = Encoder()


@when('a {string} and {key} are provided to vernam encoder')
def step_impl(context, string, key):
    context.string = string
    context.key = key


@then('decrypted string by vernam encoder should be equal to {correct_string}')
def step_impl(context, correct_string):
    assert correct_string == context.encoder.vernam_decrypt(context.string, context.key)


@then('vernam encoder should raise a value error')
def step_impl(context):
    try:
        context.encoder.vernam_decrypt(context.text, context.key)
    except Exception as e:
        assert type(e) == ValueError
