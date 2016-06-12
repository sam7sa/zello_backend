import sqlalchemy as sa
from paginate_sqlalchemy import SqlalchemyOrmPage
from ..models.blog_record import BlogRecord

class BlogRecordService(object):

    @classmethod
    def all(cls, request):
        query = request.dbsession.query(BlogRecord)
        return query.order_by(sa.desc(BlogRecord.created))


    @classmethod
    def by_id(cls, _id, request):
        query = request.dbsession.query(BlogRecord)
        return query.get(_id)


    @classmethod
    def get_paginator(cls, request, page=1):
        query = request.dbsession.query(BlogRecord)
        query = query.order_by(sa.desc(BlogRecord.created))
        query_params = request.GET.mixed()

        def url_maker(link_page):
            query_params['page'] = link_page
            return request.current_route_url(_query=query_params)

        return SqlalchemyOrmPage(query, page, items_per_page=5,
                                url_maker=url_maker)

