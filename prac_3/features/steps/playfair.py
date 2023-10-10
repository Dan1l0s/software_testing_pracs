from behave import *
from encoder import Encoder

@given('a running encoder object (playfair)')
def step_impl(context):
    context.encoder = Encoder()

@when('a {cyph_str} and keyword {keyword} are provided (playfair)')
def step_impl(context, cyph_str, keyword):
    context.cyph_str = cyph_str
    context.keyword = keyword

@then('decrypted playfair string should be equal to {decyph_str}')
def step_impl(context, decyph_str):
    assert decyph_str == context.encoder.playfair_decrypt(context.cyph_str, context.keyword)

@then('playfair decrypt function should raise a TypeError')
def step_impl(context):
    try:
        context.encoder.playfair_decrypt(context.cyph_str, context.keyword)
    except Exception as e:
        assert type(e) == TypeError