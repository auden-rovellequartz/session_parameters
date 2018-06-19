# -*- coding: utf-8 -*-

def home():
	form = FORM(
		DIV(
			LABEL("fruit: "),
			INPUT(
				_type = "text",
				_name = "fruit",
				),
			),
		DIV(
			LABEL("vegetable: "),
			INPUT(
				_type = "text",
				_name = "vegetable",
				),
			),
		INPUT(
			_type = "submit",
			_value = "Submit Fruit & Vegetable",
			)
		)
	if (form.process().accepted):
		session.fruit = form.vars.fruit
		session.vegetable = form.vars.vegetable
		redirect(
			URL(
				a = "session_parameters",
				c = "c01",
				f = "page_two",
				)
			)
	return dict(
		form = form,
		)
def page_two():
	home = A(
		"home",
		_href = URL(
			a = "session_parameters",
			c = "c01",
			f = "home",
			)
		)
	return dict(
		home = home,
		)
