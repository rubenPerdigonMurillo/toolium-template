from behave import given, when, then

from pageobjects.dashboard import DashboardPageObject


@given('open carrefour')
def step_impl(context):
    context.current_page = DashboardPageObject()
    context.current_page.open()

@when('click accept cookies')
def step_impl(context):
    context.current_page = context.current_page.clickAccept()

@when('click busqueda')
def step_impl(context):
    context.current_page = context.current_page.clickSearch()

@when('click search"')
def step_impl(context, product):
    context.current_page = context.current_page.searchProduct(product)
#
#
# @when('click "Precio"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When click "Precio"')
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
