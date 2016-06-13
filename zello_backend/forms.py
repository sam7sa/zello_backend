from wtforms import (
    Form,
    StringField,
    TextAreaField,
    HiddenField,
    validators,
)

strip_filter = lambda x: x.strip() if x else None


class BlogCreateForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=255)],
                        filters=[strip_filter])
    body = TextAreaField('Contents', [validators.Length(min=1)],
                        filters=[strip_filter])


class BlogUpdateForm(BlogCreateForm):
    id = HiddenField()


class SellingCreateForm(Form):
    title = StringField('code', [validators.Length(min=1, max=255)],
                        filters=[strip_filter])


class SellingUpdateForm(SellingCreateForm):
    id = HiddenField()
