from behave import given, when, then


@when('search "{product}"')
def step_impl(context, product):
    context.current_page = context.current_page.searchProduct(product)

@when('click precio')
def step_impl(context):
    context.current_page = context.current_page.clickPrice()
#
# @then('verify price range product "<"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then verify price range product "<"')
#
# @when('save first price and name product')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When save first price and name product')
#
# @when('click first product')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When click first product')
#
# @then('see "detalle del producto"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then see "detalle del producto"')
#
# @when('click "Añadir"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When click "Añadir"')
#
# @then('verify add bucket product')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then verify add bucket product')
#
# @then('verify number bucket are 1')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then verify number bucket are 1')
#
# @when('click "carro"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When click "carro"')
#
# @then('see "Mi cesta"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then see "Mi cesta"')
#
# @then('verify name and price product')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then verify name and price product')
#
# @when('click "+"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When click "+"')
#
# @when('verify number product are 2')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When verify number product are 2')
#
# @when('verify price product are double')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When verify price product are double')
#
# @when('click "-"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When click "-"')
#
# @when('verify number product are 1')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When verify number product are 1')
#
# @when('verify name and price product')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When verify name and price product')
#
