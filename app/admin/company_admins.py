from app.models.company import Sponsor


from sqladmin import ModelView


class SponsorkAdmin(ModelView, model=Sponsor):
    name = 'Sponsor'
    name_plural = 'Sponsors'

    column_list = [Sponsor.id, Sponsor.url]
    form_columns = [Sponsor.id, Sponsor.url, Sponsor.image]

    