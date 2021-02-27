def get_all_responsible(page, paginate_by, filters):
    url = '/responsible'
    page_obj = Page(page, paginate_by, url)
    result = responsable_repository.find_all(page_obj, 'responsable', filters)
    return result
