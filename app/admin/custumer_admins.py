from models.custumers import Feedback, ContactUS

from sqladmin import ModelView


class FeedbackAdmin(ModelView, model=Feedback):
    name = 'Feedback'
    name_plural = 'Feedbacks'

    column_list = [Feedback.id, Feedback.name]
    form_columns = [Feedback.id, Feedback.name, Feedback.job, Feedback.desc, Feedback.image]
    column_searchable_list = [Feedback.name, Feedback.job]
    

class ContactUSAdmin(ModelView, model=ContactUS):
    name = 'Contact US'
    name_plural = 'Contact US'

    column_list = [ContactUS.id, ContactUS.name, ContactUS.phone]
    form_columns = [ContactUS.id, ContactUS.name, ContactUS.phone]
    column_searchable_list = [ContactUS.name, ContactUS.phone]
    